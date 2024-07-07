import sys
import os
import tkinter as tk
from tkinter import PhotoImage, Entry
from mysql_connection import DatabaseConnection
from resources.FileTracker.tracker import resource_path

class Signup(tk.Canvas):
    def __init__ (self, master = None,switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        self.database = DatabaseConnection()

        self.GradiantBg = PhotoImage(file=resource_path("resources/signup/landingPagebg.png"))
        self.welcomText = PhotoImage(file=resource_path("resources/signup/WelcomeText.png"))
        self.loginBg = PhotoImage(file=resource_path("resources/signup/loginBG.png"))
        self.Logo = PhotoImage(file=resource_path("resources/signup/Logo.png"))
        self.signUPButtonPic = PhotoImage(file=resource_path("resources/signup/signupButton.png"))
        self.signUpBG = PhotoImage(file=resource_path("resources/signup/signupBG.png"))
        self.entryBg = PhotoImage(file=resource_path("resources/signup/textBOX.png"))
        self.signuploginButton = PhotoImage(file=resource_path("resources/signup/loginButton.png"))


        self.create_image(410.0, 250.0, image=self.GradiantBg)
        self.create_image(300.0, 250, image=self.welcomText)
        self.create_image(600.0, 250.0, image=self.loginBg)
        self.create_image(610.0, 120.0, image=self.Logo)
        self.create_image(603.0, 170.0, image=self.entryBg)
        self.create_image(603.0, 210.0, image=self.entryBg)
        self.create_image(603.0, 250.0, image=self.entryBg)
        self.create_image(603.0, 300.0, image=self.signUpBG)

        self.signUPButton = tk.Button(self, image=self.signUPButtonPic, command=self.signup,borderwidth=0, highlightthickness=0,)
        self.signUPButton.place(x=603.0, y=300.0, anchor="center", width=220, height=25)

        self.create_line(470.0, 337.5, 735.0, 337.5, fill="#000000")
        self.create_text(470.0, 340.0, anchor="nw", text="Already have an account?", fill="#000000", font=("Nokora", 12 * -1))
        self.LoginButton = tk.Button(self, image=self.signuploginButton, command=self.go_to_login,borderwidth=0, highlightthickness=0)
        self.LoginButton.place(x=630.0, y=348.0, anchor="center", width=45, height=18)

        self.Username = Entry(self, bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0)
        self.Username.place(x=480.0, y=160.0, width=240.0, height=25.0)
        self.Fullname = Entry(self, bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0)
        self.Fullname.place(x=480.0, y=200.0, width=240.0, height=25.0)
        self.Password = Entry(self, bd=0, bg="#FFFFFF", fg="#000000", highlightthickness=0, show="•")
        self.Password.place(x=480.0, y=240.0, width=240.0, height=25.0)




        # Create placeholder labels
        self.username_placeholder = tk.Label(self, text="Username", fg="grey", bg="white")
        self.username_placeholder.place(x=485.0, y=160.0)
        self.fullname_placeholder = tk.Label(self, text="Full Name", fg="grey", bg="white")
        self.fullname_placeholder.place(x=485.0, y=200.0)
        self.password_placeholder = tk.Label(self, text="Password", fg="grey", bg="white")
        self.password_placeholder.place(x=485.0, y=240.0)

        # Bind focus in and focus out events
        self.Username.bind("<FocusIn>", self.clear_placeholder)
        self.Username.bind("<FocusOut>", self.show_placeholder)
        self.Fullname.bind("<FocusIn>", self.clear_placeholder)
        self.Fullname.bind("<FocusOut>", self.show_placeholder)
        self.Password.bind("<FocusIn>", self.clear_placeholder)
        self.Password.bind("<FocusOut>", self.show_placeholder)

        # Initial placeholder check
        self.show_placeholder(None)

    def clear_placeholder(self, event):
        widget = event.widget
        if widget == self.Username:
            self.username_placeholder.place_forget()
        elif widget == self.Fullname:
            self.fullname_placeholder.place_forget()
        elif widget == self.Password:
            self.password_placeholder.place_forget()

    def show_placeholder(self, event):
        if not self.Username.get():
            self.username_placeholder.place(x=485.0, y=160.0)
        if not self.Fullname.get():
            self.fullname_placeholder.place(x=485.0, y=200.0)
        if not self.Password.get():
            self.password_placeholder.place(x=485.0, y=240.0)

    def signup(self):
        print("Signup button clicked")
        username = self.Username.get()
        fullname = self.Fullname.get()
        password = self.Password.get()

        if not username or not fullname or not password:
            print("Please fill in all fields.")
            return

        # Check if username already exists
        if self.database.check_username_exists(username):
            print("Username already exists.")
            return

        # Insert new user into database
        self.database.signup(fullname,username, password)
        print("User inserted into database.")
        self.go_to_login()


 


    def go_to_login(self):
        print("Login button clicked")
        if self.switch_frame:
            self.switch_frame('login')
