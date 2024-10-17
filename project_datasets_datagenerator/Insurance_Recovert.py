import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Function to generate random dates within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Define the number of rows to generate
num_records = 100

# Define the start and end dates for random date generation
start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 1, 1)

# List to hold generated data
data = []

for _ in range(num_records):
    recovery_id = random.randint(1000, 9999)
    patient_id = random.randint(1, 200)
    insurance_provider = fake.company()
    policy_number = fake.bothify(text='??#####')
    coverage_start_date = random_date(start_date, end_date)
    coverage_end_date = random_date(coverage_start_date, end_date)
    total_claim_amount = round(random.uniform(500, 50000), 2)
    recovered_amount = round(random.uniform(0, total_claim_amount), 2)
    claim_status = random.choice(['Pending', 'Approved', 'Denied'])
    recovery_date = random_date(coverage_end_date, end_date)

    # Append the row data to the list
    data.append([recovery_id, patient_id, insurance_provider, policy_number, 
                 coverage_start_date, coverage_end_date, total_claim_amount, 
                 recovered_amount, claim_status, recovery_date])

# Define the columns for the DataFrame
columns = ['recovery_id', 'patient_id', 'insurance_provider', 'policy_number', 
           'coverage_start_date', 'coverage_end_date', 'total_claim_amount', 
           'recovered_amount', 'claim_status', 'recovery_date']

# Create a DataFrame with the generated data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file on the desktop
file_path = '/Users/patel/Desktop/InsuranceRecoveryData.xlsx'
df.to_excel(file_path, index=False)

print(f"Data successfully saved to {file_path}")