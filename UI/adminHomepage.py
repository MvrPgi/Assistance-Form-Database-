
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, Entry, messagebox, StringVar
from mysql_connection import DatabaseConnection
import mysql.connector
from resources.FileTracker.tracker import resource_path


class AdminHomepage(tk.Canvas):
    def __init__(self, master = None,switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.database = DatabaseConnection()
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        self.last_selected = None

        self.dashboardLogo = PhotoImage(file=resource_path("resources/adminhome/dashboardlogo.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/adminhome/dashboardbg.png"))
        self.gradiantBG = PhotoImage(file=resource_path("resources/adminhome/gradiant.png"))
        self.ShapeBg = PhotoImage(file=resource_path("resources/adminhome/shapebg.png"))
        self.ButtonBG = PhotoImage(file=resource_path("resources/adminhome/ButtonBGA.png"))


        self.dashboardButton = PhotoImage(file=resource_path("resources/adminhome/dashboardButton.png"))
        self.tablesButton = PhotoImage(file=resource_path("resources/adminhome/tables.png"))
        self.applicantsButton = PhotoImage(file=resource_path("resources/adminhome/ApplicantButton.png"))
        self.HouseholdButton = PhotoImage(file=resource_path("resources/adminhome/HouseHoldButton.png"))
        self.ReferenceButton = PhotoImage(file=resource_path("resources/adminhome/ReferenceButton.png"))
        self.profileButton = PhotoImage(file=resource_path("resources/adminhome/profile.png"))
        self.logoutButton = PhotoImage(file=resource_path("resources/adminhome/LogoutButton.png"))



        self.create_image(410.0, 250.0, image = self.gradiantBG) 
        #self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(50.0, 60.0, image = self.dashboardLogo)
        self.create_image(330.0, 100.0, image = self.ShapeBg)
        self.create_image(520.0, 100.0, image = self.ShapeBg)
        self.create_image(710.0, 100.0, image = self.ShapeBg)
        self.create_image(100.0, 165.0, image = self.ButtonBG)
        self.create_image(100.0, 215.0, image = self.ButtonBG)
        self.create_image(100.0, 380.0, image = self.ButtonBG)
        

        self.text_item = self.create_text(100.0, 40.0, anchor="nw", text="", fill="#FFFFFF", font=("Nokora", 17 * -1, "bold"))
        self.UpdateAdminName()



        self.create_text(20.0, 110.0, anchor = "nw", text = "NAVIGATION", fill="#FFFFFF", font=("Nokora", 11 * -1,"bold"))
        self.create_line(20.0, 100.0, 200.0, 100.0, fill="#FFFFFF")

        self.create_text(270.0, 50.0, anchor = "nw", text = "Total No Of Applicants", fill="#000000", font=("Nokora", 12 * -1,"bold"))
        self.create_text(455.0, 50.0, anchor = "nw", text = "Average Monthly Salary", fill="#000000", font=("Nokora", 12 * -1,"bold"))
        self.create_text(660.0, 50.0, anchor = "nw", text = "Philhealth Member", fill="#000000", font=("Nokora", 12 * -1,"bold"))





        self.TotalApplicants = StringVar(value="0")
        self.AverageApplicantSalary = StringVar(value="0")
        self.Philhealth = StringVar(value="0")

        Applicantcount = self.database.count_applicant_details()
        self.TotalApplicants.set(Applicantcount)

        Salary = self.database.average_monthly_income()
        Salary = "₱{:.0f}".format(Salary)
        self.AverageApplicantSalary.set(Salary)

        Philhealth = self.database.count_philhealth_member()
        self.Philhealth.set(Philhealth)

        # Create text items on the canvas
        self.text_id_1 = self.create_text(310.0, 80.0, anchor="nw", text=self.TotalApplicants.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))
        self.text_id_2 = self.create_text(450.0, 80.0, anchor="nw", text=self.AverageApplicantSalary.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))
        self.text_id_3 = self.create_text(690.0, 80.0, anchor="nw", text=self.Philhealth.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))

        self.create_line(270, 140, 390, 140, fill="#1B4B77")
        self.create_line(455, 140, 585, 140, fill="#1B4B77")
        self.create_line(645, 140, 780, 140, fill="#1B4B77")



#Button
        self.DashboardButton = tk.Button(self, image=self.dashboardButton, borderwidth=0, highlightthickness=0, command=lambda:print("DashBoard"), relief="flat")
        self.DashboardButton.place(x=20.0, y=147.0, width=160.0, height=30.0)
        self.TablesButton = tk.Button(self, image=self.tablesButton, borderwidth=0, highlightthickness=0, command=self.go_to_maintable)
        self.TablesButton.place(x=23.0, y=199.0, width=157.0, height=30.0)
        self.ApplicantTableButton = tk.Button(self, image=self.applicantsButton, borderwidth=0, highlightthickness=0, command=self.go_to_applicant, relief="flat")
        self.HouseholdTableButton = tk.Button(self, image=self.HouseholdButton, borderwidth=0, highlightthickness=0, command=self.go_to_household, relief="flat")
        self.ReferenceTableButton = tk.Button(self, image=self.ReferenceButton, borderwidth=0, highlightthickness=0, command=self.go_to_reference, relief="flat")
        self.LogOutButton = tk.Button(self, image=self.logoutButton, borderwidth=0, highlightthickness=0, command= self.LogOut, relief="flat")
        
        self.ApplicantTableButton.place(x=40.0, y=250.0, width=140, height=28.0)
        self.HouseholdTableButton.place(x=40.0, y=285.0, width=140, height=28.0)
        self.ReferenceTableButton.place(x=40.0, y=320.0, width=140, height=28.0)
        self.LogOutButton.place(x=23.0, y=365.0, width=140, height=28.0)


        
        self.TableCanva = tk.Canvas(self, bg="#FFFFFF", height=220, width=540, highlightthickness=0)
        self.TableCanva.place(x=250.0, y=230.0)

        self.Tree = ttk.Treeview(self.TableCanva,show='headings', height=10)
        self.Tree.pack_propagate(False) # Prevent the treeview from resizing with the window
        self.Tree.place(x=270,y=110, anchor="center", width=540, height=220)
        self.style = ttk.Style()

        

        self.HScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.Tree.xview)
        self.HScroll.place(x=520, y=455, anchor="center", width=540,height=10)
        
        self.Tree.configure(xscrollcommand=self.HScroll.set)

        self.ComboBoxEasy = ttk.Combobox(self, state="readonly")
        self.ComboBoxEasy.place(x=520, y=210, anchor="center", width=540, height=20)
        self.ComboBoxEasy["values"] = ("Easy 1", "Easy 2", "Easy 3", "Moderate 1", "Moderate 2", "Moderate 3", "Moderate 4", "Hard 1", "Hard 2", "Hard 3")
        self.ComboBoxEasy.bind("<<ComboboxSelected>>", self.update_treeview)








    def CountApplicants(self):
        count = self.database.count_applicant_details
        self.TotalApplicants.set(count)

    def UpdateAdminName(self):
        username = self.GetUserAdminName()
        if username:
            self.itemconfig(self.text_item, text=username)

    def GetUserAdminName(self):
        username = self.database.GetLastAdminEntry()
        print(username)
        return username
    




    def go_to_maintable(self):
        print("Go to maintable")
        if self.switch_frame:
            print("Switching to adminbench...")
            self.switch_frame('adminbench')

    def go_to_household(self):
        print("Go to applicanttable")
        if self.switch_frame:
            print("Switching to adminbench...")
            self.switch_frame('household')
    def go_to_applicant(self):
        print("Go to applicanttable")
        if self.switch_frame:
            print("Switching to adminbench...")
            self.switch_frame('applicant')
    def go_to_reference(self):
        print("Go to referencetable")
        if self.switch_frame:
            print("Switching to adminbench...")
            self.switch_frame('reference')



    def LogOut(self):
        print("LogOut")
        # Ask for confirmation
        if messagebox.askyesno("Log Out", "Are you sure you want to log out?"):
            print("Logging out...")
            if self.switch_frame:
                print("Switching to login...")
                self.switch_frame('applicantadmin')
        else:
            print("Log out cancelled.")
    
    def Easy1Columns(self):
        EasyRows1 = self.database.EasyTask1()
        self.ColumnsEasy = ("Applicant_ID", "Full_Name", "Age")
        self.Tree["columns"] = self.ColumnsEasy
    
        for col in self.ColumnsEasy:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)            
    
        for row in self.Tree.get_children():
            self.Tree.delete(row)# Clear the existing data in the treeview
    
        # Define alternating colors
        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"  # Slightly darker grey

        # Insert data with alternating colors
        for index, row in enumerate(EasyRows1):
            tag = f"color_{index % 2}"  # Alternating tag
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))


    def Easy2Columns(self):
        self.EasyRows2 = self.database.EasyTask2()
        self.ColumnsEasy = ("Applicant_ID", "Full_Name", "Montly_Income","Occupation")
        self.Tree["columns"] = self.ColumnsEasy
        for col in self.ColumnsEasy:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)            
        for row in self.Tree.get_children():
            self.Tree.delete(row)
        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"  # Slightly darker grey

        for index, row in enumerate(self.EasyRows2):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Easy3Columns(self):
        self.EasyRows3 = self.database.EasyTask3()
        self.ColumnsEasy = ("Applicant_ID", "Full_Name", "Address","Civil_Status","Birth_Date","Age","Sex","Nationality","Religion","Highest_Educational_Attainment","Occupation","Monthly Income","Membership","Other Source Of Income","Monthly Expenditures","Gross Monthly Income","Net Monthly Income")
        self.Tree["columns"] = self.ColumnsEasy

        for col in self.ColumnsEasy:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)            
        for row in self.Tree.get_children():
            self.Tree.delete(row)


        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"  # Slightly darker grey

  
        for index, row in enumerate(self.EasyRows3):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            tag = f"color_{index % 2}"  # Alternating tag
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Moderate1Columns(self):
        self.Moderate1Columns = self.database.ModerateTask1()
        self.ColumnsModerate = ("Sex","Count")
        self.Tree["columns"] = self.ColumnsModerate

        for col in self.ColumnsModerate:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)

        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Moderate1Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Moderate2Columns(self):
        self.Moderate2Columns = self.database.ModerateTask2()
        self.ColumnsModerate =("Highest Educational Attainment", "Average Monthly Income")
        self.Tree["columns"] = self.ColumnsModerate

        for col in self.ColumnsModerate:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)
        
        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Moderate2Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))
    
    def Moderate3Columns(self):
        self.Moderate3Columns = self.database.ModerateTask3()
        self.ColumnsModerate = ("Applicant ID", "Full Name", "Address", "Average Monthly Income")
        self.Tree["columns"] = self.ColumnsModerate

        for col in self.ColumnsModerate:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)

        color1 = "#1B4B77"  # Light grey
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Moderate3Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Moderate4Columns(self):
        self.Moderate4Columns = self.database.ModerateTask4()
        self.ColumnsModerate = ("Occupation", "Member Count ", "Average Gross Income")
        self.Tree["columns"] = self.ColumnsModerate

        for col in self.ColumnsModerate:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)

        color1 = "#1B4B77"
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Moderate4Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Hard1Columns(self):
        self.Hard1Columns = self.database.HardTask1()
        self.ColumnsHard = ("Applicant ID", "Full Name", "Total Family Income")
        self.Tree["columns"] = self.ColumnsHard

        for col in self.ColumnsHard:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)
            
        color1 = "#1B4B77"
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Hard1Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Hard2Columns(self):
        self.Hard2Columns = self.database.HardTask2()
        self.ColumnsHard = ("Applicant Name", "Minimum Family Income", "Maximum Family Income")
        self.Tree["columns"] = self.ColumnsHard

        for col in self.ColumnsHard:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)
            
        color1 = "#1B4B77"
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Hard2Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color,foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))

    def Hard3Columns(self):
        self.Hard3Columns = self.database.HardTask3()
        self.ColumnsHard = ("Applicant ID", "Full Name", "Family Member Count", "Average Family Income")
        self.Tree["columns"] = self.ColumnsHard

        for col in self.ColumnsHard:
            self.Tree.heading(col, text=col)
            self.Tree.column(col, width=150, minwidth=150, anchor=tk.CENTER, stretch=tk.YES)

        for row in self.Tree.get_children():
            self.Tree.delete(row)
            
        color1 = "#1B4B77"
        color2 = "#FFFBFB"

        for index, row in enumerate(self.Hard3Columns):
            tag = f"color_{index % 2}"
            color = color1 if index % 2 == 0 else color2
            textcolor = "#FFFFFF" if index % 2 == 0 else "#000000"
            self.Tree.tag_configure(tag, background=color, foreground=textcolor)
            self.Tree.insert('', 'end', values=row, tags=(tag,))




    def update_treeview(self, event=None):
        selected = self.ComboBoxEasy.get() 
        try:
            if selected == self.last_selected:
                print(f"Already selected: {selected}")
                return

            print(f"Selected: {selected}")
            self.last_selected = selected

            if selected == "Easy 1":
                self.Easy1Columns()
            elif selected == "Easy 2":
                self.Easy2Columns()
            elif selected == "Easy 3":
                self.Easy3Columns()
            elif selected == "Moderate 1":
                self.Moderate1Columns()
            elif selected == "Moderate 2":
                self.Moderate2Columns()
            elif selected == "Moderate 3":
                self.Moderate3Columns()
            elif selected == "Moderate 4":
                self.Moderate4Columns()
            elif selected == "Hard 1":
                self.Hard1Columns()
            elif selected == "Hard 2":
                self.Hard2Columns()
            elif selected == "Hard 3":
                self.Hard3Columns()
            else:
                print(f"Selection '{selected}' not recognized.")
        except Exception as e:
            print(f"An error occurred: {e}")


