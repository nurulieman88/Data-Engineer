import sqlite3
import pandas as pd
import os

# Check if data folder and CSV file exist
if not os.path.exists('data/customer_data.csv'):
    print("❌ CSV file not found. Please run your data generator script first.")
    exit()

# Connect to SQLite database (create if doesn't exist)
conn = sqlite3.connect('data/customer_data.db')
cursor = conn.cursor()

# Create Customer_Master table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer_Master (
        Customer_ID INTEGER,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Phone_Number TEXT,
        Join_Date TEXT,
        Country TEXT
    )
''')

print("✅ Customer_Master table created.")

# Read CSV data
df = pd.read_csv('data/customer_data.csv')

# Insert data into table
df.to_sql('Customer_Master', conn, if_exists='append', index=False)

print("✅ Data inserted into Customer_Master table.")

# Confirm total records
cursor.execute("SELECT COUNT(*) FROM Customer_Master")
total_records = cursor.fetchone()[0]
print(f"📊 Total records in table: {total_records}")

# Close connection
conn.close()
