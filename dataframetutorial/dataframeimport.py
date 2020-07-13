import pandas as pd
import os

# Method 1: Specify full path to file
#  stats = pd.read_csv('D:\\PycharmProjects\\dataframetutorial\\P4-Demographic-Data.csv')
stats = pd.read_csv('P4-Demographic-Data.csv')
print(stats)

# Get current working directory
print(os.getcwd())

# Exploring Data

# Number of Rows
print("Number of Rows:", len(stats)) # 195 rows imported

# Column Headers
print(stats.columns)

# Number of columns
print("Number of Columns: ", len(stats.columns)) # 5 Columns imported

# Top Rows
print(stats.head(5)) # Rows 0-4 (Top 5 rows)

# Bottom Rows
print(stats.tail(5)) # Rows 190-194 (Bottom 5 rows)

# Information on the Columns
print(stats.info())

# Get statistics on the columns
print(stats.describe())
# or
print(stats.describe().transpose())

