import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:\Users\Angie\Desktop\ieman\Data Analyst\Data Engineer\test2\data_mobile.csv')

# Display first 5 rows
print(df)

# Check data types and missing values
print(df.info())

# Quick summary statistics 
print(df.describe())

# Remove negative and null sales 
df = df[df['price_range'].notnull()]
df = df[df['price_range'] >= 0]

# Standardize Date format 