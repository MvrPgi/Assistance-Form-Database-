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
        self.canvas.create_image(955.0, 15, image=self.Header)


        self.EditBGPic = PhotoImage(file=resource_path("resources/adminbench/UpdateBG.png"))
        self.canvas.create_image(80.0, 90, image=self.EditBGPic)
        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command=self.EditButton, borderwidth=0, highlightthickness=0)
        self.updateButton.place(x=80.0, y=90,anchor="center", width=95, height=20)


        self.RefreshBGPic = PhotoImage(file=resource_path("resources/adminbench/updateBG.png"))
        self.canvas.create_image(210.0, 90, image=self.RefreshBGPic)
        self.RefreshButtonImage = PhotoImage(file=resource_path("resources/adminbench/refreshButton.png"))
        self.refreshButton = tk.Button(self.canvas, image=self.RefreshButtonImage, command=self.FetchRefrenceTable, borderwidth=0, highlightthickness=0)
        self.refreshButton.place(x=210.0, y=92, anchor="center", width=95, height=20)

        self.backButtonImage = PhotoImage(file=resource_path("resources/adminbench/homeButton.png"))
        self.backButton = tk.Button(self.canvas,image=self.backButtonImage, command=self.back_to_admin_homepage,borderwidth=0, highlightthickness=0)
        self.backButton.place(x=25.0, y=25, anchor="center", width=30, height=20)


        self.columns = (
        "Reference_No","Applicant_ID","Date","Applicant_Status"
        )
        
        # Create the Treeview widget
        self.tree = ttk.Treeview(self.canvas, columns=self.columns, show='headings', height=20)
        self.tree.pack_propagate(False) # Prevent the treeview from resizing with the window
        self.tree.place(x=955.0, y=400, anchor="center", width=1870, height=560)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#FFFFF", foreground="#000000", font=("Nokora", 10))
        self.style.configure("Treeview", rowheight=25)



        # Set headings and column widths
        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=150, minwidth=300, anchor=tk.CENTER, stretch=tk.YES)                

        self.HScroll = ttk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.place(x=955.0, y=115, anchor="center", width=1880)

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

    def UpdateRefrenceTable(self,item):
        new_values =[self.entries[col].get() for col in self.columns]
        self.tree.item(item, values=new_values)


        self.database.UpdateReferenceDetails(
            new_values[0],new_values[1],new_values[2],new_values[3]
        )
        self.edit_window.destroy()

    def EditButton(self):
        item = self.tree.selection()[0] # Get the selected item
        values = self.tree.item(item, "values") # Get the values of the selected item

        self.edit_window = tk.Toplevel(self)
        self.edit_window.geometry("300x170")
        self.edit_window.wm_resizable(False, False)

        self.edit_window.title("Edit") 

        self.RadioButtonVariable = tk.BooleanVar(value=False)
        self.RadioButton = tk.Radiobutton(self.edit_window,variable=self.RadioButtonVariable,value=True ,text="Enable",command=self.toggle_entries)
        self.RadioButton.grid(row=0, column=0)
        self.RadioButton = tk.Radiobutton(self.edit_window, text="Disable",variable=self.RadioButtonVariable,value=False,command=self.toggle_entries)
        self.RadioButton.grid(row=0, column=1)

        self.LowerFrameEdit = tk.Frame(self.edit_window)
        self.LowerFrameEdit.grid(row=1, column=0, columnspan=2)
        self.EditWindow = tk.Frame(self.edit_window).grid(row=0, column=0, columnspan=2)
        self.entries = {} # Store the entry widgets
        for i, col in enumerate(self.columns): # Create the entry widgets
            tk.Label(self.LowerFrameEdit, text=col).grid(row=i, column=0) # Create a label
            entry = tk.Entry(self.LowerFrameEdit,width=30, justify="center")# Create an entry widget
            entry.grid(row=i, column=1,padx=5,pady =2)# Place the entry widget
            entry.insert(0, values[i]) # Insert the value of the selected item into the entry widget
            self.entries[col] = entry # Store the entry widget

        for entry in self.entries.values():# Disable the entry widgets
            entry.config(state="readonly")        # Disable the entry widgets
        self.entries[self.columns[1]].config(state="readonly") # Disable the entry widgets

        
        self.saveButton = tk.Button(self.edit_window, text="Save",state='disabled', command=lambda: self.UpdateRefrenceTable(item))
        self.saveButton.grid(row=5, column=0, columnspan=2,pady=7)


    def toggle_entries(self):
        if self.RadioButtonVariable.get() == True:
            self.saveButton.config(state="normal")
            for entry in self.entries.values():
                entry.config(state="normal")

            for i in range(2):  # Disable only columns 0, 1, and 2
                self.entries[self.columns[i]].config(state="readonly")
        else:
            self.saveButton.config(state="disabled") # Disable the save button
            for entry in self.entries.values():
                entry.config(state="readonly")





    def on_close(self):
        self.destroy()
        self.master.destroy()  

    def back_to_admin_homepage(self):
        self.withdraw()
        self.master.switch_frame('adminhomepage')
        self.master.deiconify()



