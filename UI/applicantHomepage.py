import tkinter as tk
from tkinter import ttk
from UI.register import Register
from tkinter import PhotoImage, Entry, messagebox, StringVar
from mysql_connection import DatabaseConnection
import mysql.connector
from resources.FileTracker.tracker import resource_path


class ApplicantHomepage(tk.Canvas):
    def __init__(self, master = None,switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app



        
        self.dashboardLogo = PhotoImage(file=resource_path("resources/applicanthome/dashboardlogo.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/applicanthome/dashboardbg.png"))
        self.gradiantBG = PhotoImage(file=resource_path("resources/applicanthome/gradiant.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/applicanthome/dashboardbg.png"))
        self.ButtonBG = PhotoImage(file=resource_path("resources/applicanthome/buttonBG.png"))
        self.HomeText = PhotoImage(file=resource_path("resources/applicanthome/Welcome.png"))
        self.GetStartedButtonPic = PhotoImage(file=resource_path("resources/applicanthome/GetStartedButton.png"))
        self.GetStartedButtonBG = PhotoImage(file=resource_path("resources/applicanthome/GetStartedButtonBG.png"))




        self.create_image(410.0, 250.0, image = self.gradiantBG) 
        self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(50.0, 60.0, image = self.dashboardLogo)
        self.create_image(520.0, 250.0, image = self.HomeText)
        self.create_image(520.0, 380.0, image = self.GetStartedButtonBG)



        self.create_text(100.0, 40.0, anchor = "nw", text = "USER", fill="#FFFFFF", font=("Nokora", 17 * -1,"bold"))
        self.create_text(20.0, 110.0, anchor = "nw", text = "NAVIGATION", fill="#FFFFFF", font=("Nokora", 11 * -1,"bold"))
        self.create_line(20.0, 100.0, 200.0, 100.0, fill="#FFFFFF")


        self.DashBoardButtonPic = PhotoImage(file=resource_path("resources/applicanthome/DashBoardButton.png"))
        self.RegisterButtonPic = PhotoImage(file=resource_path("resources/applicanthome/RegisterButton.png"))
        self.ProfileButtonPic = PhotoImage(file=resource_path("resources/applicanthome/ProfileButton.png"))
        self.LogoutButtonPic = PhotoImage(file=resource_path("resources/applicanthome/LogoutButton.png"))
        self.StatusButtonPic = PhotoImage(file=resource_path("resources/applicanthome/StatusButton.png"))


        self.create_image(100.0, 165.0, image = self.ButtonBG)
        self.DashBoardButton = tk.Button(self, image=self.DashBoardButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("DashBoard"), relief="flat")
        self.DashBoardButton.place(x=20.0, y=150.0, width=160.0, height=28.0)

        self.create_image(100.0, 215.0, image = self.ButtonBG)
        self.RegisterButton = tk.Button(self, image=self.RegisterButtonPic, borderwidth=0, highlightthickness=0, command=self.Register, relief="flat")
        self.RegisterButton.place(x=20.0, y=200.0, width=160.0, height=28.0)

        self.create_image(100.0, 265.0, image = self.ButtonBG)
        self.ProfileButton = tk.Button(self, image=self.ProfileButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("Profile"), relief="flat")
        self.ProfileButton.place(x=20.0, y=250.0, width=160.0, height=28.0)


        self.create_image(100.0, 315.0, image = self.ButtonBG)
        self.StatusButton = tk.Button(self, image=self.StatusButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("Status"), relief="flat")
        self.StatusButton.place(x=20.0, y=300.0, width=160.0, height=28.0)


        self.create_image(100.0, 365.0, image = self.ButtonBG)
        self.LogoutButton = tk.Button(self, image=self.LogoutButtonPic, borderwidth=0, highlightthickness=0, command=self.LogOut, relief="flat")
        self.LogoutButton.place(x=20.0, y=350.0, width=160.0, height=28.0)

        self.GetStartedButton = tk.Button(self, image=self.GetStartedButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("Get Started"), relief="flat")
        self.GetStartedButton.place(x=320.0, y=361.0, width=400.0, height=30.0)



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


    def Register(self):
        print("Register")
        if self.switch_frame:
            self.switch_frame('register')