import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry
import mysql.connector
from mysql_config import dbConfig
from mysql_connection import DatabaseConnection
from resources.FileTracker.tracker import resource_path

class AdminBenchReference(tk.Toplevel):
        
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
        self.canvas.create_image(960.0, 30, image=self.Header)


        self.DeleteButtonImage = PhotoImage(file=resource_path("resources/adminbench/deleteButton.png"))
        self.deleteButton = tk.Button(self.canvas, image=self.DeleteButtonImage, command= print("Delete"))
        self.deleteButton.place(x=100.0, y=90, anchor="center", width=95, height=20)

        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command= print("Update"))
        self.updateButton.place(x=200.0, y=90, anchor="center", width=95, height=20)

        self.RefreshButtonImage = PhotoImage(file=resource_path("resources/adminbench/refreshButton.png"))
        self.refreshButton = tk.Button(self.canvas, image=self.RefreshButtonImage, command=self.FetchRefrenceTable)
        self.refreshButton.place(x=300.0, y=90, anchor="center", width=95, height=20)


        self.backButton = tk.Button(self.canvas, text="Back", command=self.back_to_admin_homepage)
        self.backButton.place(x=500.0, y=90, anchor="center", width=95, height=20)

        self.columns = (
        "Reference_No","Applicant_ID","Date","Applicant_Status"
        )
        
        # Create the Treeview widget
        self.tree = ttk.Treeview(self.canvas, columns=self.columns, show='headings', height=20)
        self.tree.pack_propagate(False) # Prevent the treeview from resizing with the window
        self.tree.place(x=955.0, y=400, anchor="center", width=1900, height=550)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#FFFFF", foreground="#000000", font=("Helvetica", 10))
        self.style.configure("Treeview", rowheight=25)



        # Column widths configuration
        column_widths = {
        "Reference_No":100,"Applicant_ID":100,"Date":100,"Applicant_Status":100
        }

        # Set headings and column widths
        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)            

        # Create the horizontal scrollbar
        self.HScroll = ttk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.place(x=955.0, y=115, anchor="center", width=1899)

        # Configure the tree view to use the scrollbar
        self.tree.configure(xscrollcommand=self.HScroll.set)


        # Destroy the window when the close button is clicked
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        self.FetchRefrenceTable()

    def FetchRefrenceTable(self):
        rows = self.database.FetchApplincatDetailsR()

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



