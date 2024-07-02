import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry
import mysql.connector
from mysql_config import dbConfig
from mysql_connection import DatabaseConnection
from resources.FileTracker.tracker import resource_path

class AdminBench(tk.Toplevel):
        
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Admin Bench")
        self.geometry("1910x700")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.database = DatabaseConnection()

        
        # Create the upper frame
        self.UpperFrame = tk.Frame(self,height=200)
        self.UpperFrame.pack(side="top", fill=tk.X)

   
   
        # Create a canvas in the upper frame
        self.canvas = tk.Canvas(self.UpperFrame, bg="#FFFFFF")
        self.canvas.pack(fill=tk.BOTH, expand=True)
  
        self.Header = PhotoImage(file=resource_path("resources/adminbench/header.png"))
        self.canvas.create_image(960.0, 30, image = self.Header)

    


        self.ComboBoxSex = ttk.Combobox(self.canvas, values=["Male","Female"], state="readonly", width=10)
        self.ComboBoxSex.place(x=920.0, y=150, anchor="center")
        self.ComboBoxSex.bind("<<ComboboxSelected>>",self.GenderPicker)


        self.DeleteButtonImage = PhotoImage(file=resource_path("resources/adminbench/deleteButton.png"))
        self.deleteButton = tk.Button(self.canvas, image=self.DeleteButtonImage, command=lambda: print("hello word"))
        self.deleteButton.place(x=1020.0, y=150, anchor="center",width=95, height=23)

        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command=lambda: print("hello word"))
        self.updateButton.place(x=1120.0, y=150, anchor="center",width=95, height=23)




        # Create the lower frame
        self.LowerFrame = tk.Frame(self, bg="#FFFFFF",height=600)
        self.LowerFrame.pack(side="top", fill=tk.BOTH, expand=True,pady=10)

        
        # Create a treeview to display the data
        self.columns = ( # Create the columns
            "Reference No","Applicant ID","Date","Applicant Status", "Fullname", "Address", "Civil Status", "BirthDate", "Age",
            "Sex", "Nationality", "Religion", "Educational Attainment",
            "Occupation",  "Monthly Income","Membership", "OtherSourceOfIncome", "Monthly Expenditures",
            "GrossMonthlyIncome", "NetMonthlyIncome"
        )
        self.tree = ttk.Treeview(self.LowerFrame, columns=self.columns, show='headings',height=600)
        self.tree.pack_propagate(False)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=20)


        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#FFFFF", foreground="#000000", font=("Helvetica", 10))
        self.style.configure("Treeview",rowheight=25)
        
        self.tree.bind('<Double-1>', self.highlight)

        column_widths = {
            "Reference No": 100, "Applicant ID": 100, "Date": 100, "Applicant Status": 150, "Fullname": 150, "Address": 300, 
            "Civil Status": 75, "BirthDate": 100, "Age": 50, "Sex": 50, "Nationality": 100, "Religion": 100,
            "Educational Attainment": 250, "Occupation": 150, "Monthly Income": 150, 
            "Membership": 100, "OtherSourceOfIncome": 150, "Monthly Expenditures": 175,
            "GrossMonthlyIncome": 150, "NetMonthlyIncome": 150
        }

        for col in self.columns: # Create the headings  and set the column width
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100),anchor=tk.CENTER)




        # Create the horizontal scrollbar
        self.HScroll = ttk.Scrollbar(self.UpperFrame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the tree view to use the scrollbar
        self.tree.configure(xscrollcommand=self.HScroll.set)
        # Destroy the window when the close button is clicked
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        self.FetchReferenceApplicantData()

    def FetchReferenceApplicantData(self):
        rows = self.database.FetchRefApplincatDetails()

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

        for row in rows:
            self.tree.insert('', 'end', values=row)  # Insert new data into the Treeview

    def FemaleFetchApplicantData(self):
        rows = self.database.FetchFemaleApplicantDetails()

        for row in self.tree.get_children():
            self.tree.delete(row)  # Clear the existing data in the Treeview

        for row in rows:
            self.tree.insert('', 'end', values=row)  # Insert new data into the Treeview
    
    def GenderPicker(self,event):
        if self.ComboBoxSex.get() =='Male':
            self.MaleFetchApplicantData()
        if self.ComboBoxSex.get() =='Female':
            self.FemaleFetchApplicantData()



    def UpdateApplicantDetails(self, item):
        new_values = [self.entries[col].get() for col in self.columns]
        self.tree.item(item, values=new_values)

        # Update the database with the new values
        self.database.update_applicant_details(
            new_values[0], new_values[1], new_values[2], new_values[3], new_values[4], new_values[5], new_values[6],  # Update the database with the new values
            new_values[7], new_values[8], new_values[9], new_values[10], new_values[11], new_values[12], 
            new_values[13], new_values[14], new_values[15], new_values[16], new_values[17], new_values[18], new_values[19], new_values[20], new_values[21]
        )

        self.edit_window.destroy()

    def UpdateRefApplicantDetails(self, item):
        new_values = [self.entries[col].get() for col in self.columns]
        self.tree.item(item, values=new_values)

        # Update the database with the new values
        self.database.UpdateRefApplicantDetails(
            new_values[0], new_values[1], new_values[2], new_values[3], new_values[4], new_values[5], new_values[6],  # Update the database with the new values
            new_values[7], new_values[8], new_values[9], new_values[10], new_values[11], new_values[12], 
            new_values[13], new_values[14], new_values[15], new_values[16], new_values[17], new_values[18], new_values[19]
        )

        self.edit_window.destroy()


    def SelectDeleteRow(self, event):
        select = self.tree.selection()
        if not select:
            print("No item selected.")
            return None

        item_id = select[0]
        values = self.tree.item(item_id, "values")
        return values
    

    def DeleteSelectRow(self):
        select = self.tree.selection()
        if not select:
            print("No item selected.")
            return
        
        item_id = select[0]
        
        if not self.tree.exists(item_id):
            print(f"Item {item_id} not found.")
            return
        
        values = self.tree.item(item_id, "values")

        # Assuming the second value in the row is the primary key for deletion
        primary_key = values[1]
        
        try:
            self.database.DeleteApplicantDetails(primary_key)
        except Exception as e:
            print(f"Error deleting from database: {e}")
            return

        # Remove item from Treeview
        self.tree.delete(item_id)




    def highlight(self,event):
        item = self.tree.selection()[0] # Get the selected item
        values = self.tree.item(item, "values") # Get the values of the selected item

        self.edit_window = tk.Toplevel(self)
        self.edit_window.geometry("350x550")
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



        self.saveButton = tk.Button(self.edit_window, text="Save",state='disabled', command=lambda: self.UpdateRefApplicantDetails(item))
        self.saveButton.grid(row=17, column=0, columnspan=2,pady=7)

    def toggle_entries(self):
        if self.RadioButtonVariable.get() == True:
            self.saveButton.config(state="normal")
            for entry in self.entries.values():
                entry.config(state="normal")
            for i in range(3):
                self.entries[self.columns[i]].config(state="readonly")      
                

        elif self.RadioButtonVariable.get() == False:
            self.saveButton.config(state="disabled")
            for entry in self.entries.values():
                entry.config(state="readonly")
            for i in range(3):
                self.entries[self.columns[i]].config(state="readonly")
            

    def on_close(self):
        self.destroy()
        self.master.destroy()  



    # def FetchApplicantData(self):
    #     rows = self.database.FetchApplincatDetailsA()
        
    #     for row in self.tree.get_children():
    #         self.tree.delete(row)# Clear the existing data in the treeview


    #     for row in rows:
    #         self.tree.insert('', 'end', values=row)# Insert new data into the treeview




