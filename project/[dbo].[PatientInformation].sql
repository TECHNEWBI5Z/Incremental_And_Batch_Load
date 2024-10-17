SELECT * FROM [dbo].[PatientInformation];
-- INSERT RECORDS 
INSERT INTO PatientInformation (patient_id, first_name, last_name, date_of_birth, gender, blood_type, medical_history, primary_physician, date_of_admission, date_of_discharge, diagnosis, treatment_plan)
VALUES (111, 'John', 'Doe', '1985-07-15', 'Male', 'O+', 'Type 2 Diabetes for 10 years; Hypertension under control with medication; Family history of heart disease.', 'Smith', '2024-10-10', '2024-10-15', 'Hypertension', 'Medication and diet change');
INSERT INTO PatientInformation (patient_id, first_name, last_name, date_of_birth, gender, blood_type, medical_history, primary_physician, date_of_admission, date_of_discharge, diagnosis, treatment_plan)
VALUES (112, 'Jane', 'Smith', '1990-05-22', 'Female', 'A-', 'Mild Asthma since childhood; Allergic to penicillin; Recent history of upper respiratory infections.', 'Johnson', '2024-10-11', '2024-10-15', 'Pneumonia', 'Antibiotics and rest');

-- DELETE RECORDS
DELETE FROM [dbo].[PatientInformation]
WHERE patient_id = 10;

DELETE FROM [dbo].[PatientInformation]
WHERE patient_id = 1;

DELETE FROM [dbo].[PatientInformation]
WHERE patient_id = 5; 

--UPDATE RECORDS
UPDATE [dbo].[PatientInformation]
SET diagnosis = 'COVID-19'
WHERE patient_id = 7;