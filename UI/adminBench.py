import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry
import mysql.connector
from mysql_config import dbConfig
from mysql_connection import DatabaseConnection
from resources.FileTracker.tracker import resource_path

class AdminBench(tk.Toplevel):
        
    def __init__(self, master = None,switch_frame=None):
        super().__init__()
        self.geometry("1910x700")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.database = DatabaseConnection()

        # Create the canvas in the upper frame
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.Header = PhotoImage(file=resource_path("resources/adminbench/header.png"))
        self.canvas.create_image(960.0, 30, image=self.Header)

        self.ComboBoxSex = ttk.Combobox(self.canvas, values=["Male", "Female"], state="readonly", width=10)
        self.ComboBoxSex.place(x=400, y=90, anchor="center")
        self.ComboBoxSex.bind("<<ComboboxSelected>>", self.GenderPicker)

        self.DeleteButtonImage = PhotoImage(file=resource_path("resources/adminbench/deleteButton.png"))
        self.deleteButton = tk.Button(self.canvas, image=self.DeleteButtonImage, command=self.DeleteRow)
        self.deleteButton.place(x=100.0, y=90, anchor="center", width=95, height=20)

        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command= self.EditButton)
        self.updateButton.place(x=200.0, y=90, anchor="center", width=95, height=20)

        self.RefreshButtonImage = PhotoImage(file=resource_path("resources/adminbench/refreshButton.png"))
        self.refreshButton = tk.Button(self.canvas, image=self.RefreshButtonImage, command=self.FetchReferenceApplicantData)
        self.refreshButton.place(x=300.0, y=90, anchor="center", width=95, height=20)


        self.backButton = tk.Button(self.canvas, text="Back", command=self.back_to_admin_homepage)
        self.backButton.place(x=500.0, y=90, anchor="center", width=95, height=20)

        self.columns = (
            "Reference_No", "Applicant_ID", "Date", "Applicant_Status", "Full_Name", "Address", "Civil_Status", 
            "Birth_Date", "Age", "Sex", "Nationality", "Religion", "Highest Educational Attainment", "Occupation", 
            "Monthly_Income", "Membership", "OtherSourceOfIncome", "Monthly_Expenditures", "GrossMonthlyIncome", 
            "NetMonthlyIncome", "Household_ID", "Family Full Name", "Family Age", "Family Civil Status", 
            "Relationship", "Family Highest Educational Attainment", "Family Occupation", "Family Income"
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
            "Reference_No": 100, "Applicant_ID": 100, "Date": 100, "Applicant_Status": 150, "Full_Name": 150, 
            "Address": 300, "Civil_Status": 75, "Birth_Date": 100, "Age": 50, "Sex": 50, "Nationality": 100, 
            "Religion": 100, "Highest Educational Attainment": 250, "Occupation": 150, "Monthly_Income": 150, 
            "Membership": 100, "OtherSourceOfIncome": 150, "Monthly_Expenditures": 175, "GrossMonthlyIncome": 150, 
            "NetMonthlyIncome": 150, "Household_ID": 100, "Family Full Name": 150, "Family Age": 50,
            "Family Civil Status": 150, "Relationship": 100, "Family Highest Educational Attainment": 240,
            "Family Occupation": 150, "Family Income": 150
        }

        # Set headings and column widths
        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=column_widths.get(col, 100), anchor=tk.CENTER)

        # Create the horizontal scrollbar
        self.HScroll = ttk.Scrollbar(self.canvas, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.place(x=960.0, y=115, anchor="center", width=1900)

        # Configure the tree view to use the scrollbar
        self.tree.configure(xscrollcommand=self.HScroll.set)


        # Destroy the window when the close button is clicked
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        self.FetchReferenceApplicantData()

    def FetchReferenceApplicantData(self):
        rows = self.database.FetchRefApplincatHouseDetails()

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



    def MaleFetchApplicantData(self):
        rows = self.database.FetchMaleApplicantDetails()

        for row in self.tree.get_children():
            self.tree.delete(row)  # Clear the existing data in the Treeview

        # Define alternating colors
        color1 = "#CFCECE"  # Light grey
        color2 = "#FFFFFF"  # Slightly darker grey

        # Insert data with alternating colors
        for index, row in enumerate(rows):
            tag = f"color_{index % 2}"  # Alternating tag
            color = color1 if index % 2 == 0 else color2
            self.tree.tag_configure(tag, background=color)
            self.tree.insert('', 'end', values=row, tags=(tag,))

    def FemaleFetchApplicantData(self):
        rows = self.database.FetchFemaleApplicantDetails()

        for row in self.tree.get_children():
            self.tree.delete(row)  # Clear the existing data in the Treeview

        color1 = "#CFCECE"  # Light grey
        color2 = "#FFFFFF"  # Slightly darker grey

        # Insert data with alternating colors
        for index, row in enumerate(rows):
            tag = f"color_{index % 2}"  # Alternating tag
            color = color1 if index % 2 == 0 else color2
            self.tree.tag_configure(tag, background=color)
            self.tree.insert('', 'end', values=row, tags=(tag,))
    
    def GenderPicker(self,event):
        if self.ComboBoxSex.get() =='Male':
            self.MaleFetchApplicantData()
        if self.ComboBoxSex.get() =='Female':
            self.FemaleFetchApplicantData()



    def UpdateRefAppHouseDetails(self, item):
        new_values = [self.entries[col].get() for col in self.columns]
        self.tree.item(item, values=new_values)

        # Update the database with the new values
        self.database.UpdateRefAppHouseDetails(
            new_values[0], new_values[1], new_values[2], new_values[3], new_values[4], new_values[5], new_values[6],  # Update the database with the new values
            new_values[7], new_values[8], new_values[9], new_values[10], new_values[11], new_values[12], 
            new_values[13], new_values[14], new_values[15], new_values[16], new_values[17], new_values[18], new_values[19], new_values[20], new_values[21],new_values[22],new_values[23],new_values[24],new_values[25],new_values[26],new_values[27]
        )

        self.edit_window.destroy()


    


    def DeleteRow(self):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]  # Get the first selected item
            values = self.tree.item(item, "values")  # Get the values of the selected item
            
            # Assuming the second value in the row is the primary key for deletion
            primary_key = values[0]  # Adjust index based on your primary key column
            
            try:
                self.database.delete_applicant_details(primary_key)
                self.tree.delete(item)
                print(f"Deleted item with primary key {primary_key}.")
            except Exception as e:
                print(f"Error deleting from database: {e}")
        else:
            print("No item selected.")

    def SelectDeleteRow(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]  # Get the first selected item
            values = self.tree.item(item, "values")  # Get the values of the selected item
            print(values)
        else:
            print("No item selected.")



    def EditButton(self):
        item = self.tree.selection()[0] # Get the selected item
        values = self.tree.item(item, "values") # Get the values of the selected item

        self.edit_window = tk.Toplevel(self)
        self.edit_window.geometry("450x720")
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

        for entry in self.entries.values():
            entry.config(state="readonly")        
        for i in range(3):
            self.entries[self.columns[i]].config(state="readonly")
        self.entries[self.columns[20]].config(state="readonly")      



        self.saveButton = tk.Button(self.edit_window, text="Save",state='disabled', command=lambda: self.UpdateRefAppHouseDetails(item))
        self.saveButton.grid(row=17, column=0, columnspan=2,pady=7)

    def toggle_entries(self):
        if self.RadioButtonVariable.get() == True:
            self.saveButton.config(state="normal")
            for entry in self.entries.values():
                entry.config(state="normal")
            for i in range(3):
                self.entries[self.columns[i]].config(state="readonly")
            self.entries[self.columns[20]].config(state="readonly")      
                

        elif self.RadioButtonVariable.get() == False:
            self.saveButton.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")
            for i in range(3):
                self.entries[self.columns[i]].config(state="readonly")
            

    def on_close(self):
        self.destroy()
        self.master.destroy()  

    def back_to_admin_homepage(self):
        self.withdraw()
        self.master.switch_frame('adminhomepage')
        self.master.deiconify()








