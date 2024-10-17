import os
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

# Function to generate random date of birth between a given range
def random_date_of_birth(start_year=1940, end_year=2010):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Function to generate random date of admission and discharge based on admission date
def random_admission_and_discharge_dates():
    admission_date = fake.date_between(start_date='-2y', end_date='today')
    discharge_date = admission_date + timedelta(days=random.randint(1, 30))
    return admission_date, discharge_date

# Function to generate random blood type
def random_blood_type():
    return random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])

# Function to generate random gender
def random_gender():
    return random.choice(['Male', 'Female', 'Other'])

# Function to generate random diagnosis
def random_diagnosis():
    diagnoses = ['Hypertension', 'Diabetes', 'Asthma', 'COVID-19', 'Arthritis', 'Flu', 'Heart Disease', 'Cancer', 'Migraine']
    return random.choice(diagnoses)

# Function to generate random treatment plan
def random_treatment_plan():
    plans = [
        'Rest and hydration',
        'Medication prescribed for 7 days',
        'Physical therapy',
        'Surgery required',
        'Follow-up in 1 month',
        'Daily monitoring',
        'Referral to specialist'
    ]
    return random.choice(plans)

# Generate random patient data
def generate_patient_data(num_records):
    patient_data = []
    for patient_id in range(1, num_records + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = random_date_of_birth()
        gender = random_gender()
        blood_type = random_blood_type()
        medical_history = fake.text(max_nb_chars=200)
        primary_physician = fake.name()
        date_of_admission, date_of_discharge = random_admission_and_discharge_dates()
        diagnosis = random_diagnosis()
        treatment_plan = random_treatment_plan()
        
        patient_data.append({
            'patient_id': patient_id,
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'gender': gender,
            'blood_type': blood_type,
            'medical_history': medical_history,
            'primary_physician': primary_physician,
            'date_of_admission': date_of_admission,
            'date_of_discharge': date_of_discharge,
            'diagnosis': diagnosis,
            'treatment_plan': treatment_plan
        })
    
    return patient_data

# Number of records to generate
num_records = 100

# Generate data
data = generate_patient_data(num_records)

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file on Mac Desktop
desktop_path = os.path.expanduser('~/Desktop/')
output_file = os.path.join(desktop_path, 'PatientInformation.xlsx')
df.to_excel(output_file, index=False)

print(f"Random patient data generated and saved to {output_file}")