SELECT TOP (1000) * FROM [dbo].[PatientInformation]

-- Insert for the first record
INSERT INTO [dbo].[PatientInformation] 
(patient_id, first_name, last_name, date_of_birth, gender, blood_type, medical_history, primary_physician, date_of_admission, date_of_discharge, diagnosis, treatment_plan)
VALUES 
(115, 'arhaan', 'Wallace', '1985-08-16', 'Male', 'AB-', 'Right reduce collection later technology. Quite start wear view anyone. Case Republican more become color movement nearly painting.', 'Austin David', '2022-10-24', '2022-11-16', 'fever', 'Medication prescribed for 7 days');

-- Insert for the second record
INSERT INTO [dbo].[PatientInformation] 
(patient_id, first_name, last_name, date_of_birth, gender, blood_type, medical_history, primary_physician, date_of_admission, date_of_discharge, diagnosis, treatment_plan)
VALUES 
(114, 'ayaan', 'Briggs', '1994-11-06', 'Other', 'B-', 'Politics establish myself quickly easy both. Friend interest growth take weight hot effect. Those one goal. Scientist camera no million probably.', 'Martin Collins', '2024-02-16', '2024-02-28', 'fever', 'Surgery required');

-- UPDATE RECORDS
UPDATE [dbo].[PatientInformation] 
SET blood_type = 'B*' 
WHERE patient_id = 21 AND first_name = 'Richard';

--DELETE RECORD
DELETE FROM [dbo].[PatientInformation] 
WHERE patient_id = 53;

SELECT COUNT(*) AS COUNT_AS FROM [dbo].[PatientInformation] 