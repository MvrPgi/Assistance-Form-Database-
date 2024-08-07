
import tkinter as tk
from UI.register import Register
from tkinter import PhotoImage, Entry, messagebox
from mysql_connection import DatabaseConnection
import mysql.connector
from resources.FileTracker.tracker import resource_path


class Login(tk.Canvas):
    def __init__(self, master = None,switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        self.database = DatabaseConnection()


        self.GradiantBg = PhotoImage(file=resource_path("resources/login/landingPagebg.png"))
        #self.welcomText = PhotoImage(file=resource_path("resources/login/WelcomeText.png"))
        self.pcsioText = PhotoImage(file=resource_path("resources/applicantadmin/pcsio_text.png"))
        self.Logo = PhotoImage(file=resource_path("resources/login/Logo.png"))
        self.LogoBg = PhotoImage(file=resource_path("resources/login/loginBg.png"))
        self.TextBoxBG = PhotoImage(file=resource_path("resources/login/textBOX.png"))
        self.loginButtonBG = PhotoImage(file=resource_path("resources/login/blueBG.png"))
        self.loginButtonPic = PhotoImage(file=resource_path("resources/login/loginButton.png"))
        self.SignUpButtonPic = PhotoImage(file=resource_path("resources/login/signupButton.png"))
        self.dontHaveAccount = PhotoImage(file=resource_path("resources/login/dontHave_text.png"))
        self.HomePic = PhotoImage(file=resource_path("resources/login/HomeButton.png"))



        self.create_image(0, 0, image=self.GradiantBg, anchor="nw")
        self.create_image(600.0, 250.0, image=self.LogoBg)
        self.create_image(610.0, 145, image=self.Logo)
        self.create_image(300.0, 250.0, image=self.pcsioText)
        #self.create_image(300.0, 250, image=self.welcomText)
        self.create_image(603.0, 195.0, image=self.TextBoxBG)
        self.create_image(603.0, 240.0, image=self.TextBoxBG)
        self.create_image(603.0, 285.0, image=self.loginButtonBG)

        self.HomeButton = tk.Button(self, image=self.HomePic, command=self.go_to_applicant_admin,borderwidth=0, highlightthickness=0)
        self.HomeButton.place(x=40.0, y=40.0, width=40, height=40)

        self.LoginButton = tk.Button(self, image=self.loginButtonPic, command=self.loginApplicant,borderwidth=0, highlightthickness=0)
        self.LoginButton.place(x=480.0, y=270.0, width=250.0, height=31.0)

        self.create_line(470.0, 320.5, 735.0, 320.5, fill="#000000")
        #self.create_text(510.0, 340.0, anchor="nw", text="Don't have an account?", fill="#000000", font=("Nokora", 12 * -1))
        self.create_image(568.0, 350.0, image=self.dontHaveAccount) 


        self.SignUpButton = tk.Button(self, image=self.SignUpButtonPic, command=self.go_to_signup,borderwidth=0, highlightthickness=0)
        self.SignUpButton.place(x=673.0, y=349.0, anchor="center", width=45, height=13)

        self.Username = Entry(self, font=("Nokora", 10), bd=0, bg="#FFFFFF", highlightthickness=0)
        self.Username.place(x=480.0, y=183.0, width=240.0, height=25.0)
        self.Password = Entry(self, font=("Nokora", 10), bd=0, bg="#FFFFFF", highlightthickness=0,show="•")
        self.Password.place(x=480.0, y=229.0, width=240.0, height=25.0)


  # Create placeholder labels
        self.username_placeholder = tk.Label(self, text="Username", fg="grey", bg="white")
        self.username_placeholder.place(x=485.0, y=185.0)
        self.password_placeholder = tk.Label(self, text="Password", fg="grey", bg="white")
        self.password_placeholder.place(x=485.0, y=230.0)

        # Bind focus in and focus out events
        self.Username.bind("<FocusIn>", self.clear_placeholder)
        self.Username.bind("<FocusOut>", self.show_placeholder)
        self.Password.bind("<FocusIn>", self.clear_placeholder)
        self.Password.bind("<FocusOut>", self.show_placeholder)

        # Initial placeholder check
        self.show_placeholder(None)

    def clear_placeholder(self, event):
        widget = event.widget
        if widget == self.Username:
            self.username_placeholder.place_forget()
        elif widget == self.Password:
            self.password_placeholder.place_forget()

    def show_placeholder(self, event):
        if not self.Username.get():
            self.username_placeholder.place(x=485.0, y=185.0)
        if not self.Password.get():
            self.password_placeholder.place(x=485.0, y=230.0)


    
    def loginApplicant(self):
        username = self.Username.get()
        print(username)
        password = self.Password.get()
        print(password)
        if self.database.loginApplicantData(username, password):
            print("Login successful!")
            self.gotoApplicantHome()

        else:
            messagebox.showerror("Login Error", "Invalid username or password")


    def gotoApplicantHome(self):
        if self.switch_frame:
            self.switch_frame('applicanthomepage')

    def go_to_signup(self):
        if self.switch_frame:
            self.switch_frame('signup')


    def go_to_applicant_admin(self):
        if self.switch_frame:
            self.switch_frame('applicantadmin')





        