import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="practice"  # Connect to the database
)

create_table_sql = """
CREATE TABLE IF NOT EXISTS Applicant_Details (
    Applicant_ID INT AUTO_INCREMENT PRIMARY KEY,
    Application_Status VARCHAR(255),
    Full_Name VARCHAR(50) NOT NULL,
    Address VARCHAR(85) NOT NULL,
    Civil_Status CHAR(2) NOT NULL,
    Birth_Date DATE NOT NULL,
    Age INT NOT NULL,
    Sex CHAR(1) NOT NULL,
    Nationality VARCHAR(25) NOT NULL,
    Religion VARCHAR(25) NOT NULL,
    Highest_Educ_Attainment VARCHAR(25) NOT NULL,
    Occupation VARCHAR(30) NOT NULL,
    Monthly_Income INT NOT NULL,
    Membership VARCHAR(10) NOT NULL,
    OtherSourceOfIncome VARCHAR(50) NOT NULL,
    Monthly_Expenditures INT NOT NULL,
    GrossMonthlyIncome INT NOT NULL,
    NetMonthlyIncome INT NOT NULL,
    CHECK (Civil_Status IN ('S', 'M', 'W', 'SE')),
    CHECK (Age <= 999),
    CHECK (Sex IN ('F', 'M')),
    CHECK (Monthly_Income <= 999999),
    CHECK (Monthly_Expenditures <= 999999),
    CHECK (GrossMonthlyIncome <= 999999),
    CHECK (NetMonthlyIncome <= 999999)
);
"""

mycursor = mydb.cursor()
mycursor.execute(create_table_sql)
print("Table created successfully")
