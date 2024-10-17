SELECT TOP (1000) * FROM [dbo].[InsuranceRecoveryData];

-- INSERT RECORDS 

INSERT INTO [dbo].[InsuranceRecoveryData] 
(recovery_id, patient_id, insurance_provider, policy_number, coverage_start_date, coverage_end_date, total_claim_amount, recovered_amount, claim_status, recovery_date, entry_date)
VALUES
(101, 100, 'Schneider LLC', 'POL123456', '2023-01-01 00:00:00', '2024-01-01 23:59:59', 10000.00, 8000.00, 'Approved', '2023-03-15 10:30:00', '2024-10-14');
INSERT INTO [dbo].[InsuranceRecoveryData] 
(recovery_id, patient_id, insurance_provider, policy_number, coverage_start_date, coverage_end_date, total_claim_amount, recovered_amount, claim_status, recovery_date, entry_date)
VALUES
(102, 101, 'Castaneda PLC', 'POL987654', '2023-02-10 00:00:00', '2024-02-10 23:59:59', 15000.00, 14000.00, 'Pending', '2023-05-20 09:15:00', '2024-10-14');

--UPDATE RECORDS
UPDATE [dbo].[InsuranceRecoveryData]
SET claim_status = 'Approved', recovered_amount = 15000.00
WHERE recovery_id = 1018 AND patient_id = 191;

--DELETE RECORDS
DELETE FROM [dbo].[InsuranceRecoveryData] 
WHERE recovery_id = 1024;
DELETE FROM [dbo].[InsuranceRecoveryData] 
WHERE recovery_id = 1052;
DELETE FROM [dbo].[InsuranceRecoveryData] 
WHERE recovery_id = 1831;