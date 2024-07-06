import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry
import mysql.connector
from mysql_config import dbConfig
from mysql_connection import DatabaseConnection
from resources.FileTracker.tracker import resource_path

class ApplicantTable(tk.Toplevel):
        
    def __init__(self, master = None,switch_frame=None):
        super().__init__()
        self.geometry("1910x700")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.database = DatabaseConnection()
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app

        # Create the canvas in the upper frame
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.Header = PhotoImage(file=resource_path("resources/adminbench/header.png"))
        self.canvas.create_image(955.0, 15, image=self.Header)
     


        self.EditBGPic = PhotoImage(file=resource_path("resources/adminbench/UpdateBG.png"))
        self.canvas.create_image(80.0, 90, image=self.EditBGPic)
        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command=lambda:print("ButtonClicked"), borderwidth=0, highlightthickness=0)
        self.updateButton.place(x=80.0, y=90,anchor="center", width=95, height=20)


        self.RefreshBGPic = PhotoImage(file=resource_path("resources/adminbench/updateBG.png"))
        self.canvas.create_image(210.0, 90, image=self.RefreshBGPic)
        self.RefreshButtonImage = PhotoImage(file=resource_path("resources/adminbench/refreshButton.png"))
        self.refreshButton = tk.Button(self.canvas, image=self.RefreshButtonImage, command=self.FetchApplicantData, borderwidth=0, highlightthickness=0)
        self.refreshButton.place(x=210.0, y=92, anchor="center", width=95, height=20)

        self.backButtonImage = PhotoImage(file=resource_path("resources/adminbench/homeButton.png"))
        self.backButton = tk.Button(self.canvas,image=self.backButtonImage, command=self.back_to_admin_homepage,borderwidth=0, highlightthickness=0)
        self.backButton.place(x=25.0, y=25, anchor="center", width=30, height=20)


        self.columns = (
            "Applicant_ID", "Full Name","Address", "Civil Status",  
            "Birth_Date", "Age", "Sex", "Nationality", "Religion", "Highest Educational Attainment", "Occupation", 
            "Monthly_Income", "Membership", "OtherSourceOfIncome", "Monthly_Expenditures", "GrossMonthlyIncome", 
            "NetMonthlyIncome"
        )
        
        # Create the Treeview widget
        self.tree = ttk.Treeview(self.canvas, columns=self.columns, show='headings', height=20)
        self.tree.pack_propagate(False) # Prevent the treeview from resizing with the window
        self.tree.place(x=955.0, y=400, anchor="center", width=1880, height=560)


        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#FFFFF", foreground="#000000", font=("Nokora", 10))
        self.style.configure("Treeview", rowheight=25)


        # Set headings and column widths
        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)            
      

        # Create the horizontal scrollbar
        self.HScroll = ttk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.place(x=955.0, y=115, anchor="center", width=1880)

        # Configure the tree view to use the scrollbar
        self.tree.configure(xscrollcommand=self.HScroll.set)


        # Destroy the window when the close button is clicked
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        self.FetchApplicantData()

    def FetchApplicantData(self):
        rows = self.database.FetchApplincatDetailsA()

        for row in self.tree.get_children():
            self.tree.delete(row)# Clear the existing data in the treeview

        
        # Define alternating colors
        color1 = "#CFCECE"  # Light grey
        color2 = "#FFFFFF"  # Slightly darker grey

        # Insert data with alternating colors
        for index, row in enumerate(rows):
            tag = f"color_{index % 2}"  # Alternating tag
            color = color1 if index % 2 == 0 else color2
            self.tree.tag_configure(tag, background=color)
            self.tree.insert('', 'end', values=row, tags=(tag,))




    def on_close(self):
        self.destroy()
        self.master.destroy()  

    def back_to_admin_homepage(self):
        self.withdraw()
        self.master.switch_frame('adminhomepage')
        self.master.deiconify()


