from mysql_config import dbConfig
import mysql.connector as mysql
from tkinter import messagebox
from mysql.connector import Error



class DatabaseConnection:
    def __init__(self): # Constructor
            self.con = None
            self.cursor = None
            self.open_connection()


    def open_connection(self):
            if self.con is None or not self.con.is_connected():# Check if the connection is not open or is closed
                self.con = mysql.connect(**dbConfig)  # Connect to the database using the dbConfig dictionary from mysql_config.py
                self.cursor = self.con.cursor()  # Create a cursor object
                print("You have connected to the database")  # Print a message to indicate that the connection was successful
                # print(self.con)  # Print the connection object

    def close_connection(self):
            if self.con is not None and self.con.is_connected():
                self.con.close()  # Close the connection
                self.cursor.close()
                print("You have disconnected from the database")  # Print a message to indicate that the connection was closed

# -------------------------------------------------------GET LAST REFERENCE ID----------------------------------------------------------------------------


    def get_last_reference_id(self):
            self.open_connection()
            try:
                last_reference_id_query = "SELECT reference_No FROM reference ORDER BY reference_No DESC LIMIT 1"
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
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    # -------------------------------------------------------GET LAST APPLICANT ID----------------------------------------------------------------------------


    
    def get_last_applicant_id(self):
            self.open_connection()
            try:
                last_applicant_id_query = "SELECT LAST_INSERT_ID()"
                self.cursor.execute(last_applicant_id_query)
                last_applicant_id = self.cursor.fetchone()
                return last_applicant_id[0]
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    # -------------------------------------------------------UPDATE REFERENCE TABLE---------------------------------------------------------------------------

    def UpdateReferenceDetails(self, Reference_No, Applicant_ID, Date, Applicant_Status):
            self.open_connection()
            try:
                query = """
                    UPDATE Reference
                    SET Applicant_ID=%s, Date=%s, Applicant_Status=%s
                    WHERE Reference_No=%s
                """
                data = (Applicant_ID, Date, Applicant_Status, Reference_No)
                self.cursor.execute(query, data)
                self.con.commit()
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

    # -------------------------------------------------------UPDATE APPLICANT DETAILS-------------------------------------------------------------------------


    def UpdateApplicantDetails(self, Applicant_ID, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
            self.open_connection()
            try:
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
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()
    def UpdateHouseHoldDetails(self, Household_Id,Applicant_ID, Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome):
            self.open_connection()
            try:
                query = """
                    UPDATE Household_Details
                    SET Applicant_ID =%s,Hhold_Fam_Name=%s, Hhold_Fam_Age=%s, Hhold_Fam_CivilStatus=%s, Hhold_Fam_RSWithPatient=%s, Hhold_Fam_HighestEducAttain=%s, Hhold_Fam_Occupation=%s, Hhold_Fam_MonthlyIncome=%s
                    WHERE Household_Id=%s
                """
                data = (Applicant_ID,Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome, Household_Id)
                self.cursor.execute(query, data)
                self.con.commit()
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

        
    # -------------------------------------------------------UPDATE COMBINED DETAILS---------------------------------------------------------------

    def UpdateRefAppHouseDetails(self, Reference_No, Applicant_ID, Date, Applicant_Status, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome,Household_Id,Hhold_Fam_Name,Hhold_Fam_Age,Hhold_Fam_CivilStatus,Hhold_Fam_RSWithPatient,Hhold_Fam_HighestEducAttain,Hhold_Fam_Occupation,Hhold_Fam_MonthlyIncome):
        self.open_connection()
        try:
                query_reference = """
                    UPDATE reference
                    SET Applicant_ID=%s, Date=%s, Applicant_Status=%s
                    WHERE Reference_No=%s
                """
                data_reference = (Applicant_ID, Date, Applicant_Status, Reference_No)
                self.cursor.execute(query_reference, data_reference)

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
                messagebox.showinfo(title="Edit Success", message="Edit Success")
        except Error as e:
                print(f"Error: {e}")
                messagebox.showerror("Database Query Error", f"An error occurred while updating details: {e}")
        finally:
                self.close_connection()


    # -------------------------------------------------------DELETE APPLICANT DETAILS-------------------------------------------------------------------------

    def delete_applicant_details(self, reference_no):
            self.open_connection()
            try:
                delete_household_query = """
                DELETE FROM Household_Details
                WHERE Applicant_ID IN (
                    SELECT Applicant_ID FROM Reference WHERE Reference_No = %s
                );
                """
                self.cursor.execute(delete_household_query, (reference_no,))

                delete_reference_query = """
                DELETE FROM Reference
                WHERE Reference_No = %s;
                """
                self.cursor.execute(delete_reference_query, (reference_no,))

                delete_applicant_query = """
                DELETE FROM Applicant_Details
                WHERE Applicant_ID NOT IN (
                    SELECT Applicant_ID FROM Reference
                );
                """
                self.cursor.execute(delete_applicant_query)

                self.con.commit()
                print("Records deleted successfully.")
            except Error as e:
                print(f"Error: {e}")
                if self.con.is_connected():
                    self.con.rollback()
                    print("Transaction rolled back due to error.")
                messagebox.showerror("Database Query Error", f"An error occurred while deleting details: {e}")
            finally:
                self.close_connection()
        
    def delete_household_details(self,household_id):
            self.open_connection()
            try:
                delete_household_query = """
                DELETE FROM Household_Details
                WHERE Household_Id = %s;
                """
                self.cursor.execute(delete_household_query, (household_id,))
                self.con.commit()
                print("Records deleted successfully.")
            except Error as e:
                print(f"Error: {e}")
                if self.con.is_connected():
                    self.con.rollback()
                    print("Transaction rolled back due to error.")
                messagebox.showerror("Database Query Error", f"An error occurred while deleting details: {e}")
            finally:
                self.close_connection



    # -------------------------------------------------------APPLICANT DETAILS INSERT--------------------------------------------------------------------------------

    def insert_applicant_details(self, Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome):
        self.open_connection()
        try:
            query = "INSERT INTO applicant_details (Full_Name, Address, Civil_Status, Birth_Date, Age, Sex, Nationality, Religion, Highest_Educ_Attainment, Occupation, Monthly_Income, Membership, OtherSourceOfIncome, Monthly_Expenditures, GrossMonthlyIncome, NetMonthlyIncome) VALUES (%(Full_Name)s, %(Address)s, %(Civil_Status)s, %(Birth_Date)s, %(Age)s, %(Sex)s, %(Nationality)s, %(Religion)s, %(Highest_Educ_Attainment)s, %(Occupation)s, %(Monthly_Income)s, %(Membership)s, %(OtherSourceOfIncome)s, %(Monthly_Expenditures)s, %(GrossMonthlyIncome)s, %(NetMonthlyIncome)s)"
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
            self.cursor.execute(query, data)
            self.con.commit()
            messagebox.showinfo(title="PCSCO TABLE",message=" NEW RECORD ADDED SUCCESSFULLY")
        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()


    #-------------------------------------------------------HOUSEHOLD DETAILS INSERT --------------------------------------------------------------------------------

    def insert_household_details(self,Hhold_Fam_Name, Hhold_Fam_Age, Hhold_Fam_CivilStatus, Hhold_Fam_RSWithPatient, Hhold_Fam_HighestEducAttain, Hhold_Fam_Occupation, Hhold_Fam_MonthlyIncome):

        self.open_connection()
        try:
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
        except Error as e:
                print(f"Error: {e}")
        finally:
                self.close_connection() 





    
    #-------------------------------------------------------REFERENCE DETAILS INSERT --------------------------------------------------------------------------------

    def insert_reference_details(self, Reference_No, Date, Applicant_Status):
        self.open_connection()
        try:
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
        except Error as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

    # -------------------------------------------------------FETCH WHOLE DETAILS--------------------------------------------------------------------------


    def FetchRefApplincatHouseDetails(self):
            self.open_connection()
            try:
                query = """
                    SELECT R.Reference_No, R.Applicant_ID, R.Date, R.Applicant_Status, A.Full_Name, A.Address, A.Civil_Status, A.Birth_Date, A.Age, A.Sex, A.Nationality, A.Religion, A.Highest_Educ_Attainment, A.Occupation, A.Monthly_Income, A.Membership, A.OtherSourceOfIncome, A.Monthly_Expenditures, A.GrossMonthlyIncome, A.NetMonthlyIncome, H.Household_ID, H.Hhold_Fam_Name, H.Hhold_Fam_Age, H.Hhold_Fam_CivilStatus, H.Hhold_Fam_RSWithPatient, H.Hhold_Fam_HighestEducAttain, H.Hhold_Fam_Occupation, H.Hhold_Fam_MonthlyIncome
                    FROM Reference AS R
                    JOIN Applicant_Details AS A ON R.Applicant_ID = A.Applicant_ID
                    LEFT JOIN Household_Details AS H ON A.Applicant_ID = H.Applicant_ID;
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    # -------------------------------------------------------FETCH APPLICANT DETAILS--------------------------------------------------------------------------

    

    def FetchApplincatDetailsA(self):
            self.open_connection()
            try:
                query = "SELECT * FROM Applicant_Details"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

    # -------------------------------------------------------FETCH HOUSEHOLD DETAILS--------------------------------------------------------------------------



    def FetchApplincatDetailsH(self):
            self.open_connection()
            try:
                query = "SELECT * FROM Household_Details"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()



    # -------------------------------------------------------FETCH REFERENCE DETAILS--------------------------------------------------------------------------


    def FetchApplincatDetailsR(self):
            self.open_connection()
            try:
                query = "SELECT * FROM Reference"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    #-------------------------------------------------------- SEX APPLICANT DETAILS-------------------------------------------------------------------------


    def FetchMaleApplicantDetails(self):
            self.open_connection()
            try:
                query = """
                    SELECT R.Reference_No, R.Applicant_ID, R.Date, R.Applicant_Status, A.Full_Name, A.Address, A.Civil_Status, A.Birth_Date, A.Age, A.Sex, A.Nationality, A.Religion, A.Highest_Educ_Attainment, A.Occupation, A.Monthly_Income, A.Membership, A.OtherSourceOfIncome, A.Monthly_Expenditures, A.GrossMonthlyIncome, A.NetMonthlyIncome, H.Household_ID, H.Hhold_Fam_Name, H.Hhold_Fam_Age, H.Hhold_Fam_CivilStatus, H.Hhold_Fam_RSWithPatient, H.Hhold_Fam_HighestEducAttain, H.Hhold_Fam_Occupation, H.Hhold_Fam_MonthlyIncome
                    FROM Reference AS R
                    JOIN Applicant_Details AS A ON R.Applicant_ID = A.Applicant_ID
                    LEFT JOIN Household_Details AS H ON A.Applicant_ID = H.Applicant_ID
                    WHERE A.Sex = 'M';
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

    def FetchFemaleApplicantDetails(self):
            self.open_connection()
            try:
                query = """
                    SELECT R.Reference_No, R.Applicant_ID, R.Date, R.Applicant_Status, A.Full_Name, A.Address, A.Civil_Status, A.Birth_Date, A.Age, A.Sex, A.Nationality, A.Religion, A.Highest_Educ_Attainment, A.Occupation, A.Monthly_Income, A.Membership, A.OtherSourceOfIncome, A.Monthly_Expenditures, A.GrossMonthlyIncome, A.NetMonthlyIncome, H.Household_ID, H.Hhold_Fam_Name, H.Hhold_Fam_Age, H.Hhold_Fam_CivilStatus, H.Hhold_Fam_RSWithPatient, H.Hhold_Fam_HighestEducAttain, H.Hhold_Fam_Occupation, H.Hhold_Fam_MonthlyIncome
                    FROM Reference AS R
                    JOIN Applicant_Details AS A ON R.Applicant_ID = A.Applicant_ID
                    LEFT JOIN Household_Details AS H ON A.Applicant_ID = H.Applicant_ID
                    WHERE A.Sex = 'F';
                """
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

    

    #--------------------------------------------------------COUNT FEMALE APPLICANTS-------------------------------------------------------------------------


    def count_female_applicant_details(self):
            self.open_connection()
            try:
                query = "SELECT COUNT(*) FROM Applicant_Details WHERE Sex = 'F'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()



    #--------------------------------------------------------COUNT MALE APPLICANTS------------------------------------------------------------------------------



    def count_male_applicant_details(self):
            self.open_connection()
            try:
                query = "SELECT COUNT(*) FROM Applicant_Details WHERE Sex = 'M'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()



    #--------------------------------------------------------COUNT APPLICANT DETAILS TABLES-------------------------------------------------------------------------

    def count_applicant_details(self):
            self.open_connection()
            try:
                query = "SELECT COUNT(*) FROM Applicant_Details"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    #--------------------------------------------------------AVERAGE MONTHLY INCOME-------------------------------------------------------------------------

    def average_monthly_income(self):
            self.open_connection()
            try:
                query = "SELECT AVG(Monthly_Income) FROM Applicant_Details"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                return result[0]
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()
                

    #---------------------------------------------------------------EASY 1------------------------------------------------------------------------	


    def EasyTask1(self):
            self.open_connection()
            try:
                query = "SELECT applicant_id, full_name, age FROM applicant_details WHERE sex = 'F' AND Highest_Educ_Attainment = 'College';"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                messagebox.showinfo(title="Generate Report",message="Applicants that is female and has highest education attainment of college")
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    #----------------------------------------------------------------EASY 2------------------------------------------------------------------------	

    def EasyTask2(self):
            self.open_connection()
            try:
                query = "SELECT applicant_id, full_name, monthly_income, occupation FROM applicant_details WHERE monthly_income > 60000 ORDER BY monthly_income DESC, occupation;"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                messagebox.showinfo(title="Generate Report",message="Applicants that has monthly income greater than 60000. Sort the monthly income descending and occupation ascending")
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()


    #----------------------------------------------------------------EASY 3------------------------------------------------------------------------


    def EasyTask3(self):
            self.open_connection()
            try:
                query = "SELECT * FROM applicant_details WHERE Age > 30 AND (Civil_Status = 'S' OR Civil_Status = 'M') ORDER BY Full_Name ASC;"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                messagebox.showinfo(title="Generate Report",message="Applicants who are over 30 years old and their civil status is either Single or Married, sorted by their full name")
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()

    #----------------------------------------------------------------Moderate 1------------------------------------------------------------------------
    
    def ModerateTask1(self):
            self.open_connection()
            try:
                query = "SELECT  Highest_Educ_Attainment, SUM(monthly_income) as monthlyIncome FROM applicant_details WHERE membership <> 'Non-Member' GROUP BY Highest_Educ_Attainment HAVING monthlyIncome > 15000;"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                messagebox.showinfo(title="Generate Report",message="Highest education attainment of applicants who are not a non-member and the sum of their monthly income is greater than 15000")
                return rows
            except Error as e:
                print(f"Error: {e}")
            finally:
                self.close_connection()
    #----------------------------------------------------------------Moderate 2------------------------------------------------------------------------

    #----------------------------------------------------------------Moderate 3------------------------------------------------------------------------

    def ModerateTask3(self):
            self.open_connection()
            try:
                query = "SELECT Civil_Status, AVG(Monthly_Income) AS Average_Income FROM applicant_details GROUP BY Civil_Status HAVING AVG(Monthly_Income) > 30000;"
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                messagebox.showinfo(title="Generate Report",message="Highest education attainment of applicants and their average monthly income, sorted by average monthly income descending")
                return rows
            except Error as e:
                print(f"Error: {e}")




