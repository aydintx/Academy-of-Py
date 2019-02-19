#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[2]:


# Count unique school names
unique_school_names = school_data["school_name"].unique()
school_count = len(unique_school_names)


# In[3]:


# Add $ sign to budget
school_data ["$budget"] = school_data ["budget"].map("${:,.2f}".format)
#Sum total budget
total_budget = school_data["budget"].sum()
total_budget = "${0:,.2f}".format(total_budget)


# In[4]:


#Sum number of the students
total_students = school_data["size"].sum()


# In[5]:


#Mean of the reading & math
average_reading = student_data["reading_score"].mean()
average_math = student_data["math_score"].mean()


# In[6]:


#% passing math&reading
passing_math = school_data_complete[school_data_complete["math_score"]>=70].count()["school_name"]
percent_passing_math=(passing_math/total_students)*100
passing_reading = school_data_complete[school_data_complete["reading_score"]>=70].count()["school_name"]
percent_passing_reading=(passing_reading/total_students)*100


# In[7]:


#Overall passing score
def add_numbers(average_reading, average_math): 
     return average_reading+ average_math
overall_passing = add_numbers(average_reading, average_math ) /2
print(overall_passing)


# In[8]:


# District Summary Table
District_Summary = pd.DataFrame({"Total Schools":[school_count], 
                                 "Total Students":[total_students],
                                "Total Budget":[total_budget],
                                 "Average Math Score":[average_math],
                                 "Average Reading Score":[average_reading],
                                 "% Passing Math":percent_passing_math,
                                 "% Passing Reading":percent_passing_reading,
                                 "Overall Passing Rate":overall_passing})

District_Summary = District_Summary[["Total Schools", "Total Students", "Total Budget", "Average Math Score",
                                 "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]]

District_Summary


# In[9]:


school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[10]:


#Number of the School types& sum of the students per school
school_types = school_data.set_index(["school_name"])["type"]
per_school_counts = school_data_complete["school_name"].value_counts()


# In[11]:


#Student budget per school
per_school_budget = school_data_complete.groupby(["school_name"]).mean()["budget"]
per_student_budget=per_school_budget/per_school_counts


# In[12]:


#Average math& reading
average_math = school_data_complete.groupby(["school_name"]).mean()["math_score"]
average_reading = school_data_complete.groupby(["school_name"]).mean()["reading_score"]
#Passing math&reading with percent
passing_math = school_data_complete[school_data_complete["math_score"]>=70].groupby("school_name").count()["student_name"]
percent_passing_math=(passing_math/per_school_counts)*100
passing_reading = school_data_complete[school_data_complete["reading_score"]>=70].groupby("school_name").count()["student_name"]
percent_passing_reading=(passing_reading/per_school_counts)*100
percent_passing_reading
#Overall passing 
overall_passing=(percent_passing_reading+percent_passing_math)/2


# In[13]:


#School summary table
School_Summary = pd.DataFrame({"School Type":school_types,
                              "Total Students":per_school_counts,
                               "Total School Budget":per_school_budget,
                               "Per Student Budget":per_student_budget,
                              "Average Math Score":average_math,
                               "Average Reading Score":average_reading,
                               "% Passing Math":percent_passing_math,
                                "% Passing Reading":percent_passing_reading,
                               "Overall Passing Rate":overall_passing})


School_Summary = School_Summary [["School Type","Total Students","Total School Budget","Per Student Budget",
                                  "Average Math Score", "Average Reading Score",
                               "% Passing Math", "% Passing Reading","Overall Passing Rate"]]

School_Summary["Total School Budget"] = School_Summary["Total School Budget"].map("${:,.2f}".format)
School_Summary["Per Student Budget"] = School_Summary["Per Student Budget"].map("${:,.2f}".format)

School_Summary


# In[14]:


#Top 5 schools
Top_Schools = School_Summary.sort_values(["Overall Passing Rate"], ascending = False)
Top_Schools.head(5)


# In[15]:


#Buttom 5 schools
Buttom_Schools = School_Summary.sort_values(["Overall Passing Rate"], ascending = True)
Buttom_Schools.head(5)


# In[16]:


#Math scores for grade levels for each schools
school_data_complete.head()
df = school_data_complete.set_index("grade")
nine_grade_score =  school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean()["math_score"]
ten_grade_score = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean()["math_score"]
eleven_grade_score =  school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean()["math_score"]
twelve_grade_score =  school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean()["math_score"]
Grade_Levels_Math = pd.DataFrame({"9th":nine_grade_score,
                              "10th":ten_grade_score,
                              "11th":eleven_grade_score,
                              "12th":twelve_grade_score})
Grade_Levels_Math = Grade_Levels_Math [["9th","10th", "11th","12th"]]
Grade_Levels_Math.index.name =None
Grade_Levels_Math


# In[17]:


#Reading scores for grade levels for each schools
nine_grade_score =  school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean()["reading_score"]
ten_grade_score = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean()["reading_score"]
eleven_grade_score =  school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean()["reading_score"]
twelve_grade_score =  school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean()["reading_score"]
Grade_Levels_Reading = pd.DataFrame({"9th":nine_grade_score,
                              "10th":ten_grade_score,
                              "11th":eleven_grade_score,
                              "12th":twelve_grade_score})

Grade_Levels_Reading = Grade_Levels_Reading [["9th","10th", "11th","12th"]]
Grade_Levels_Reading.index.name = None
Grade_Levels_Reading


# In[18]:


#Scores by School Spending
bins=[0, 585, 615, 645, 675]
group_names=["<$585", "$585-615", "$615-645", "$645-675"]
pd.cut(per_student_budget, bins, labels=group_names).head()
School_Summary["Spending Ranges (Per Student)"] = pd.cut(per_student_budget, bins, labels=group_names)


# In[19]:


#Spending Ranges (Per Student)
School_Summary["Spending Ranges (Per Student)"] = pd.cut(per_student_budget, bins, labels=group_names)
spending_math_score = School_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['Average Math Score']
Spending_reading_score = School_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['Average Reading Score']
spending_passing_math =  School_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Math']
spending_passing_reading =  School_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Reading']
overall_passing_rate =  (spending_math_score + Spending_reading_score) / 2
# Scores by School Spending in table form
Spending_Score = pd.DataFrame({"Average Math Score":spending_math_score, "Average Reading Score":Spending_reading_score,
                               "% Passing Math":spending_passing_math,"% Passing Reading":spending_passing_reading,
                                    "Overall Passing Rate":overall_passing_rate}) 
# Data munging
Spending_Score = Spending_Score[["Average Math Score", "Average Reading Score",
                               "% Passing Math","% Passing Reading","Overall Passing Rate"]]
# Display the data frame
Spending_Score


# In[20]:


# Scores by school size
size_bins = [0, 1000, 2000, 5000]
size_ranges = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
School_Summary["School Size"] = pd.cut(School_Summary["Total Students"], size_bins, labels = size_ranges)

avg_math_score = School_Summary.groupby(["School Size"]).mean()['Average Math Score']
avg_reading_score = School_Summary.groupby(["School Size"]).mean()['Average Reading Score']
percent_passing_math =  School_Summary.groupby(["School Size"]).mean()['% Passing Math']
percent_passing_reading = School_Summary.groupby(["School Size"]).mean()['% Passing Reading']
overall_passing_rate = School_Summary.groupby(["School Size"]).mean()['Overall Passing Rate']

# Scores by School Size in table form
Size_Score = pd.DataFrame({"Average Math Score":avg_math_score, "Average Reading Score":avg_reading_score,
                               "% Passing Math":percent_passing_math,"% Passing Reading":percent_passing_reading,
                                    "Overall Passing Rate":overall_passing_rate})   
# Data munging
Size_Score = Size_Score[["Average Math Score", "Average Reading Score",
                               "% Passing Math","% Passing Reading","Overall Passing Rate"]]
# Display the data frame
Size_Score


# In[21]:


#Scores by School Type
avg_math_score = School_Summary.groupby(["School Type"]).mean()['Average Math Score']
avg_reading_score = School_Summary.groupby(["School Type"]).mean()['Average Reading Score']
percent_passing_math =  School_Summary.groupby(["School Type"]).mean()['% Passing Math']
percent_passing_reading =  School_Summary.groupby(["School Type"]).mean()['% Passing Reading']
overall_passing_rate = School_Summary.groupby(["School Type"]).mean()['Overall Passing Rate']
# Scores by School Type in table form
Type_Score = pd.DataFrame({"Average Math Score":avg_math_score, "Average Reading Score":avg_reading_score,
                               "% Passing Math":percent_passing_math,"% Passing Reading":percent_passing_reading,
                                    "Overall Passing Rate":overall_passing_rate})            
# Data munging
Type_Score = Type_Score[["Average Math Score", "Average Reading Score",
                               "% Passing Math","% Passing Reading","Overall Passing Rate"]]
# Display the data frame
Type_Score

