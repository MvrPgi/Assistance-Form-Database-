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
        self.geometry("1920x700")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.database = DatabaseConnection()

        
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

        # Count the number of applicants
        self.canvas.create_text(120.0, 150.0, text="Total Number Of Applicant: ", font=("Mada Regular", 10*-1), fill="#000000")
        Count = self.database.count_applicant_details()
        self.CountEntry = Entry(self.canvas, font=("Mada Regular", 10*-1), bd=0, bg="#FFE5AB", highlightthickness=0,fg="#000716",justify="center")
        self.CountEntry.place(x=120.0, y=167.0, anchor="center")
        self.CountEntry.insert(0, Count)
        self.CountEntry.config(state="readonly")

        # Count the number of male applicants
        self.canvas.create_text(320.0, 150.0, text="Total Number Of Male Applicant: ", font=("Mada Regular", 10*-1), fill="#000000")
        Count_M = self.database.count_male_applicant_details()
        self.CountEntry_M = Entry(self.canvas, font=("Mada Regular", 10*-1), bd=0, bg="#FFE5AB", highlightthickness=0,fg="#000716",justify="center")
        self.CountEntry_M.place(x=320.0, y=167.0, anchor="center")
        self.CountEntry_M.insert(0, Count_M)
        self.CountEntry_M.config(state="readonly")


        self.canvas.create_text(520.0, 150.0, text="Total Number Of Female Applicant: ", font=("Mada Regular", 10*-1), fill="#000000")
        Count_F = self.database.count_female_applicant_details()
        self.CountEntry_M = Entry(self.canvas, font=("Mada Regular", 10*-1), bd=0, bg="#FFE5AB", highlightthickness=0,fg="#000716",justify="center")
        self.CountEntry_M.place(x=520.0, y=167.0, anchor="center")
        self.CountEntry_M.insert(0, Count_F)
        self.CountEntry_M.config(state="readonly")

    



  
        # Create a button to fetch data
        self.FetchApplicant = tk.Button(self.canvas,image =self.button_image_1,borderwidth=0,highlightthickness=0, command=self.FetchApplicantData)
        self.FetchApplicant.place(x=120.0, y=320, anchor="center")
        # self.FetchApplicant = tk.Button(self.canvas,text= "GET DATA",borderwidth=0,width=20,highlightthickness=0, command=self.FetchApplicantData)
        # self.FetchApplicant.place(x=120.0, y=300, anchor="center")


        self.ComboBoxSex = ttk.Combobox(self.canvas, values=["Male","Female"], state="readonly", width=10)
        self.ComboBoxSex.place(x=520.0, y=300, anchor="center")
        self.ComboBoxSex.bind("<<ComboboxSelected>>",self.GenderPicker)


        self.ComboBoxSex = ttk.Combobox(self.canvas, values=["Male","Female"], state="readonly", width=10)
        self.ComboBoxSex.place(x=520.0, y=300, anchor="center")
        self.ComboBoxSex.bind("<<ComboboxSelected>>",self.GenderPicker)




        # Create the lower frame
        self.LowerFrame = tk.Frame(self)
        self.LowerFrame.pack(side="bottom", fill=tk.BOTH, expand=True)
        
        # Create a treeview to display the data
        self.columns = ( # Create the columns
            "Applicant ID", "FullName", "Address", "Civil Status", "BirthDate", "Age",
            "Sex", "Nationality", "Religion", "Educational Attainment",
            "Occupation",  "Monthly Income","Membership", "OtherSourceOfIncome", "Monthly Expenditures",
            "GrossMonthlyIncome", "NetMonthlyIncome"
        )
        self.tree = ttk.Treeview(self.LowerFrame, columns=self.columns, show='headings')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="#D97F76", foreground="#000000", font=("Helvetica", 10))
        self.style.configure("Treeview", background="#FFFFFF", foreground="#000000", fieldbackground="yellow")
        self.tree.bind('<Double-1>', self.highlight)

        column_widths = {
            "ApplicantID": 100, "FullName": 150, "Address": 300, "Civil Status": 75, 
            "BirthDate": 100, "Age": 100, "Sex": 100, "Nationality": 100, "Religion": 100,
             "Educational Attainment": 250, "Occupation": 150,"Monthly Income": 150, 
             "Membership": 100, "OtherSourceOfIncome": 150, "Monthly Expenditures": 175,
            "GrossMonthlyIncome": 150, "NetMonthlyIncome": 150
        }
        
        

        for col in self.columns: # Create the headings  and set the column width
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100),anchor=tk.CENTER)

        
        # Create a vertical scrollbar/ horizontal scrollbar
        self.VScroll = ttk.Scrollbar(self.LowerFrame, orient=tk.VERTICAL, command=self.tree.yview)
        self.VScroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.VScroll.set)
        self.HScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.HScroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.HScroll.set)

        # Destroy the window when the close button is clicked
        self.protocol("WM_DELETE_WINDOW", self.on_close)


        # self.database = DatabaseConnection()
    def FetchApplicantData(self):
        rows = self.database.FetchApplincatDetailsA()
        
        for row in self.tree.get_children():
            self.tree.delete(row)# Clear the existing data in the treeview


        for row in rows:
            self.tree.insert('', 'end', values=row)# Insert new data into the treeview


    def GenderPicker(self,event):
        if self.ComboBoxSex.get() =='Male':
            self.MaleFetchApplicantData()
        if self.ComboBoxSex.get() =='Female':
            self.FemaleFetchApplicantData()


    def MaleFetchApplicantData(self):
        rows = self.database.FetchMaleApplincatDetails()
        
        for row in self.tree.get_children():
            self.tree.delete(row)# Clear the existing data in the treeview

        for row in rows:
            self.tree.insert('', 'end', values=row)# Insert new data into the treeview

    def FemaleFetchApplicantData(self):
        rows = self.database.FetchFemaleApplincatDetails()
        
        for row in self.tree.get_children():
            self.tree.delete(row)# Clear the existing data in the treeview

        for row in rows:
            self.tree.insert('', 'end', values=row)# Insert new data into the treeview




    def update(self, item):
        new_values = [self.entries[col].get() for col in self.columns]
        self.tree.item(item, values=new_values)

        # Update the database with the new values
        self.database.update_applicant_details(
            new_values[0], new_values[1], new_values[2], new_values[3], new_values[4], new_values[5], new_values[6],  # Update the database with the new values
            new_values[7], new_values[8], new_values[9], new_values[10], new_values[11], new_values[12], 
            new_values[13], new_values[14], new_values[15], new_values[16]
        )

        self.edit_window.destroy()

    def highlight(self,event ):
        item = self.tree.selection()[0] # Get the selected item
        values = self.tree.item(item, "values") # Get the values of the selected item

        self.edit_window = tk.Toplevel(self)
        self.edit_window.geometry("350x450")
        self.edit_window.wm_resizable(False, False)

        self.edit_window.title("Edit") 

        self.RadioButtonVariable = tk.BooleanVar(value=True)
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
            entry.grid(row=i, column=1)# Place the entry widget
            entry.insert(0, values[i]) # Insert the value of the selected item into the entry widget
            self.entries[col] = entry # Store the entry widget

        for entry in self.entries.values():
            entry.config(state="readonly")        
        self.entries[self.columns[0]].config(state="readonly")


        tk.Button(self.edit_window, text="Save", command=lambda: self.update(item)).grid(row=17, column=0)

    def toggle_entries(self):
        if self.RadioButtonVariable.get() == "True":
            for entry in self.entries.values():
                entry.config(state="normal")        
                
        elif self.RadioButtonVariable.get() == "False":
            for entry in self.entries.values():
                entry.config(state="readonly")
        self.entries[self.columns[0]].config(state="readonly")


    def on_close(self):
        self.destroy()
        self.master.destroy()  



