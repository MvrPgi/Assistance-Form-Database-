--  Author: Alwyn John M. Mercene


-- Practice Database.sql
-- Create the database if it does not exist and use it
CREATE DATABASE IF NOT EXISTS practice;
USE practice;

-- Drop tables if they already exist to avoid conflicts
DROP TABLE IF EXISTS Household_Details;
DROP TABLE IF EXISTS Reference;
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Applicant_Details;

-- Create Applicant_Details table
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

-- Create Household_Details table with ON DELETE CASCADE
CREATE TABLE IF NOT EXISTS Household_Details (
    Household_ID INT AUTO_INCREMENT PRIMARY KEY,
    Applicant_ID INT NOT NULL,
    Hhold_Fam_Name VARCHAR(50) NOT NULL,
    Hhold_Fam_Age INT NOT NULL CHECK (Hhold_Fam_Age <= 999),
    Hhold_Fam_CivilStatus CHAR(2) NOT NULL CHECK (Hhold_Fam_CivilStatus IN ('S', 'M', 'W', 'SE','C')),
    Hhold_Fam_RSWithPatient VARCHAR(20) NOT NULL,
    Hhold_Fam_HighestEducAttain VARCHAR(25) NOT NULL,
    Hhold_Fam_Occupation VARCHAR(25) NOT NULL,
    Hhold_Fam_MonthlyIncome INT NOT NULL CHECK (Hhold_Fam_MonthlyIncome <= 999999),
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID) ON DELETE CASCADE
);

-- Create Reference table with ON DELETE CASCADE
CREATE TABLE IF NOT EXISTS Reference (
    Reference_No VARCHAR(15) PRIMARY KEY NOT NULL,
    Applicant_ID INT NOT NULL,
    Date DATE NOT NULL,
    Applicant_Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID) ON DELETE CASCADE
);
-- Create Admin table
CREATE TABLE IF NOT EXISTS Admin (
    Username VARCHAR(20) NOT NULL PRIMARY KEY,
    _Password VARCHAR(20) NOT NULL
);

-- Create User table
CREATE TABLE IF NOT EXISTS User (
    FullName VARCHAR(50) NOT NULL,
    Username VARCHAR(20) NOT NULL PRIMARY KEY,
    _Password VARCHAR(20) NOT NULL
    );
    




-- Finalized Database.sql

-- Create the database if it does not exist and use it
CREATE DATABASE IF NOT EXISTS PSCODATABASE;
USE PSCODATABASE;

-- Drop tables if they already exist to avoid conflicts
DROP TABLE IF EXISTS Household_Details;
DROP TABLE IF EXISTS Reference;
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Applicant_Details;

-- Create Applicant_Details table
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

-- Create Household_Details table with ON DELETE CASCADE
CREATE TABLE IF NOT EXISTS Household_Details (
    Household_ID INT AUTO_INCREMENT PRIMARY KEY,
    Applicant_ID INT NOT NULL,
    Hhold_Fam_Name VARCHAR(50) NOT NULL,
    Hhold_Fam_Age INT NOT NULL CHECK (Hhold_Fam_Age <= 999),
    Hhold_Fam_CivilStatus CHAR(2) NOT NULL CHECK (Hhold_Fam_CivilStatus IN ('S', 'M', 'W', 'SE','C')),
    Hhold_Fam_RSWithPatient VARCHAR(20) NOT NULL,
    Hhold_Fam_HighestEducAttain VARCHAR(25) NOT NULL,
    Hhold_Fam_Occupation VARCHAR(25) NOT NULL,
    Hhold_Fam_MonthlyIncome INT NOT NULL CHECK (Hhold_Fam_MonthlyIncome <= 999999),
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID) ON DELETE CASCADE
);

-- Create Reference table with ON DELETE CASCADE
CREATE TABLE IF NOT EXISTS Reference (
    Reference_No VARCHAR(15) PRIMARY KEY NOT NULL,
    Applicant_ID INT NOT NULL,
    Date DATE NOT NULL,
    Applicant_Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID) ON DELETE CASCADE
);
-- Create Admin table
CREATE TABLE IF NOT EXISTS Admin (
    Username VARCHAR(20) NOT NULL PRIMARY KEY,
    _Password VARCHAR(20) NOT NULL
);

-- Create User table
CREATE TABLE IF NOT EXISTS User (
    FullName VARCHAR(50) NOT NULL,
    Username VARCHAR(20) NOT NULL PRIMARY KEY,
    _Password VARCHAR(20) NOT NULL
    );
    
    
