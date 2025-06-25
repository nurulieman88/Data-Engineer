import pandas as pd
from faker import Faker
import random
import datetime
import os

# Setup Faker
fake = Faker()

# Create 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Convert string to date object
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2025, 6, 1)

# Create empty list to hold customer records
data = []

# Generate 100 customer records with intentional errors
for i in range(100):
    customer_id = random.randint(1000, 1050)  # Intentionally allow duplicates
    name = fake.name() if random.random() > 0.05 else None  # 5% missing name
    email = fake.email() if random.random() > 0.1 else fake.user_name()  # 10% invalid emails
    phone_number = fake.phone_number() if random.random() > 0.1 else None  # 10% missing phone
    join_date = fake.date_between(start_date=start_date, end_date=end_date)
    country = random.choice(['Malaysia', 'Singapore', 'Thailand', 'Indonesia', 'Philippines'])

    data.append([customer_id, name, email, phone_number, join_date, country])

# Define columns
columns = ['Customer_ID', 'Name', 'Email', 'Phone_Number', 'Join_Date', 'Country']

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('data/customer_data.csv', index=False)

print("✅ 100-sample customer dataset generated successfully with intentional errors.")
