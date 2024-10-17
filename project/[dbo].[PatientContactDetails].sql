SELECT TOP (1000) * FROM [dbo].[PatientContactDetails];

--INSERT RECORDS 
INSERT INTO [dbo].[PatientContactDetails] 
(contact_id, patient_id, phone_number, email, address_line1, address_line2, city, state, postal_code, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship)
VALUES 
(2222, 123, '555-1234', 'john.doe@example.com', '123 Elm Street', 'Apt 101', 'Springfield', 'Illinois', 62704, 'Jane Doe', '555-5678', 'Friend');
INSERT INTO [dbo].[PatientContactDetails] 
(contact_id, patient_id, phone_number, email, address_line1, address_line2, city, state, postal_code, emergency_contact_name, emergency_contact_phone, emergency_contact_relationship)
VALUES 
(4444, 45, '555-9876', 'sarah.smith@example.com', '456 Oak Street', 'Suite 191', 'Lake Derrickberg', 'Massachusetts', 92501, 'Mark Smith', '555-4321', 'Parent');


-- DELETE RECORDS
DELETE FROM [dbo].[PatientContactDetails]
WHERE contact_id = 1433;
DELETE FROM [dbo].[PatientContactDetails]
WHERE contact_id = 2014;
DELETE FROM [dbo].[PatientContactDetails]
WHERE contact_id = 2091;

--UPDATE RECORD
UPDATE [dbo].[PatientContactDetails]
SET email = 'faizanscf@gmail.com', phone_number = '8660602668'
WHERE contact_id = 1263;