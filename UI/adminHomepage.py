
import tkinter as tk
from tkinter import ttk
from UI.register import Register
from tkinter import PhotoImage, Entry, messagebox, StringVar
from mysql_connection import DatabaseConnection
import mysql.connector
from resources.FileTracker.tracker import resource_path


class AdminHomepage(tk.Canvas):
    def __init__(self, master = None,switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app

        self.dashboardLogo = PhotoImage(file=resource_path("resources/adminhome/dashboardlogo.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/adminhome/dashboardbg.png"))
        self.gradiantBG = PhotoImage(file=resource_path("resources/adminhome/gradiant.png"))
        self.ShapeBg = PhotoImage(file=resource_path("resources/adminhome/shapebg.png"))


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
        

        self.create_text(100.0, 40.0, anchor = "nw", text = "ADMIN", fill="#FFFFFF", font=("Nokora", 17 * -1,"bold"))
        self.create_text(20.0, 110.0, anchor = "nw", text = "NAVIGATION", fill="#FFFFFF", font=("Nokora", 11 * -1,"bold"))
        self.create_line(20.0, 100.0, 200.0, 100.0, fill="#FFFFFF")

        self.create_text(270.0, 50.0, anchor = "nw", text = "Total No Of Applicants", fill="#000000", font=("Nokora", 12 * -1,"bold"))
        self.create_text(470.0, 50.0, anchor = "nw", text = "Philhealth Members", fill="#000000", font=("Nokora", 12 * -1,"bold"))
        self.create_text(680.0, 50.0, anchor = "nw", text = "Dependent", fill="#000000", font=("Nokora", 12 * -1,"bold"))
     
        self.TotalApplicants = StringVar(value="100")
        self.TotalPhilhealth = StringVar(value="80")
        self.DependentlApplicants = StringVar(value="50")

        # Create text items on the canvas
        self.text_id_1 = self.create_text(290.0, 80.0, anchor="nw", text=self.TotalApplicants.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))
        self.text_id_2 = self.create_text(500.0, 80.0, anchor="nw", text=self.TotalPhilhealth.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))
        self.text_id_3 = self.create_text(700.0, 80.0, anchor="nw", text=self.DependentlApplicants.get(), fill="#1B4B77", font=("Nokora", 30, "bold"))



        self.DashboardButton = tk.Button(self, image=self.dashboardButton, borderwidth=0, highlightthickness=0, command=lambda:print("DashBoard"), relief="flat")
        self.DashboardButton.place(x=20.0, y=150.0, width=180.0, height=48.0)

        self.TablesButton = tk.Button(self, image=self.tablesButton, borderwidth=0, highlightthickness=0, command=self.go_to_maintable)

        self.TablesButton.place(x=20.0, y=210.0, width=180.0, height=48.0)


        
        self.ApplicantTableButton = tk.Button(self, image=self.applicantsButton, borderwidth=0, highlightthickness=0, command=self.go_to_applicant, relief="flat")

        
        self.HouseholdTableButton = tk.Button(self, image=self.HouseholdButton, borderwidth=0, highlightthickness=0, command=self.go_to_household, relief="flat")


        self.ReferenceTableButton = tk.Button(self, image=self.ReferenceButton, borderwidth=0, highlightthickness=0, command=self.go_to_reference, relief="flat")
        self.ReferenceTableButton.place(x=40.0, y=340.0, width=140, height=28.0)


        self.LogOutButton = tk.Button(self, image=self.logoutButton, borderwidth=0, highlightthickness=0, command= self.LogOut, relief="flat")
        self.ApplicantTableButton.place(x=40.0, y=270.0, width=140, height=28.0)
        self.HouseholdTableButton.place(x=40.0, y=305.0, width=140, height=28.0)
        self.LogOutButton.place(x=40.0, y=375.0, width=140, height=28.0)

        
        self.TableCanva = tk.Canvas(self, bg="#FFFFFF", height=220, width=540, highlightthickness=0)
        self.TableCanva.place(x=250.0, y=230.0)
        self.columns = (
            "Reference_No", "Applicant_ID", "Date")

        self.Tree = ttk.Treeview(self.TableCanva, columns=self.columns, show='headings', height=10)
        self.Tree.pack_propagate(False) # Prevent the treeview from resizing with the window
        self.Tree.place(x=270,y=110, anchor="center", width=540, height=220)
        self.style = ttk.Style()

        

        self.HScroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.Tree.xview)
        self.HScroll.place(x=520, y=455, anchor="center", width=540,height=10)
        self.Tree.configure(xscrollcommand=self.HScroll.set)

        




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
    
    # def update_text_1(self):
    #     self.itemconfig(self.text_id_1, text=self.TotalApplicants.get())

    # def update_text_2(self):
    #     self.itemconfig(self.text_id_2, text=self.TotalPhilhealth.get())

    # def update_text_3(self):
    #     self.itemconfig(self.text_id_3, text=self.DependentlApplicants.get())



