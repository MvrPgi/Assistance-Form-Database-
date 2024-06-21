use practice;

SELECT * FROM practice.applicant_details;
INSERT INTO Applicant_Details (Applicant_ID, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Membership, Highest_Educ_Attainment, Occupation, Monthly_Income, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome)
VALUES 
(1, 'Rhys S. Montillano', '130 Manila East Rd. Baytown, Angono, Rizal', 'S', '1999-04-12', 25, 'F', 'Filipino', 'Catholic', 'Member', 'College', 'Finance Clerk', 100000, 'Marketing', 5000, 7000, 2000),
(2, 'Mary Z. Castillo', 'A. Mabini Campus, Sta. Mesa, Manila', 'W', '1992-03-25', 52, 'F', 'Filipino', 'Born Again', 'Dependent', 'Post-graduate', 'Psychologist', 100000, 'Teach online courses', 11000, 13000, 2000),
(3, 'Shashi M. Reyes', '2219 Recto Ave, Sampaloc, Manila', 'SE', '1996-03-25', 28, 'M', 'Filipino', 'Iglesia ni Cristo', 'Non-Member', 'Vocational', 'Electrician', 100000, 'Pension, Investment', 7500, 8000, 500),
(4, 'Emery S. Rivera', '918 Arnaiz Ave., Makati, Manila', 'M', '1998-04-09', 26, 'M', 'Filipino', 'Catholic', 'Member', 'College', 'Event Planner', 30000, 'Theater Actor', 10000, 20000, 10000),
(5, 'Yronica A. Ayala', '1444 Metrica Street, Sampaloc, Manila', 'S', '2000-06-30', 24, 'F', 'Filipino', 'Catholic', 'Non-Member', 'College', 'Vlogger', 50000, 'Makeup Artist', 20000, 30000, 10000),
(6, 'Dante F. Rosa', '179 M. Ponce Street, Bagong Bario, Caloocan City, Manila', 'S', '1995-06-25', 28, 'M', 'Filipino', 'Catholic', 'Non-Member', 'Vocational', 'Seaman', 100000, 'None', 15000, 80000, 65000),
(7, 'Nathan E. Reyes', '7 Blk 1a-4 Road 18 Phase 5 Cogeo Village, Antipolo, Rizal', 'M', '1995-04-22', 29, 'M', 'Filipino', 'Born Again', 'Member', 'College', 'Security Guard', 17000, 'Part-time barista', 8000, 14000, 6000),
(8, 'Arlo T. Flores', '1358 Concepcion St, Santa Cruz, Manila', 'S', '1998-08-02', 25, 'M', 'Filipino', 'Catholic', 'Non-Member', 'College', 'Nurse', 40000, 'Small business owner', 13000, 20000, 7000),
(9, 'Juan Dela Cruz', '143, Masbate Street, South City Homes, Biñan, Laguna', 'SE', '1992-09-20', 32, 'M', 'Filipino', 'Iglesia ni Cristo', 'Member', 'High School', 'Sales Clerk', 10000, 'Janitor', 7000, 75000, 68000),
(10, 'Evelyn M. Mendoza', 'EDSA Extension, Mall of Asia Complex, Pasay, Manila', 'S', '1994-03-29', 30, 'F', 'Filipino', 'Iglesia ni Cristo', 'Non-Member', 'Post-graduate', 'Human Resources Manager', 80000, 'Graphic Designing', 35000, 60000, 25000),
(11, 'Achilles S. Fajardo', 'Blk 5 Lot 19 Florida St. Summer Heights, Bacoor, Cavite', 'S', '2000-07-07', 23, 'M', 'Filipino', 'Catholic', 'Member', 'College', 'Accountant', 70000, 'Investment', 40000, 70000, 30000),
(12, 'Leslie Z. Santos', '6451 Rizal Ave, Mabalacat, Pampamga', 'M', '1994-01-17', 30, 'F', 'Filipino', 'Born Again', 'Non-Member', 'High School', 'Teacher', 30000, 'Business', 20000, 14000, 6000),
(13, 'Marian O. Buenaventura', '1124 Perez Street, Sta. Mesa, Manila', 'M', '1997-08-12', 26, 'F', 'Filipino', 'Catholic', 'Member', 'Post-graduate', 'Call Center Agent', 20000, 'None', 8000, 5000, 3000),
(14, 'Aurora T. Trinidad', '8346 Dr A Santos Avenue, Paranaque City', 'SE', '1999-08-29', 24, 'F', 'Filipino', 'Iglesia ni Cristo', 'Member', 'Vocational', 'Nurse', 28000, 'Pension', 15000, 9000, 6000),
(15, 'Yula H. Bayani', 'Smith Bldg. 2294, Pasong Kawayan II, Dau, Pampanga', 'W', '1962-02-01', 62, 'F', 'Filipino', 'Catholic', 'Dependent', 'College', 'IT Support Specialist', 31000, 'Freelancing', 17000, 11000, 6000),
(16, 'Ruel F. Alcalde', 'B9 L2, Cooper St., Lancaster City, General Trias Cavite', 'S', '1999-10-30', 24, 'M', 'Filipino', 'Catholic', 'Non-Member', 'High School', 'Sales Manager', 45000, 'Small business owner', 23000, 18000, 5000),
(17, 'Luke A. Leviste', '713 P Paterno Street, Makati City', 'S', '1989-11-27', 34, 'M', 'Filipino', 'Born Again', 'Member', 'College', 'Electrician', 18000, 'None', 10000, 5000, 5000),
(18, 'Zyrus M. De Leon', '484 Sto. Cristo Street, St. Anthony Village, Carmona, Cavite', 'S', '1993-04-13', 31, 'M', 'Filipino', 'Born Again', 'Non-Member', 'High School', 'Teaching Assistant', 16500, 'None', 12000, 9000, 3000),
(19, 'Arianne B. Cruz', '8 Molave St. Cityhomes, Tanay, Rizal', 'M', '1992-05-26', 32, 'F', 'Filipino', 'Iglesia ni Cristo', 'Dependent', 'Vocational', 'Financial Manager', 48000, 'Residential Property', 17000, 11000, 6000),
(20, 'Solenn P. Verde', '108 Panay Avenue 1100, Pasay City', 'M', '1999-09-17', 24, 'F', 'Filipino', 'Catholic', 'Member', 'College', 'Service Desk', 32000, 'Freelance', 11000, 5000, 6000);
