import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry,messagebox
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
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app

        # Create the canvas in the upper frame
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.Header = PhotoImage(file=resource_path("resources/adminbench/header.png"))
        self.canvas.create_image(955.0, 15, image=self.Header)
        self.canvas.create_text(435.0, 90, text="Filter By :", font=("Nokora", 10), fill="#000000")
        # self.canvas.create_line(15, 106, 1895, 106, fill="#000000")
        # self.canvas.create_line(13, 106, 13, 680, fill="#000000")
        # self.canvas.create_line(1896, 106, 1896, 680, fill="#000000")


        self.ComboBoxSex = ttk.Combobox(self.canvas, values=["Gender - Male", "Gender - Female"], state="readonly", width=30, font=("Nokora", 10,))
        self.ComboBoxSex.place(x=595, y=90, anchor="center")
        self.ComboBoxSex.bind("<<ComboboxSelected>>", self.GenderPicker)


        self.DeleteBGPic = PhotoImage(file=resource_path("resources/adminbench/DeleteBG.png"))
        self.canvas.create_image(80.0, 90, image=self.DeleteBGPic)
        self.DeleteButtonImage = PhotoImage(file=resource_path("resources/adminbench/deleteButton.png"))
        self.deleteButton = tk.Button(self.canvas, image=self.DeleteButtonImage, command=self.DeleteRow, borderwidth=0, highlightthickness=0)
        self.deleteButton.place(x=80.0, y=90, anchor="center", width=95, height=20)

        self.EditBGPic = PhotoImage(file=resource_path("resources/adminbench/UpdateBG.png"))
        self.canvas.create_image(210.0, 90, image=self.EditBGPic)
        self.UpdateButtonImage = PhotoImage(file=resource_path("resources/adminbench/updateButton.png"))
        self.updateButton = tk.Button(self.canvas, image=self.UpdateButtonImage, command= self.EditButton, borderwidth=0, highlightthickness=0)
        self.updateButton.place(x=210.0, y=90, anchor="center", width=95, height=20)

        self.RefreshBGPic = PhotoImage(file=resource_path("resources/adminbench/updateBG.png"))
        self.canvas.create_image(340.0, 90, image=self.RefreshBGPic)
        self.RefreshButtonImage = PhotoImage(file=resource_path("resources/adminbench/refreshButton.png"))
        self.refreshButton = tk.Button(self.canvas, image=self.RefreshButtonImage, command=self.FetchReferenceApplicantData, borderwidth=0, highlightthickness=0)
        self.refreshButton.place(x=340.0, y=92, anchor="center", width=95, height=18)

        self.SearchBGPic = PhotoImage(file=resource_path("resources/adminbench/searchBG.png"))
        self.canvas.create_image(1820.0, 90, image=self.SearchBGPic)
        self.SearchButtonImage = PhotoImage(file=resource_path("resources/adminbench/searchButton.png"))
        self.searchButton = tk.Button(self.canvas, image=self.SearchButtonImage, borderwidth=0, highlightthickness=0, command=self.SearchApplicant)
        self.searchButton.place(x=1820.0, y=90, anchor="center", width=95, height=20)

        self.searchBG = PhotoImage(file=resource_path("resources/adminbench/searchEntry.png"))
        self.canvas.create_image(1600.0, 90, image=self.searchBG)
        self.EntrySearch = Entry(self.canvas, font=("Nokora", 10), width=30,bd=0, bg="#FFFFFF",highlightthickness=0, relief="flat")
        self.EntrySearch.place(x=1590.0, y=90, anchor="center")

        self.backButtonImage = PhotoImage(file=resource_path("resources/adminbench/homeButton.png"))
        self.backButton = tk.Button(self.canvas,image=self.backButtonImage, command=self.back_to_admin_homepage,borderwidth=0, highlightthickness=0)
        self.backButton.place(x=25.0, y=25, anchor="center", width=30, height=20)

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
        self.tree.place(x=955.0, y=400, anchor="center", width=1880, height=560)

        # Style configuration
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
        self.FetchReferenceApplicantData()




    def DeleteRow(self):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]  # Get the first selected item
            values = self.tree.item(item, "values")  # Get the values of the selected item
            
            # Assuming the second value in the row is the primary key for deletion
            primary_key = values[1]  # Adjust index based on your primary key column
            
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

    def SearchApplicant(self):
        search = self.EntrySearch.get()
        rows = self.database.searchApplicantDetails(search)
        
        # Debugging statements
        print(f"Search term: {search}")
        print(f"Rows returned: {rows}")


        for row in self.tree.get_children(): 
            self.tree.delete(row)


        if not rows: # If no results are found
            print("No results found.")
            messagebox.showinfo("No Results", "No references found.")
            return

        color1 = "#CFCECE"  # Light grey
        color2 = "#FFFFFF"  # Slightly darker grey

        for index, row in enumerate(rows):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            self.tree.tag_configure(tag, background=color)
            self.tree.insert('', 'end', values=row, tags=(tag,))

    def FetchReferenceApplicantData(self):
        self.EntrySearch.delete(0, tk.END)  # Clear the search entry
        self.ComboBoxSex.set("") # Clear the combobox selection
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
        if self.ComboBoxSex.get() =='Gender - Male':
            self.EntrySearch.delete(0, tk.END)  # Clear the search entr
            self.MaleFetchApplicantData()
        if self.ComboBoxSex.get() =='Gender - Female':
            self.EntrySearch.delete(0, tk.END)  # Clear the search entry
            self.FemaleFetchApplicantData()

            

    def on_close(self):
        self.destroy()
        self.master.destroy()  

    def back_to_admin_homepage(self):
        self.withdraw()
        self.master.switch_frame('adminhomepage')
        self.master.deiconify()








