import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:\Users\Angie\Desktop\ieman\Data Analyst\Data Engineer\raw_sales_data_50.csv')

# Display first 5 rows
print(df.head())
# Check data types and missing values
print(df.info())

# Quick summary statistics
print(df.describe())
# Remove negative and null sales
df = df[df['Sales Amount'].notnull()]
df = df[df['Sales Amount'] >= 0]

# Standardize Date format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Fill missing region with 'Unknown'
df['Region'] = df['Region'].fillna('Unknown')

# Capitalize region names
df['Region'] = df['Region'].str.title()

# Display cleaned data
print(df.head())
# Connect to SQLite database (it will create a file if not exist)
conn = sqlite3.connect(r'C:\Users\Angie\Desktop\ieman\Data Analyst\Data Engineer\sales_data.db')

# Write DataFrame to a new table called 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

# Test: read back some data
result = pd.read_sql('SELECT * FROM sales LIMIT 5', conn)
print(result)
query = """
SELECT Product, Region, SUM("Sales Amount") AS Total_Sales
FROM sales
GROUP BY Product, Region
ORDER BY Total_Sales DESC
"""

summary_df = pd.read_sql(query, conn)
print(summary_df)
# Create a barplot of Total Sales by Region and Product
plt.figure(figsize=(12,6))
sns.barplot(data=summary_df, x='Region', y='Total_Sales', hue='Product')
plt.title('Total Sales by Product and Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
