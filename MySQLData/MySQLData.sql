-- Practice Database --
use practice;

SELECT * FROM practice.applicant_details;
SELECT * FROM practice.household_details;
SELECT * FROM practice.reference;


# Insert data into the tables

SELECT * FROM practice.applicant_details;
INSERT INTO Applicant_Details (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES
('Rhys S. Montillano', '130 Manila East Rd. Baytown, Angono, Rizal', 'S', '1999-04-12', 25, 'F', 'Filipino', 'Catholic', 'College', 'Finance Clerk', 100000, 'Member', 'Marketing', 5000, 7000, 2000),
('Mary Z. Castillo', 'A. Mabini Campus, Sta. Mesa, Manila', 'W', '1992-03-25', 52, 'F', 'Filipino', 'Born Again', 'Post-graduate', 'Psychologist', 100000, 'Dependent', 'Teach online courses', 11000, 13000, 2000),
('Shashi M. Reyes', '2219 Recto Ave, Sampaloc, Manila', 'SE', '1996-03-25', 28, 'M', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Electrician', 100000, 'Non-Member', 'Pension, Investment', 7500, 8000, 500),
('Emery S. Rivera', '918 Arnaiz Ave., Makati, Manila', 'M', '1998-04-09', 26, 'M', 'Filipino', 'Catholic', 'College', 'Event Planner', 30000, 'Member', 'Theater Actor', 10000, 20000, 10000),
('Yronica A. Ayala', '1444 Metrica Street, Sampaloc, Manila', 'S', '2000-06-30', 24, 'F', 'Filipino', 'Catholic', 'College', 'Vlogger', 50000, 'Non-Member', 'Makeup Artist', 20000, 30000, 10000),
('Dante F. Rosa', '179 M. Ponce Street, Bagong Bario, Caloocan City, Manila', 'S', '1995-06-25', 28, 'M', 'Filipino', 'Catholic', 'Vocational', 'Seaman', 100000, 'Non-Member', 'None', 15000, 80000, 65000),
('Nathan E. Reyes', '7 Blk 1a-4 Road 18 Phase 5 Cogeo Village, Antipolo, Rizal', 'M', '1995-04-22', 29, 'M', 'Filipino', 'Born Again', 'College', 'Security Guard', 17000, 'Member', 'Part-time barista', 8000, 14000, 6000),
('Arlo T. Flores', '1358 Concepcion St, Santa Cruz, Manila', 'S', '1998-08-02', 25, 'M', 'Filipino', 'Catholic', 'College', 'Nurse', 40000, 'Non-Member', 'Small business owner', 13000, 20000, 7000),
('Juan Dela Cruz', '143, Masbate Street, South City Homes, Biñan, Laguna', 'SE', '1992-09-20', 32, 'M', 'Filipino', 'Iglesia ni Cristo', 'High School', 'Sales Clerk', 10000, 'Member', 'Janitor', 7000, 75000, 68000),
('Evelyn M. Mendoza', 'EDSA Extension, Mall of Asia Complex, Pasay, Manila', 'S', '1994-03-29', 30, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Human Resources Manager', 80000, 'Non-Member', 'Graphic Designing', 35000, 60000, 25000),
('Achilles S. Fajardo', 'Blk 5 Lot 19 Florida St. Summer Heights, Bacoor, Cavite', 'S', '2000-07-07', 23, 'M', 'Filipino', 'Catholic', 'College', 'Accountant', 70000, 'Member', 'Investment', 40000, 70000, 30000),
('Leslie Z. Santos', '6451 Rizal Ave, Mabalacat, Pampamga', 'M', '1994-01-17', 30, 'F', 'Filipino', 'Born Again', 'High School', 'Teacher', 30000, 'Non-Member', 'Business', 20000, 14000, 6000),
('Marian O. Buenaventura', '1124 Perez Street, Sta. Mesa, Manila', 'M', '1997-08-12', 26, 'F', 'Filipino', 'Catholic', 'Post-graduate', 'Call Center Agent', 20000, 'Member', 'None', 8000, 5000, 3000),
('Aurora T. Trinidad', '8346 Dr A Santos Avenue, Paranaque City', 'SE', '1999-08-29', 24, 'F', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Nurse', 28000, 'Member', 'Pension', 15000, 9000, 6000),
('Yula H. Bayani', 'Smith Bldg. 2294, Pasong Kawayan II, Dau, Pampanga', 'W', '1962-02-01', 62, 'F', 'Filipino', 'Catholic', 'College', 'IT Support Specialist', 31000, 'Dependent', 'Freelancing', 17000, 11000, 6000),
('Ruel F. Alcalde', 'B9 L2, Cooper St., Lancaster City, General Trias Cavite', 'S', '1999-10-30', 24, 'M', 'Filipino', 'Catholic', 'High School', 'Sales Manager', 45000, 'Non-Member', 'Small business owner', 23000, 18000, 5000),
('Luke A. Leviste', '713 P Paterno Street, Makati City', 'S', '1989-11-27', 34, 'M', 'Filipino', 'Born Again', 'College', 'Electrician', 18000, 'Member', 'None', 10000, 5000, 5000),
('Zyrus M. De Leon', '484 Sto. Cristo Street, St. Anthony Village, Carmona, Cavite', 'S', '1993-04-13', 31, 'M', 'Filipino', 'Born Again', 'High School', 'Teaching Assistant', 16500, 'Non-Member', 'None', 12000, 9000, 3000),
('Arianne B. Cruz', '8 Molave St. Cityhomes, Tanay, Rizal', 'M', '1992-05-26', 32, 'F', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Financial Manager', 48000, 'Dependent', 'Residential Property', 17000, 11000, 6000),
('Solenn P. Verde', '108 Panay Avenue 1100, Pasay City', 'M', '1999-09-17', 24, 'F', 'Filipino', 'Catholic', 'College', 'Service Desk', 32000, 'Member', 'Freelance', 11000, 5000, 6000),
('Gabbie M. Dela Cruz', '123 Sampaguita Street, Barangay San Juan, Taytay, Rizal', 'M', '1990-01-05', 34, 'F', 'Filipino', 'Catholic', 'Vocational', 'Web Developer', 60000, 'Non-Member', 'Freelance', 28000, 22000, 8000),
('Jericha L. Gutierrez', 'Unit 14F, Eastwood Parkview, Eastwood City, Bagumbayan, Quezon City', 'S', '1984-06-15', 40, 'F', 'Filipino', 'Catholic', 'Vocational', 'Call Center Agent', 35100, 'Member', 'Social media manager', 15000, 20000, 5000),
('Javier T. Rosario', '456 Mabini Street, Barangay San Isidro, Antipolo City, Rizal', 'M', '1965-09-22', 58, 'M', 'Filipino', 'Catholic', 'College', 'Graphic Designer', 20000, 'Non-Member', 'Moderator', 10000, 15000, 5000),
('Carmelita A. Vargas', 'Unit 8B, The Beacon Makati, Chino Roces Avenue, Makati City', 'W', '1949-12-03', 74, 'F', 'Filipino', 'Born Again', 'Post-graduate', 'Attorney', 50000, 'Member', 'None', 18000, 35000, 17000),
('Elias T. Salvador', '567 Mahogany Road, Barangay Lumbangan, Calamba City, Laguna', 'S', '1976-03-27', 48, 'M', 'Filipino', 'Catholic', 'College', 'Muralist', 20000, 'Non-Member', 'Journalist', 11000, 14000, 3000),
('Seth A. Ocampo', '789 Bonifacio Drive, Barangay Mabuhay, General Santos City', 'M', '1958-08-19', 65, 'M', 'Filipino', 'Iglesia ni Cristo', 'High School', 'Small business owner', 20000, 'Non-Member', 'Cashier', 7000, 14000, 7000),
('Kiara L. Cruz', 'Unit 20C, One Oasis, Ortigas Extension, Pasig City', 'S', '1990-01-05', 34, 'F', 'Filipino', 'Catholic', 'Vocational', 'Plumber', 8000, 'Member', 'Construction Worker', 7000, 6000, 1000),
('Dhanya D. Aquino', '234 Narra Street, Barangay Maginhawa, Sariaya, Quezon', 'S', '1939-10-09', 84, 'F', 'Filipino', 'Catholic', 'College', 'Retired', 10000, 'Non-Member', 'None', 7000, 8000, 1000),
('James L. Torres', 'Unit 16D, Avida Towers, Alabang, Muntinlupa City', 'SE', '1950-07-30', 73, 'M', 'Filipino', 'Catholic', 'Post-graduate', 'Psychologist', 60000, 'Member', 'None', 18000, 40000, 22000),
('Jules A. Villanueva', 'Unit 10A, SMDC Light Residences, EDSA, Mandaluyong City', 'SE', '1939-10-09', 84, 'F', 'Filipino', 'Catholic', 'High School', 'Janitor', 7000, 'Non-Member', 'None', 5000, 4000, 1000),
('Hani P. Germinal', 'Blk 19 Lot 21, Sameera Subd., Angeles, Pampanga', 'SE', '1989-02-12', 35, 'F', 'Filipino', 'Catholic', 'College', 'Teacher', 32000, 'Non-member', 'Small business', 12000, 16000, 4000),
('Riley Y. Dy', '241 St., University Hills, General Trias, Cavite', 'S', '2003-12-01', 20, 'F', 'Filipino', 'Born Again', 'College', 'Psychiatrist', 40000, 'Member', 'None', 20000, 25000, 5000),
('Brian Z. Milan', '5678 Rizal Avenue, Barangay Santa Cruz, Quezon City, Metro Manila', 'M', '1981-07-03', 42, 'M', 'Filipino', 'Catholic', 'College', 'Incident Controller', 75000, 'Dependent', 'Freelancer', 31000, 38000, 7000),
('Dustin F. Tan', '9012 Lopez St., Barangay Mabolo, Cebu City, Cebu', 'W', '1994-08-12', 29, 'M', 'Filipino', 'Catholic', 'High School', 'Call Center Agent', 19000, 'Non-member', 'Business', 10000, 15000, 5000),
('Rette D. Mirol', 'Blk 1, Lot 8, 9102 Corrales Ave., Barangay 24, Bamban, Tarlac', 'S', '1993-08-08', 28, 'M', 'Filipino', 'Catholic', 'Vocational', 'Technician', 27000, 'Non-member', 'None', 7000, 11000, 4000),
('Cherry Ann B. Cailing', 'Block 7, Lot 9, 7890 Magsaysay Avenue, Barangay Oro Site, Legazpi City, Albay', 'M', '1976-01-04', 48, 'F', 'Filipino', 'Catholic', 'College', 'Midwife', 25000, 'Member', 'None', 8000, 12000, 4000),
('Kester Z. Cruz', 'Blk 6 Lot 2, Sta. Ana II, Indang, Cavite', 'S', '2001-05-09', 23, 'M', 'Filipino', 'Iglesia ni Cristo', 'College', 'Nurse', 31000, 'Non-member', 'None', 13000, 19000, 6000),
('Rynn B. Reyes', '6251 Rita St., Summerwind I, Imus, Cavite', 'M', '2000-01-17', 24, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Real Estate Agent', 81000, 'Member', 'Residential Property', 21000, 32000, 11000),
('Diana A. Tala', 'Blk 9 Lot 20, Brgy 630, Sta Mesa, Manila', 'S', '1985-10-29', 38, 'F', 'Filipino', 'Catholic', 'High School', 'Welder', 24000, 'Dependent', 'None', 10000, 14000, 4000),
('Cecille H. Termo', '5678 Jalandoni Street, Barangay Lapuz Norte, Iloilo City, Iloilo', 'SE', '1992-09-09', 31, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Professor', 38000, 'Member', 'Investment', 9000, 17000, 8000);



# Insert data into the tables

INSERT INTO Household_Details (
    Household_ID, Applicant_ID, Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome
) VALUES
(1, 1, 'Alexander Montillano', 32, 'M', 'Brother', 'College', 'Partimer', 15900),
(2, 2, 'Olivia Castillo', 31, 'M', 'Daughter', 'Post-Gradute', 'Carpenter', 5000),
(3, 3, 'Liam Reyes', 63, 'W', 'Father', 'None', 'Truck Driver', 11000),
(4, 4, 'Amari Rivera', 28, 'M', 'Spouse', 'College', 'Journalist', 30000),
(5, 5, 'Eman Ayala', 25, 'S', 'Cousin', 'College', 'Writer', 50000),
(6, 6, 'Andrew Rosa', 15, 'S', 'Nephew', 'College', 'Student', 100000),
(7, 7, 'Lei Reyes', 60, 'M', 'Father', 'Post-Graduate', 'Retired', 17000),
(8, 8, 'Kevin Flores', 45, 'S', 'Uncle', 'College', 'Radiologist', 40000),
(9, 9, 'John Dela Cruz', 40, 'SE', 'Brother', 'Vocational', 'Electrician', 10000),
(10, 10, 'Jun Mendoza', 32, 'SE', 'Brother', 'College', 'Accountant', 80000),
(11, 11, 'Akeela S. Fajardo', 30, 'M', 'Mother', 'College', 'Service Desk', 20000),
(12, 11, 'Leshan S. Fajardo', 35, 'M', 'Father', 'College', 'Barista', 18000),
(13, 12, 'Larry Z. Santos', 32, 'M', 'Spouse', 'Vocational', 'Electrician', 22000),
(14, 13, 'Kira O. Buenaventura', 26, 'S', 'Sister', 'College', 'Nurse', 25000),
(15, 14, 'Marie T. Trinidad', 59, 'W', 'Mother', 'College', 'Teacher', 30000),
(16, 15, 'Apple H. Bayani', 32, 'M', 'Sister', 'College', 'Accountant', 34000),
(17, 16, 'Alex F. Alcalde', 61, 'W', 'Father', 'Vocational', 'Plumber', 12000),
(18, 17, 'Dale A. Leviste', 21, 'S', 'Brother', 'College', 'Carpenter', 19000),
(19, 17, 'Rina A. Leviste', 62, 'W', 'Mother', 'None', 'Teacher', 35000),
(20, 17, 'Renn A. Leviste', 23, 'S', 'Sister', 'College', 'Pharmacist', 22000),
(21, 21, 'Julius C. Dela Cruz', 29, 'M', 'Spouse', 'College', 'Game Developer', 50000),
(22, 22, 'Val L. Gutierrez', 36, 'S', 'Sister', 'College', 'Songwriter/Producer', 60000),
(23, 23, 'Daenerys T. Rosario', 65, 'W', 'Mother', 'College', 'Flight Attendant', 24000),
(24, 24, 'Yolanda A. Vargas', 45, 'S', 'Sister', 'Vocational', 'Seamstress', 13000),
(25, 25, 'Eufemio T. Salvador', 80, 'M', 'Father', 'College', 'Retired', 9000),
(26, 26, 'Elijah A. Ocampo', 23, 'S', 'Brother', 'College', 'Customer Service Agent', 20000),
(27, 27, 'Amy L. Cruz', 40, 'M', 'Cousin', 'College', 'Reporter', 35000),
(28, 28, 'Sarah D. Aquino', 70, 'W', 'Sister', 'Vocational', 'Baker', 25000),
(29, 29, 'Hermione L. Torres', 36, 'S', 'Daughter', 'Post-Graduate', 'Pediatrician', 40000),
(30, 30, 'Tanasha A. Villanueva', 25, 'S', 'Daughter', 'Vocational', 'Seamstress', 18000),
(31, 31, 'Hera P. Germinal', 63, 'W', 'Mother', 'High School', 'Masseuse', 15000),
(32, 32, 'Joy Y. Dy', 24, 'M', 'Sister', 'College', 'Marketing Associate', 26000),
(33, 33, 'Belle Z. Milan', 41, 'M', 'Spouse', 'College', 'Senior Programmer', 78000),
(34, 34, 'Belen Z. Milan', 23, 'S', 'Daughter', 'College', 'Assistant Accountant', 23000),
(35, 36, 'Apple B. Cailing', 42, 'SE', 'Sister', 'Post-graduate', 'Professor', 35000),
(36, 36, 'Rosendo B. Cailing', 76, 'M', 'Father', 'Elementary', 'Carpenter', 15000),
(37, 37, 'Lester Z. Cruz', 35, 'S', 'Brother', 'College', 'Seaman', 43000),
(38, 38, 'Miguel B. Reyes', 26, 'S', 'Spouse', 'Vocational', 'Mechanic', 22000),
(39, 39, 'Rianna A. Tala', 25, 'S', 'Sister', 'College', 'Event Coordinator', 26000),
(40, 40, 'Daryel H. Termo', 33, 'M', 'Cousin', 'High School', 'Cook', 22000);


# Insert data into the tables
INSERT INTO Reference (Reference_No, Applicant_ID, Date, Applicant_Status)
VALUES 
('XY0001', 1, '2024-04-23', 'OLD APPLICANT'),
('XY0002', 2, '2024-04-25', 'NEW APPLICANT'),
('XY0003', 3, '2024-04-28', 'OLD APPLICANT'),
('XY0004', 4, '2024-05-01', 'NEW APPLICANT'),
('XY0005', 5, '2024-05-02', 'NEW APPLICANT'),
('XY0006', 6, '2024-05-03', 'OLD APPLICANT'),
('XY0007', 7, '2024-05-04', 'OLD APPLICANT'),
('XY0008', 8, '2024-05-08', 'OLD APPLICANT'),
('XY0009', 9, '2024-05-10', 'OLD APPLICANT'),
('XY0010', 10, '2024-05-11', 'NEW APPLICANT'),
('XY0011', 11, '2024-05-13', 'OLD APPLICANT'),
('XY0012', 12, '2024-05-15', 'OLD APPLICANT'),
('XY0013', 13, '2024-05-17', 'NEW APPLICANT'),
('XY0014', 14, '2024-05-19', 'OLD APPLICANT'),
('XY0015', 15, '2024-05-25', 'NEW APPLICANT'),
('XY0016', 16, '2024-05-29', 'NEW APPLICANT'),
('XY0017', 17, '2024-05-30', 'NEW APPLICANT'),
('XY0018', 18, '2024-06-01', 'OLD APPLICANT'),
('XY0019', 19, '2024-06-11', 'OLD APPLICANT'),
('XY0020', 20, '2024-06-19', 'NEW APPLICANT'),
('XY0021', 21, '2020-07-15', 'OLD APPLICANT'),
('XY0022', 22, '2024-07-14', 'NEW APPLICANT'),
('XY0023', 23, '2021-07-20', 'OLD APPLICANT'),
('XY0024', 24, '2021-06-30', 'OLD APPLICANT'),
('XY0025', 25, '2023-09-20', 'NEW APPLICANT'),
('XY0026', 26, '2020-03-20', 'OLD APPLICANT'),
('XY0027', 27, '2021-04-01', 'OLD APPLICANT'),
('XY0028', 28, '2024-06-30', 'NEW APPLICANT'),
('XY0029', 29, '2024-07-01', 'NEW APPLICANT'),
('XY0030', 30, '2020-10-09', 'OLD APPLICANT'),
('XY0031', 31, '2020-03-08', 'OLD APPLICANT'),
('XY0032', 32, '2022-03-27', 'OLD APPLICANT'),
('XY0033', 33, '2023-09-18', 'OLD APPLICANT'),
('XY0034', 34, '2024-04-15', 'NEW APPLICANT'),
('XY0035', 35, '2021-10-28', 'OLD APPLICANT'),
('XY0036', 36, '2019-07-29', 'NEW APPLICANT'),
('XY0037', 37, '2021-05-21', 'OLD APPLICANT'),
('XY0038', 38, '2023-08-12', 'NEW APPLICANT'),
('XY0039', 39, '2024-08-01', 'NEW APPLICANT'),
('XY0040', 40, '2021-07-05', 'OLD APPLICANT');

# Insert data into the tables

INSERT INTO admin(Username,_Password)
VALUES
('Marl','admin'),
('Alwyn','admin'),
('Isha','admin'),
('Lucky','admin');




-- Final Query -- 


use PSCODATABASE;
SELECT * FROM PSCODATABASE.applicant_details;
SELECT * FROM PSCODATABASE.household_details; 
SELECT * FROM PSCODATABASE.reference;
SELECT * FROM PSCODATABASE.user;
SELECT * FROM PSCODATABASE.admin;



SELECT * FROM PSCODATABASE.applicant_details;
INSERT INTO Applicant_Details (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES
('Rhys S. Montillano', '130 Manila East Rd. Baytown, Angono, Rizal', 'S', '1999-04-12', 25, 'F', 'Filipino', 'Catholic', 'College', 'Finance Clerk', 100000, 'Member', 'Marketing', 5000, 7000, 2000),
('Mary Z. Castillo', 'A. Mabini Campus, Sta. Mesa, Manila', 'W', '1992-03-25', 52, 'F', 'Filipino', 'Born Again', 'Post-graduate', 'Psychologist', 100000, 'Dependent', 'Teach online courses', 11000, 13000, 2000),
('Shashi M. Reyes', '2219 Recto Ave, Sampaloc, Manila', 'SE', '1996-03-25', 28, 'M', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Electrician', 100000, 'Non-Member', 'Pension, Investment', 7500, 8000, 500),
('Emery S. Rivera', '918 Arnaiz Ave., Makati, Manila', 'M', '1998-04-09', 26, 'M', 'Filipino', 'Catholic', 'College', 'Event Planner', 30000, 'Member', 'Theater Actor', 10000, 20000, 10000),
('Yronica A. Ayala', '1444 Metrica Street, Sampaloc, Manila', 'S', '2000-06-30', 24, 'F', 'Filipino', 'Catholic', 'College', 'Vlogger', 50000, 'Non-Member', 'Makeup Artist', 20000, 30000, 10000),
('Dante F. Rosa', '179 M. Ponce Street, Bagong Bario, Caloocan City, Manila', 'S', '1995-06-25', 28, 'M', 'Filipino', 'Catholic', 'Vocational', 'Seaman', 100000, 'Non-Member', 'None', 15000, 80000, 65000),
('Nathan E. Reyes', '7 Blk 1a-4 Road 18 Phase 5 Cogeo Village, Antipolo, Rizal', 'M', '1995-04-22', 29, 'M', 'Filipino', 'Born Again', 'College', 'Security Guard', 17000, 'Member', 'Part-time barista', 8000, 14000, 6000),
('Arlo T. Flores', '1358 Concepcion St, Santa Cruz, Manila', 'S', '1998-08-02', 25, 'M', 'Filipino', 'Catholic', 'College', 'Nurse', 40000, 'Non-Member', 'Small business owner', 13000, 20000, 7000),
('Juan Dela Cruz', '143, Masbate Street, South City Homes, Biñan, Laguna', 'SE', '1992-09-20', 32, 'M', 'Filipino', 'Iglesia ni Cristo', 'High School', 'Sales Clerk', 10000, 'Member', 'Janitor', 7000, 75000, 68000),
('Evelyn M. Mendoza', 'EDSA Extension, Mall of Asia Complex, Pasay, Manila', 'S', '1994-03-29', 30, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Human Resources Manager', 80000, 'Non-Member', 'Graphic Designing', 35000, 60000, 25000),
('Achilles S. Fajardo', 'Blk 5 Lot 19 Florida St. Summer Heights, Bacoor, Cavite', 'S', '2000-07-07', 23, 'M', 'Filipino', 'Catholic', 'College', 'Accountant', 70000, 'Member', 'Investment', 40000, 70000, 30000),
('Leslie Z. Santos', '6451 Rizal Ave, Mabalacat, Pampamga', 'M', '1994-01-17', 30, 'F', 'Filipino', 'Born Again', 'High School', 'Teacher', 30000, 'Non-Member', 'Business', 20000, 14000, 6000),
('Marian O. Buenaventura', '1124 Perez Street, Sta. Mesa, Manila', 'M', '1997-08-12', 26, 'F', 'Filipino', 'Catholic', 'Post-graduate', 'Call Center Agent', 20000, 'Member', 'None', 8000, 5000, 3000),
('Aurora T. Trinidad', '8346 Dr A Santos Avenue, Paranaque City', 'SE', '1999-08-29', 24, 'F', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Nurse', 28000, 'Member', 'Pension', 15000, 9000, 6000),
('Yula H. Bayani', 'Smith Bldg. 2294, Pasong Kawayan II, Dau, Pampanga', 'W', '1962-02-01', 62, 'F', 'Filipino', 'Catholic', 'College', 'IT Support Specialist', 31000, 'Dependent', 'Freelancing', 17000, 11000, 6000),
('Ruel F. Alcalde', 'B9 L2, Cooper St., Lancaster City, General Trias Cavite', 'S', '1999-10-30', 24, 'M', 'Filipino', 'Catholic', 'High School', 'Sales Manager', 45000, 'Non-Member', 'Small business owner', 23000, 18000, 5000),
('Luke A. Leviste', '713 P Paterno Street, Makati City', 'S', '1989-11-27', 34, 'M', 'Filipino', 'Born Again', 'College', 'Electrician', 18000, 'Member', 'None', 10000, 5000, 5000),
('Zyrus M. De Leon', '484 Sto. Cristo Street, St. Anthony Village, Carmona, Cavite', 'S', '1993-04-13', 31, 'M', 'Filipino', 'Born Again', 'High School', 'Teaching Assistant', 16500, 'Non-Member', 'None', 12000, 9000, 3000),
('Arianne B. Cruz', '8 Molave St. Cityhomes, Tanay, Rizal', 'M', '1992-05-26', 32, 'F', 'Filipino', 'Iglesia ni Cristo', 'Vocational', 'Financial Manager', 48000, 'Dependent', 'Residential Property', 17000, 11000, 6000),
('Solenn P. Verde', '108 Panay Avenue 1100, Pasay City', 'M', '1999-09-17', 24, 'F', 'Filipino', 'Catholic', 'College', 'Service Desk', 32000, 'Member', 'Freelance', 11000, 5000, 6000),
('Gabbie M. Dela Cruz', '123 Sampaguita Street, Barangay San Juan, Taytay, Rizal', 'M', '1990-01-05', 34, 'F', 'Filipino', 'Catholic', 'Vocational', 'Web Developer', 60000, 'Non-Member', 'Freelance', 28000, 22000, 8000),
('Jericha L. Gutierrez', 'Unit 14F, Eastwood Parkview, Eastwood City, Bagumbayan, Quezon City', 'S', '1984-06-15', 40, 'F', 'Filipino', 'Catholic', 'Vocational', 'Call Center Agent', 35100, 'Member', 'Social media manager', 15000, 20000, 5000),
('Javier T. Rosario', '456 Mabini Street, Barangay San Isidro, Antipolo City, Rizal', 'M', '1965-09-22', 58, 'M', 'Filipino', 'Catholic', 'College', 'Graphic Designer', 20000, 'Non-Member', 'Moderator', 10000, 15000, 5000),
('Carmelita A. Vargas', 'Unit 8B, The Beacon Makati, Chino Roces Avenue, Makati City', 'W', '1949-12-03', 74, 'F', 'Filipino', 'Born Again', 'Post-graduate', 'Attorney', 50000, 'Member', 'None', 18000, 35000, 17000),
('Elias T. Salvador', '567 Mahogany Road, Barangay Lumbangan, Calamba City, Laguna', 'S', '1976-03-27', 48, 'M', 'Filipino', 'Catholic', 'College', 'Muralist', 20000, 'Non-Member', 'Journalist', 11000, 14000, 3000),
('Seth A. Ocampo', '789 Bonifacio Drive, Barangay Mabuhay, General Santos City', 'M', '1958-08-19', 65, 'M', 'Filipino', 'Iglesia ni Cristo', 'High School', 'Small business owner', 20000, 'Non-Member', 'Cashier', 7000, 14000, 7000),
('Kiara L. Cruz', 'Unit 20C, One Oasis, Ortigas Extension, Pasig City', 'S', '1990-01-05', 34, 'F', 'Filipino', 'Catholic', 'Vocational', 'Plumber', 8000, 'Member', 'Construction Worker', 7000, 6000, 1000),
('Dhanya D. Aquino', '234 Narra Street, Barangay Maginhawa, Sariaya, Quezon', 'S', '1939-10-09', 84, 'F', 'Filipino', 'Catholic', 'College', 'Retired', 10000, 'Non-Member', 'None', 7000, 8000, 1000),
('James L. Torres', 'Unit 16D, Avida Towers, Alabang, Muntinlupa City', 'SE', '1950-07-30', 73, 'M', 'Filipino', 'Catholic', 'Post-graduate', 'Psychologist', 60000, 'Member', 'None', 18000, 40000, 22000),
('Jules A. Villanueva', 'Unit 10A, SMDC Light Residences, EDSA, Mandaluyong City', 'SE', '1939-10-09', 84, 'F', 'Filipino', 'Catholic', 'High School', 'Janitor', 7000, 'Non-Member', 'None', 5000, 4000, 1000),
('Hani P. Germinal', 'Blk 19 Lot 21, Sameera Subd., Angeles, Pampanga', 'SE', '1989-02-12', 35, 'F', 'Filipino', 'Catholic', 'College', 'Teacher', 32000, 'Non-member', 'Small business', 12000, 16000, 4000),
('Riley Y. Dy', '241 St., University Hills, General Trias, Cavite', 'S', '2003-12-01', 20, 'F', 'Filipino', 'Born Again', 'College', 'Psychiatrist', 40000, 'Member', 'None', 20000, 25000, 5000),
('Brian Z. Milan', '5678 Rizal Avenue, Barangay Santa Cruz, Quezon City, Metro Manila', 'M', '1981-07-03', 42, 'M', 'Filipino', 'Catholic', 'College', 'Incident Controller', 75000, 'Dependent', 'Freelancer', 31000, 38000, 7000),
('Dustin F. Tan', '9012 Lopez St., Barangay Mabolo, Cebu City, Cebu', 'W', '1994-08-12', 29, 'M', 'Filipino', 'Catholic', 'High School', 'Call Center Agent', 19000, 'Non-member', 'Business', 10000, 15000, 5000),
('Rette D. Mirol', 'Blk 1, Lot 8, 9102 Corrales Ave., Barangay 24, Bamban, Tarlac', 'S', '1993-08-08', 28, 'M', 'Filipino', 'Catholic', 'Vocational', 'Technician', 27000, 'Non-member', 'None', 7000, 11000, 4000),
('Cherry Ann B. Cailing', 'Block 7, Lot 9, 7890 Magsaysay Avenue, Barangay Oro Site, Legazpi City, Albay', 'M', '1976-01-04', 48, 'F', 'Filipino', 'Catholic', 'College', 'Midwife', 25000, 'Member', 'None', 8000, 12000, 4000),
('Kester Z. Cruz', 'Blk 6 Lot 2, Sta. Ana II, Indang, Cavite', 'S', '2001-05-09', 23, 'M', 'Filipino', 'Iglesia ni Cristo', 'College', 'Nurse', 31000, 'Non-member', 'None', 13000, 19000, 6000),
('Rynn B. Reyes', '6251 Rita St., Summerwind I, Imus, Cavite', 'M', '2000-01-17', 24, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Real Estate Agent', 81000, 'Member', 'Residential Property', 21000, 32000, 11000),
('Diana A. Tala', 'Blk 9 Lot 20, Brgy 630, Sta Mesa, Manila', 'S', '1985-10-29', 38, 'F', 'Filipino', 'Catholic', 'High School', 'Welder', 24000, 'Dependent', 'None', 10000, 14000, 4000),
('Cecille H. Termo', '5678 Jalandoni Street, Barangay Lapuz Norte, Iloilo City, Iloilo', 'SE', '1992-09-09', 31, 'F', 'Filipino', 'Iglesia ni Cristo', 'Post-graduate', 'Professor', 38000, 'Member', 'Investment', 9000, 17000, 8000);

INSERT INTO Household_Details (
    Household_ID, Applicant_ID, Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome
) VALUES
(1, 1, 'Alexander Montillano', 32, 'M', 'Brother', 'College', 'Partimer', 15900),
(2, 2, 'Olivia Castillo', 31, 'M', 'Daughter', 'Post-Gradute', 'Carpenter', 5000),
(3, 3, 'Liam Reyes', 63, 'W', 'Father', 'None', 'Truck Driver', 11000),
(4, 4, 'Amari Rivera', 28, 'M', 'Spouse', 'College', 'Journalist', 30000),
(5, 5, 'Eman Ayala', 25, 'S', 'Cousin', 'College', 'Writer', 50000),
(6, 6, 'Andrew Rosa', 15, 'S', 'Nephew', 'College', 'Student', 100000),
(7, 7, 'Lei Reyes', 60, 'M', 'Father', 'Post-Graduate', 'Retired', 17000),
(8, 8, 'Kevin Flores', 45, 'S', 'Uncle', 'College', 'Radiologist', 40000),
(9, 9, 'John Dela Cruz', 40, 'SE', 'Brother', 'Vocational', 'Electrician', 10000),
(10, 10, 'Jun Mendoza', 32, 'SE', 'Brother', 'College', 'Accountant', 80000),
(11, 11, 'Akeela S. Fajardo', 30, 'M', 'Mother', 'College', 'Service Desk', 20000),
(12, 11, 'Leshan S. Fajardo', 35, 'M', 'Father', 'College', 'Barista', 18000),
(13, 12, 'Larry Z. Santos', 32, 'M', 'Spouse', 'Vocational', 'Electrician', 22000),
(14, 13, 'Kira O. Buenaventura', 26, 'S', 'Sister', 'College', 'Nurse', 25000),
(15, 14, 'Marie T. Trinidad', 59, 'W', 'Mother', 'College', 'Teacher', 30000),
(16, 15, 'Apple H. Bayani', 32, 'M', 'Sister', 'College', 'Accountant', 34000),
(17, 16, 'Alex F. Alcalde', 61, 'W', 'Father', 'Vocational', 'Plumber', 12000),
(18, 17, 'Dale A. Leviste', 21, 'S', 'Brother', 'College', 'Carpenter', 19000),
(19, 17, 'Rina A. Leviste', 62, 'W', 'Mother', 'None', 'Teacher', 35000),
(20, 17, 'Renn A. Leviste', 23, 'S', 'Sister', 'College', 'Pharmacist', 22000),
(21, 21, 'Julius C. Dela Cruz', 29, 'M', 'Spouse', 'College', 'Game Developer', 50000),
(22, 22, 'Val L. Gutierrez', 36, 'S', 'Sister', 'College', 'Songwriter/Producer', 60000),
(23, 23, 'Daenerys T. Rosario', 65, 'W', 'Mother', 'College', 'Flight Attendant', 24000),
(24, 24, 'Yolanda A. Vargas', 45, 'S', 'Sister', 'Vocational', 'Seamstress', 13000),
(25, 25, 'Eufemio T. Salvador', 80, 'M', 'Father', 'College', 'Retired', 9000),
(26, 26, 'Elijah A. Ocampo', 23, 'S', 'Brother', 'College', 'Customer Service Agent', 20000),
(27, 27, 'Amy L. Cruz', 40, 'M', 'Cousin', 'College', 'Reporter', 35000),
(28, 28, 'Sarah D. Aquino', 70, 'W', 'Sister', 'Vocational', 'Baker', 25000),
(29, 29, 'Hermione L. Torres', 36, 'S', 'Daughter', 'Post-Graduate', 'Pediatrician', 40000),
(30, 30, 'Tanasha A. Villanueva', 25, 'S', 'Daughter', 'Vocational', 'Seamstress', 18000),
(31, 31, 'Hera P. Germinal', 63, 'W', 'Mother', 'High School', 'Masseuse', 15000),
(32, 32, 'Joy Y. Dy', 24, 'M', 'Sister', 'College', 'Marketing Associate', 26000),
(33, 33, 'Belle Z. Milan', 41, 'M', 'Spouse', 'College', 'Senior Programmer', 78000),
(34, 34, 'Belen Z. Milan', 23, 'S', 'Daughter', 'College', 'Assistant Accountant', 23000),
(35, 36, 'Apple B. Cailing', 42, 'SE', 'Sister', 'Post-graduate', 'Professor', 35000),
(36, 36, 'Rosendo B. Cailing', 76, 'M', 'Father', 'Elementary', 'Carpenter', 15000),
(37, 37, 'Lester Z. Cruz', 35, 'S', 'Brother', 'College', 'Seaman', 43000),
(38, 38, 'Miguel B. Reyes', 26, 'S', 'Spouse', 'Vocational', 'Mechanic', 22000),
(39, 39, 'Rianna A. Tala', 25, 'S', 'Sister', 'College', 'Event Coordinator', 26000),
(40, 40, 'Daryel H. Termo', 33, 'M', 'Cousin', 'High School', 'Cook', 22000);


INSERT INTO Reference (Reference_No, Applicant_ID, Date, Applicant_Status)
VALUES 
('XY0001', 1, '2024-04-23', 'OLD APPLICANT'),
('XY0002', 2, '2024-04-25', 'NEW APPLICANT'),
('XY0003', 3, '2024-04-28', 'OLD APPLICANT'),
('XY0004', 4, '2024-05-01', 'NEW APPLICANT'),
('XY0005', 5, '2024-05-02', 'NEW APPLICANT'),
('XY0006', 6, '2024-05-03', 'OLD APPLICANT'),
('XY0007', 7, '2024-05-04', 'OLD APPLICANT'),
('XY0008', 8, '2024-05-08', 'OLD APPLICANT'),
('XY0009', 9, '2024-05-10', 'OLD APPLICANT'),
('XY0010', 10, '2024-05-11', 'NEW APPLICANT'),
('XY0011', 11, '2024-05-13', 'OLD APPLICANT'),
('XY0012', 12, '2024-05-15', 'OLD APPLICANT'),
('XY0013', 13, '2024-05-17', 'NEW APPLICANT'),
('XY0014', 14, '2024-05-19', 'OLD APPLICANT'),
('XY0015', 15, '2024-05-25', 'NEW APPLICANT'),
('XY0016', 16, '2024-05-29', 'NEW APPLICANT'),
('XY0017', 17, '2024-05-30', 'NEW APPLICANT'),
('XY0018', 18, '2024-06-01', 'OLD APPLICANT'),
('XY0019', 19, '2024-06-11', 'OLD APPLICANT'),
('XY0020', 20, '2024-06-19', 'NEW APPLICANT'),
('XY0021', 21, '2020-07-15', 'OLD APPLICANT'),
('XY0022', 22, '2024-07-14', 'NEW APPLICANT'),
('XY0023', 23, '2021-07-20', 'OLD APPLICANT'),
('XY0024', 24, '2021-06-30', 'OLD APPLICANT'),
('XY0025', 25, '2023-09-20', 'NEW APPLICANT'),
('XY0026', 26, '2020-03-20', 'OLD APPLICANT'),
('XY0027', 27, '2021-04-01', 'OLD APPLICANT'),
('XY0028', 28, '2024-06-30', 'NEW APPLICANT'),
('XY0029', 29, '2024-07-01', 'NEW APPLICANT'),
('XY0030', 30, '2020-10-09', 'OLD APPLICANT'),
('XY0031', 31, '2020-03-08', 'OLD APPLICANT'),
('XY0032', 32, '2022-03-27', 'OLD APPLICANT'),
('XY0033', 33, '2023-09-18', 'OLD APPLICANT'),
('XY0034', 34, '2024-04-15', 'NEW APPLICANT'),
('XY0035', 35, '2021-10-28', 'OLD APPLICANT'),
('XY0036', 36, '2019-07-29', 'NEW APPLICANT'),
('XY0037', 37, '2021-05-21', 'OLD APPLICANT'),
('XY0038', 38, '2023-08-12', 'NEW APPLICANT'),
('XY0039', 39, '2024-08-01', 'NEW APPLICANT'),
('XY0040', 40, '2021-07-05', 'OLD APPLICANT');



INSERT INTO admin(Username,_Password)
VALUES
('Marl','admin'),
('Alwyn','admin'),
('Isha','admin'),
('Lucky','admin');







