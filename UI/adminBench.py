import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry
import mysql.connector
from mysql_config import dbConfig
from resources.FileTracker.tracker import resource_path

class AdminBench(tk.Toplevel):
        

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Admin Bench")
        self.geometry("1920x700")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        
        # Create the upper frame
        self.UpperFrame = tk.Frame(self)
        self.UpperFrame.pack(side="top", fill=tk.BOTH, expand=True)
        
        # Create a canvas in the upper frame
        self.canvas = tk.Canvas(self.UpperFrame, bg="#FFFFFF")
        self.canvas.pack(side="top", fill=tk.BOTH, expand=True)


        self.image_1 = PhotoImage(file=resource_path("resources/adminbench/image_1.png"))
        self.canvas.create_image(960.0, 30, image = self.image_1)

        self.button_image_1 = PhotoImage(file=resource_path("resources/adminbench/button_1.png"))
        self.button_image_2 = PhotoImage(file=resource_path("resources/adminbench/button_2.png"))
        self.button_image_3 = PhotoImage(file=resource_path("resources/adminbench/button_3.png"))


  
        # Create a button to fetch data
        self.FetchApplicant = tk.Button(self.canvas,image =self.button_image_1,borderwidth=0,highlightthickness=0, command=self.FetchApplicantData)
        self.FetchApplicant.place(x=120.0, y=300, anchor="center")


        # Create the lower frame
        self.LowerFrame = tk.Frame(self)
        self.LowerFrame.pack(side="bottom", fill=tk.BOTH, expand=True)
        
        # Create a treeview to display the data
        self.columns = (
            "Applicant_ID", "Full_Name", "Address", "Civil_Status", "Birth_Date", "Age",
            "Sex", "Nationality", "Religion", "Membership", "Highest_Educ_Attainment",
            "Occupation", "Monthly_Income", "OtherSourceOfIncome", "Monthly_Expenditures",
            "GrossMonthlyIncome", "NetMonthlyIncome"
        )
        self.tree = ttk.Treeview(self.LowerFrame, columns=self.columns, show='headings')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#D97F76", foreground="#000000", font=("Helvetica", 10))
        self.style.configure("Treeview", background="#FFFFFF", foreground="#000000", fieldbackground="yellow")

        

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)
        

        self.VScroll = ttk.Scrollbar(self.LowerFrame, orient=tk.VERTICAL, command=self.tree.yview)
        self.VScroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.VScroll.set)
        

        self.HScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.HScroll.set)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        

    def FetchApplicantData(self):
        # Connect to the MySQL database
        self.con = mysql.connector.connect(**dbConfig)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM Applicant_Details")
        rows = self.cursor.fetchall()

        # Clear the existing data in the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new data into the treeview
        for row in rows:
            self.tree.insert('', 'end', values=row)

        # Close the database connection
        self.cursor.close()
        self.con.close()


    def on_close(self):
        self.destroy()
        self.master.destroy()  



