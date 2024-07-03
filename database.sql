CREATE DATABASE IF NOT EXISTS practice;
USE practice;
CREATE TABLE IF NOT EXISTS Applicant_Details (
    Applicant_ID INT AUTO_INCREMENT PRIMARY KEY,
    Full_Name VARCHAR(50) NOT NULL,
    Address VARCHAR(85) NOT NULL,
    Civil_Status CHAR(2) NOT NULL CHECK (Civil_Status IN ('S', 'M', 'W', 'SE', 'C', 'O')),
    Birth_Date DATE NOT NULL,
    Age INT NOT NULL CHECK (Age <= 999),
    Sex CHAR(1) NOT NULL CHECK (Sex IN ('F', 'M')),
    Nationality VARCHAR(25) NOT NULL,
    Religion VARCHAR(25) NOT NULL,
    Highest_Educ_Attainment VARCHAR(25) NOT NULL,
    Occupation VARCHAR(30) NOT NULL,
    Monthly_Income INT NOT NULL CHECK (Monthly_Income <= 999999),
    Membership VARCHAR(10) NOT NULL,
    OtherSourceOfIncome VARCHAR(50) NOT NULL,
    Monthly_Expenditures INT NOT NULL CHECK (Monthly_Expenditures <= 999999),
    GrossMonthlyIncome INT NOT NULL CHECK (GrossMonthlyIncome <= 999999),
    NetMonthlyIncome INT NOT NULL CHECK (NetMonthlyIncome <= 999999)
);



CREATE TABLE IF NOT EXISTS Household_Details (
    Household_ID INT AUTO_INCREMENT PRIMARY KEY,
    Applicant_ID INT NOT NULL,
    Hhold_Fam_Name VARCHAR(50) NOT NULL,
    Hhold_Fam_Age INT NOT NULL CHECK (Hhold_Fam_Age <= 999),
    Hhold_Fam_CivilStatus CHAR(2) NOT NULL CHECK (Hhold_Fam_CivilStatus IN ('S', 'M', 'W', 'SE')),
    Hhold_Fam_RSWithPatient VARCHAR(20) NOT NULL,
    Hhold_Fam_HighestEducAttain VARCHAR(25) NOT NULL,
    Hhold_Fam_Occupation VARCHAR(25) NOT NULL,
    Hhold_Fam_MonthlyIncome INT NOT NULL CHECK (Hhold_Fam_MonthlyIncome <= 999999),
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID)
);

CREATE TABLE IF NOT EXISTS Reference (
	Reference_No VARCHAR(15) PRIMARY KEY NOT NULL,
	Applicant_ID INT NOT NULL,
	Date DATE NOT NULL,
	Applicant_Status VARCHAR(20) NOT NULL,
	FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID)
);

CREATE TABLE IF NOT EXISTS Admin (
	Username VARCHAR(20) NOT NULL,
    _Password VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS User (
	FullName VARCHAR(50) NOT NULL,
	Username VARCHAR(20) NOT NULL,
    _Password VARCHAR(20) NOT NULL
);

#mga ID INT muna
#gawa table ng admin and user, laman ng dalawa is username and password