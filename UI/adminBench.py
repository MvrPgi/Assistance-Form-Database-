import tkinter as tk
from tkinter import ttk
import mysql.connector


class AdminBench(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Admin Bench")
        self.geometry("820x500")
        self.configure(bg="#FFFFFF")
        

        # Create a frame for the treeview and scrollbars
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
    
   

        # Create a treeview to display the data
        self.columns = (
            "Applicant_ID", "Full_Name", "Address", "Civil_Status", "Birth_Date", "Age",
            "Sex", "Nationality", "Religion", "Membership", "Highest_Educ_Attainment",
            "Occupation", "Monthly_Income", "OtherSourceOfIncome", "Monthly_Expenditures",
            "GrossMonthlyIncome", "NetMonthlyIncome"
        )

        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define column headings and center the data
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        # Create vertical scrollbar
        self.v_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.v_scrollbar.set)

        # Create horizontal scrollbar
        self.h_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.h_scrollbar.set)

        # Create a button to fetch data
        self.fetch_button = tk.Button(self, text="Fetch Data", command=self.fetch_data)
        self.fetch_button.pack()

    def fetch_data(self):
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',     
            user='root',  
            password='1234', 
            database='practice'  
        )
        cursor = conn.cursor()

        # Fetch data from the Applicant_Details table
        cursor.execute("SELECT * FROM Applicant_Details")
        rows = cursor.fetchall()

        # Clear the existing data in the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new data into the treeview
        for row in rows:
            self.tree.insert('', 'end', values=row)

        # Close the database connection
        cursor.close()
        conn.close()



