#Q3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful 

import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'nba.csv'))
print(df.head())

print("\n info of DF at Start")
# Data Analysis
print(df.info())

# Check for missing values
print("\n Missing values in each column:")
print(df.isnull().sum())

# Fill missing values with mean for Salary column
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("\n Missing values in Salary column after filling:")
print(df['Salary'].isnull().sum())


df.drop_duplicates(inplace=True)
print("\n Info of DF after removing duplicates:")
print(df.info())

new_df = df.dropna()
print("\n Info of DF after dropping rows with missing values:")
print(new_df.info())

avg_age = df['Age'].mean()
print("\n Average Age of Players:", avg_age)

max_salary = df['Salary'].max()
print("\n Maximum Salary of Players:", max_salary)

min_salary = df['Salary'].min()
print("\n Minimum Salary of Players:", min_salary)

total_salary = df['Salary'].sum()
print("\n Total Salary of Players:", total_salary)