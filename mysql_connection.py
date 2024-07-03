from mysql_config import dbConfig
import mysql.connector as mysql
from tkinter import messagebox
from mysql.connector import Error


class DatabaseConnection:
  def __init__(self): # Constructor
    self.con = mysql.connect(**dbConfig) # Connect to the database using the dbConfig dictionary from mysql_config.py
    self.cursor = self.con.cursor() # Create a cursor object
    print("You have connected to the  database") # Print a message to indicate that the connection was successful
    print(self.con) # Print the connection object

  def __del__(self):  # Destructor
    self.con.close() # Close the connection
    print("You have disconnected to the  database") # Print a message to indicate that the connection was closed

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------GET LAST REFERENCE ID----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def get_last_reference_id(self): 
    # SQL query to get the last inserted reference ID directly
    last_reference_id_query =  "SELECT reference_No FROM reference ORDER BY reference_No DESC LIMIT 1"
    self.cursor.execute(last_reference_id_query) 
    result = self.cursor.fetchone() 
    if result is None:
        new_reference_id = "XY0001"
    else:
        last_reference_id = result[0]
        numeric_part = int(last_reference_id[2:]) 
        new_numeric_part = numeric_part + 1 
        new_reference_id = f"XY{new_numeric_part:04d}" 
    
    return new_reference_id

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------GET LAST APPLICANT ID----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------



  def get_last_applicant_id(self): # Get the last applicant ID
    last_applicant_id_query = "SELECT LAST_INSERT_ID()" # SQL query to get the last inserted ID
    self.cursor.execute(last_applicant_id_query) # Execute the query
    last_applicant_id = self.cursor.fetchone()# Fetch the result
    return last_applicant_id[0]# Return the last applicant ID



#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------UPDATE APPLICANT DETAILS-------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def UpdateApplicantDetails(self, Applicant_ID, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
    query = """
        UPDATE Applicant_Details
        SET Full_Name=%s, Address=%s, Civil_Status=%s, Birth_Date=%s, Age=%s, Sex=%s, Nationality=%s, Religion=%s,
            Highest_Educ_Attainment=%s, Occupation=%s, Monthly_Income=%s, Membership=%s, OtherSourceOfIncome=%s,
            Monthly_Expenditures=%s, GrossMonthlyIncome=%s, NetMonthlyIncome=%s
        WHERE Applicant_ID=%s
    """
    data = (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome, Applicant_ID)
    
    self.cursor.execute(query, data)
    self.con.commit()

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------UPDATE HouseHold DETAILS-------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def UpdateApplicantDetails(self, Applicant_ID, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
    query = """
        UPDATE Applicant_Details
        SET Full_Name=%s, Address=%s, Civil_Status=%s, Birth_Date=%s, Age=%s, Sex=%s, Nationality=%s, Religion=%s,
            Highest_Educ_Attainment=%s, Occupation=%s, Monthly_Income=%s, Membership=%s, OtherSourceOfIncome=%s,
            Monthly_Expenditures=%s, GrossMonthlyIncome=%s, NetMonthlyIncome=%s
        WHERE Applicant_ID=%s
    """
    data = (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome, Applicant_ID)
    
    self.cursor.execute(query, data)
    self.con.commit()


    
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------UPDATE REFERENCE APPLICANT DETAILS---------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def UpdateRefAppHouseDetails(self, Reference_No, Applicant_ID, Date, Applicant_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome,Household_Id,Hhold_Fam_Name,Hhold_Fam_Age,Hhold_Fam_CivilStatus,Hhold_Fam_RSWithPatient,Hhold_Fam_HighestEducAttain,
Hhold_Fam_Occupation,Hhold_Fam_MonthlyIncome):
      # Update the reference table
      query_reference = """
          UPDATE reference
          SET Applicant_ID=%s, Date=%s, Applicant_Status=%s
          WHERE Reference_No=%s
      """
      data_reference = (Applicant_ID, Date, Applicant_Status, Reference_No)
      
      self.cursor.execute(query_reference, data_reference)

      # Update the applicant_details table
      query_applicant_details = """
          UPDATE applicant_details
          SET Full_Name=%s, Address=%s, Civil_Status=%s, Birth_Date=%s, Age=%s, Sex=%s, Nationality=%s, Religion=%s,
              Highest_Educ_Attainment=%s, Occupation=%s, Monthly_Income=%s, Membership=%s, OtherSourceOfIncome=%s,
              Monthly_Expenditures=%s, GrossMonthlyIncome=%s, NetMonthlyIncome=%s
          WHERE Applicant_ID=%s
      """
      data_applicant_details = (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome, Applicant_ID)
      self.cursor.execute(query_applicant_details, data_applicant_details)


      query_household_details = """
          UPDATE household_details
          SET Hhold_Fam_Name=%s, Hhold_Fam_Age=%s, Hhold_Fam_CivilStatus=%s, Hhold_Fam_RSWithPatient=%s, Hhold_Fam_HighestEducAttain=%s, Hhold_Fam_Occupation=%s, Hhold_Fam_MonthlyIncome=%s
          WHERE Household_Id=%s
      """
      data_household_details = (Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome, Household_Id) 
      self.cursor.execute(query_household_details, data_household_details) 

      

      self.con.commit()
      messagebox.showinfo(title="Edit Success",message="Edit Success")# Display a message box to indicate that the record was added successfully

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------DELETE APPLICANT DETAILS-------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def DeleteDetails(self, reference_no):
        try:
            delete_household_query = """
            DELETE FROM Household_Details
            WHERE Applicant_ID IN (
                SELECT Applicant_ID FROM Reference WHERE Reference_No = %s
            );
            """
            self.cursor.execute(delete_household_query, (reference_no,))

            # Step 2: Delete the reference record
            delete_reference_query = """
            DELETE FROM Reference
            WHERE Reference_No = %s;
            """
            self.cursor.execute(delete_reference_query, (reference_no,))

            # Step 3: Delete applicant records that are no longer referenced
            delete_applicant_query = """
            DELETE FROM Applicant_Details
            WHERE Applicant_ID NOT IN (
                SELECT Applicant_ID FROM Reference
            );
            """
            self.cursor.execute(delete_applicant_query)

            # Commit the transaction
            self.con.commit()
            messagebox.showinfo(title="PCSCO TABLE",message="Data Deleted")# Display a message box to indicate that the record was added successfully


        except Error as e:
            print(f"Error: {e}")
            if self.con.is_connected():  # Check if the connection is still active
                self.con.rollback()  # Rollback the transaction in case of an error
                print("Transaction rolled back due to error.")


#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------APPLICANT DETAILS--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert_applicant_details(self, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion,Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
    # Insert data into the Applicant_Details table
    query = "INSERT INTO applicant_details (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES (%(Full_Name)s, %(Address)s, %(Civil_Status)s, %(Birth_Date)s, %(Age)s, %(Sex)s, %(Nationality)s, %(Religion)s, %(Highest_Educ_Attainment)s, %(Occupation)s, %(Monthly_Income)s, %(Membership)s, %(OtherSourceOfIncome)s, %(Monthly_Expenditures)s, %(GrossMonthlyIncome)s, %(NetMonthlyIncome)s)" # SQL query
    # Data to be inserted
    data = {
      "Full_Name": Full_Name,
      "Address": Address,
      "Civil_Status": Civil_Status,
      "Birth_Date": Birth_Date,
      "Age": Age,
      "Sex": Sex,
      "Nationality": Nationality,
      "Religion": Religion,
      "Highest_Educ_Attainment": Highest_Educ_Attainment,
      "Occupation": Occupation,
      "Monthly_Income": Monthly_Income,
      "Membership": Membership,
      "OtherSourceOfIncome": OtherSourceOfIncome,
      "Monthly_Expenditures": Monthly_Expenditures,
      "GrossMonthlyIncome": GrossMonthlyIncome,
      "NetMonthlyIncome": NetMonthlyIncome
    }
    self.cursor.execute(query, data) # Execute the query
    self.con.commit() # Commit the transaction
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")# Display a message box to indicate that the record was added successfully

    





# ---------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------HOUSEHOLD DETAILS--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert_household_details(self,Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome):
    household_query = "INSERT INTO household_details (Applicant_ID, Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome) VALUES (%(Applicant_ID)s, %(Hhold_Fam_Name)s, %(Hhold_Fam_Age)s, %(Hhold_Fam_CivilStatus)s, %(Hhold_Fam_RSWithPatient)s, %(Hhold_Fam_HighestEducAttain)s, %(Hhold_Fam_Occupation)s, %(Hhold_Fam_MonthlyIncome)s)"
    last_applicant_id = self.get_last_applicant_id() # Get the last applicant ID
    household_data = {
      "Applicant_ID": last_applicant_id, # Data to be inserted
      "Hhold_Fam_Name": Hhold_Fam_Name,
      "Hhold_Fam_Age": Hhold_Fam_Age,
      "Hhold_Fam_CivilStatus": Hhold_Fam_CivilStatus,
      "Hhold_Fam_RSWithPatient": Hhold_Fam_RSWithPatient,
      "Hhold_Fam_HighestEducAttain": Hhold_Fam_HighestEducAttain,
      "Hhold_Fam_Occupation": Hhold_Fam_Occupation,
      "Hhold_Fam_MonthlyIncome": Hhold_Fam_MonthlyIncome
    }
    self.cursor.execute(household_query, household_data)
    self.con.commit()
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")




#--------------------------------------------------------------------------------------------------------------------------------------------------------  
#-------------------------------------------------------REFERENCE DETAILS--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
  def insert_reference_details(self, Reference_No, Date, Applicant_Status):
    query = "INSERT INTO Reference(Reference_No, Applicant_ID, Date, Applicant_Status) VALUES (%(Reference_No)s, %(Applicant_ID)s, %(Date)s, %(Applicant_Status)s)"
    last_applicant_id = self.get_last_applicant_id() # Get the last applicant ID
    last_reference_id = self.get_last_reference_id() # Get the last applicant ID
    data = {
      "Reference_No": last_reference_id, # Data to be inserted
      "Applicant_ID": last_applicant_id, 
      "Date": Date,
      "Applicant_Status": Applicant_Status
    }
    self.cursor.execute(query, data)
    self.con.commit()
    messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------FETCH WHOLE DETAILS--------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
  
  def FetchRefApplincatHouseDetails(self):
     self.cursor.execute("SELECT Reference_No,R.Applicant_ID,Date,Applicant_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality,Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome,Household_Id,Hhold_Fam_Name,Hhold_Fam_Age,Hhold_Fam_CivilStatus,Hhold_Fam_RSWithPatient,Hhold_Fam_HighestEducAttain,Hhold_Fam_Occupation,Hhold_Fam_MonthlyIncome FROM reference AS R, applicant_details AS A, household_details as H WHERE R.Applicant_ID = A.Applicant_ID AND A.Applicant_ID = H.Applicant_ID;")
     rows = self.cursor.fetchall()
     return rows
  

  def FetchApplincatDetailsA(self):
    self.cursor.execute("SELECT * FROM Applicant_Details")
    rows = self.cursor.fetchall()          
    return rows  
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------FETCH HOUSEHOLD DETAILS--------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def FetchApplincatDetailsH(self):
    self.cursor.execute("SELECT * FROM Household_Details")
    rows = self.cursor.fetchall()          
    return rows  


#---------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------FETCH REFERENCE DETAILS--------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

  def FetchApplincatDetailsR(self):
    self.cursor.execute("SELECT * FROM Reference")
    rows = self.cursor.fetchall()  
    return rows  



#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------- SEX APPLICANT DETAILS-------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------


  def FetchMaleApplicantDetails(self):
      self.cursor.execute("SELECT Reference_No,R.Applicant_ID,Date,Applicant_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality,Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome,Household_Id,Hhold_Fam_Name,Hhold_Fam_Age,Hhold_Fam_CivilStatus,Hhold_Fam_RSWithPatient,Hhold_Fam_HighestEducAttain,Hhold_Fam_Occupation,Hhold_Fam_MonthlyIncome FROM reference AS R, applicant_details AS A, household_details as H WHERE R.Applicant_ID = A.Applicant_ID AND A.Applicant_ID = H.Applicant_ID AND A.Sex = 'M';")
      rows = self.cursor.fetchall()
      return rows

  def FetchFemaleApplicantDetails(self):
      self.cursor.execute("SELECT Reference_No,R.Applicant_ID,Date,Applicant_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality,Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome,Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome,Household_Id,Hhold_Fam_Name,Hhold_Fam_Age,Hhold_Fam_CivilStatus,Hhold_Fam_RSWithPatient,Hhold_Fam_HighestEducAttain,Hhold_Fam_Occupation,Hhold_Fam_MonthlyIncome FROM reference AS R, applicant_details AS A, household_details as H WHERE R.Applicant_ID = A.Applicant_ID AND A.Applicant_ID = H.Applicant_ID AND A.Sex = 'F';")
      rows = self.cursor.fetchall()
      return rows

  
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------COUNT FEMALE DETAILS-------------------------------------------------------------------------

  def count_female_applicant_details(self):
      query = "SELECT COUNT(*) FROM Applicant_Details WHERE Sex = 'F'"
      self.cursor.execute(query)
      result = self.cursor.fetchone()
      return result[0]
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------COUNT MALE DETAILS------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------

  def count_male_applicant_details(self):
      query = "SELECT COUNT(*) FROM Applicant_Details WHERE Sex = 'M'"
      self.cursor.execute(query)
      result = self.cursor.fetchone()
      return result[0]
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------COUNT APPLICANT DETAILS-------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
  def count_applicant_details(self):
      query = "SELECT COUNT(*) FROM Applicant_Details"
      self.cursor.execute(query)
      result = self.cursor.fetchone()
      return result[0]

