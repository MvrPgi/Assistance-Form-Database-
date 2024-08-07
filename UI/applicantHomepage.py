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
        self.database = DatabaseConnection()



        
        self.dashboardLogo = PhotoImage(file=resource_path("resources/applicanthome/dashboardlogo.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/applicanthome/dashboardbg.png"))
        self.gradiantBG = PhotoImage(file=resource_path("resources/applicanthome/gradiant.png"))
        self.dashboardBG = PhotoImage(file=resource_path("resources/applicanthome/dashboardbg.png"))
        self.ButtonBG = PhotoImage(file=resource_path("resources/applicanthome/buttonBG.png"))
        self.HomeText = PhotoImage(file=resource_path("resources/applicanthome/Welcome.png"))
        self.GetStartedButtonPic = PhotoImage(file=resource_path("resources/applicanthome/GetStartedButton.png"))
        self.GetStartedButtonBG = PhotoImage(file=resource_path("resources/applicanthome/GetStartedButtonBG.png"))
        self.UserImageText = PhotoImage(file=resource_path("resources/applicanthome/UserProfileImage.png"))
        self.UserProfileLogo = PhotoImage(file=resource_path("resources/applicanthome/UserProfileLogo.png"))




        self.create_image(410.0, 250.0, image = self.gradiantBG) 
        self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(50.0, 60.0, image = self.dashboardLogo)

        self.text_item = self.create_text(100.0, 40.0, anchor="nw", text="", fill="#FFFFFF", font=("Nokora", 17 * -1, "bold"))
        self.UpdateUserName()


        self.create_text(20.0, 110.0, anchor = "nw", text = "NAVIGATION", fill="#FFFFFF", font=("Nokora", 11 * -1,"bold"))
        self.create_line(20.0, 100.0, 200.0, 100.0, fill="#FFFFFF")


        self.DashBoardButtonPic = PhotoImage(file=resource_path("resources/applicanthome/dashboardButton.png"))
        self.RegisterButtonPic = PhotoImage(file=resource_path("resources/applicanthome/RegisterButton.png"))
        self.ProfileButtonPic = PhotoImage(file=resource_path("resources/applicanthome/ProfileButton.png"))
        self.LogoutButtonPic = PhotoImage(file=resource_path("resources/applicanthome/LogoutButton.png"))
        self.StatusButtonPic = PhotoImage(file=resource_path("resources/applicanthome/StatusButton.png"))


        self.create_image(100.0, 165.0, image = self.ButtonBG)
        self.DashBoardButton = tk.Button(self, image=self.DashBoardButtonPic, borderwidth=0, highlightthickness=0, command=self.GetStarted, relief="flat")
        self.DashBoardButton.place(x=20.0, y=150.0, width=160.0, height=28.0)

        self.create_image(100.0, 215.0, image = self.ButtonBG)
        self.RegisterButton = tk.Button(self, image=self.RegisterButtonPic, borderwidth=0, highlightthickness=0, command=self.Register, relief="flat")
        self.RegisterButton.place(x=20.0, y=200.0, width=160.0, height=28.0)

        self.create_image(100.0, 265.0, image = self.ButtonBG)
        self.ProfileButton = tk.Button(self, image=self.ProfileButtonPic, borderwidth=0, highlightthickness=0, command=self.ApplicantAccount, relief="flat")
        self.ProfileButton.place(x=20.0, y=250.0, width=160.0, height=28.0)


        self.create_image(100.0, 315.0, image = self.ButtonBG)
        self.StatusButton = tk.Button(self, image=self.StatusButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("Status"), relief="flat")
        self.StatusButton.place(x=20.0, y=300.0, width=160.0, height=28.0)


        self.create_image(100.0, 365.0, image = self.ButtonBG)
        self.LogoutButton = tk.Button(self, image=self.LogoutButtonPic, borderwidth=0, highlightthickness=0, command=self.LogOut, relief="flat")
        self.LogoutButton.place(x=20.0, y=350.0, width=160.0, height=28.0)
        


        self.ApplicantAccountID =[]
        self.ApplicantAccountID.append(self.create_image(350.0, 50.0, image = self.UserImageText, state ="hidden"))

        self.ApplicantAccountID.append(self.create_text(260.0, 120.0, anchor = "nw", text = "User Name", fill="#000000", font=("Nokora", 17 * -1,"bold"), state ="hidden"))
        self.UserName = Entry(self, font=("Nokora", 17 * -1,"bold"),state='normal')
     
        self.ApplicantAccountID.append(self.create_text(260.0, 190.0, anchor = "nw", text = "Full Name", fill="#000000", font=("Nokora", 17 * -1,"bold"), state ="hidden"))
        self.FullName = Entry(self, font=("Nokora", 17 * -1,"bold"),state='normal')
        self.ApplicantAccountID.append(self.create_text(260.0, 255.0, anchor = "nw", text = "Password", fill="#000000", font=("Nokora", 17 * -1,"bold"), state ="hidden"))
        self.Password = Entry(self, font=("Nokora", 17 * -1,"bold"),state='normal')


        self.GetStartedID = []
        self.GetStartedID.append(self.create_image(520.0, 250.0, image = self.HomeText, state ="hidden"))
        self.GetStartedID.append(self.create_image(520.0, 380.0, image = self.GetStartedButtonBG,state ="hidden"))
        self.GetStartedButton = tk.Button(self, image=self.GetStartedButtonPic, borderwidth=0, highlightthickness=0, command=lambda:print("Get Started"), relief="flat")

        self.GetStarted()

    def GetStarted(self):
        for getstarted in self.GetStartedID:
            self.itemconfigure(getstarted, state="normal")


        for account in self.ApplicantAccountID:
            self.itemconfigure(account, state="hidden")


        self.GetStartedButton.place(x=320.0, y=361.0, width=400.0, height=30.0)

        self.UserName.place(x=260.0, y=150.0, width=400.0, height=30.0)
        self.FullName.place(x=260.0, y=215.0, width=400.0, height=30.0)
        self.Password.place(x=260.0, y=280.0, width=400.0, height=30.0)


        self.FullName.place_forget()
        self.UserName.place_forget()
        self.Password.place_forget()


    def ApplicantAccount(self):

        try:
            for getstarted in self.GetStartedID:
                self.itemconfigure(getstarted, state="hidden")


            for account in self.ApplicantAccountID:
                self.itemconfigure(account, state="normal")

            self.UserName.place(x=260.0, y=150.0, width=400.0, height=30.0)
            self.FullName.place(x=260.0, y=215.0, width=400.0, height=30.0)
            self.Password.place(x=260.0, y=280.0, width=400.0, height=30.0)
            
            self.GetStartedButton.place(x=320.0, y=361.0, width=400.0, height=30.0)
            self.GetStartedButton.place_forget()

            rows = self.database.GetApplicantLoginDetails()
     
            self.UserName.delete(0, tk.END)
            self.FullName.delete(0, tk.END)
            self.Password.delete(0, tk.END)
            self.UserName.insert(0, rows[0][1])
            self.FullName.insert(0, rows[0][0])
            self.Password.insert(0, rows[0][2])
            self.UserName.config(state='readonly')
            self.FullName.config(state='readonly')
            self.Password.config(state='readonly')
 

        except:
            print("Applicant ID not found")



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


    def UpdateUserName(self):
        username = self.GetUserName()
        if username:
            self.itemconfig(self.text_item, text=username)

    def GetUserName(self):
        username = self.database.GetLastApplicantEntry()
        print(username)
        self.database.close_connection()
        return username
    
