
import mysql.connector as database  

mydb = database.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="practice"  # Connect to the database
)

create_table_sql = """
CREATE TABLE IF NOT EXISTS Reference (
    Reference_No VARCHAR(15) PRIMARY KEY,
    Applicant_ID INT,
    Date DATE,
    Applicant_Status VARCHAR(20),
    FOREIGN KEY (Applicant_ID) REFERENCES Applicant_Details(Applicant_ID)
);
"""

mycursor = mydb.cursor()
mycursor.execute(create_table_sql)
print("Table created successfully")

mydb.close()