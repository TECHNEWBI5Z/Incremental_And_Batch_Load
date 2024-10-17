import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 100

# Function to generate random patient contact details
def generate_contact_details(num_records):
    contact_details = []
    
    for _ in range(num_records):
        contact_id = random.randint(1000, 9999)
        patient_id = random.randint(1, 200)  # assuming patient_id is between 1 and 5000
        phone_number = fake.phone_number()
        email = fake.email()
        address_line1 = fake.street_address()
        address_line2 = fake.secondary_address()
        city = fake.city()
        state = fake.state()
        postal_code = fake.zipcode()
        emergency_contact_name = fake.name()
        emergency_contact_phone = fake.phone_number()
        emergency_contact_relationship = random.choice(['Parent', 'Sibling', 'Friend', 'Spouse', 'Relative'])
        
        contact_details.append({
            'contact_id': contact_id,
            'patient_id': patient_id,
            'phone_number': phone_number,
            'email': email,
            'address_line1': address_line1,
            'address_line2': address_line2,
            'city': city,
            'state': state,
            'postal_code': postal_code,
            'emergency_contact_name': emergency_contact_name,
            'emergency_contact_phone': emergency_contact_phone,
            'emergency_contact_relationship': emergency_contact_relationship
        })
    
    return contact_details

# Generate the data
contact_details_data = generate_contact_details(num_records)

# Convert to DataFrame
df = pd.DataFrame(contact_details_data)

# Save to Excel on desktop
output_path = '/Users/patel/Desktop/PatientContactDetails.xlsx'  # Adjust for your username
df.to_excel(output_path, index=False)

print(f"Data saved to {output_path}")