
import tkinter as tk
from tkinter import PhotoImage, Entry, messagebox
from resources.FileTracker.tracker import resource_path
from mysql_connection import DatabaseConnection


class AdminLogin(tk.Canvas,):
    def __init__ (self, master = None, switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        self.database = DatabaseConnection()
        

        self.GradiantBg = PhotoImage(file=resource_path("resources/adminlogin/landingPagebg.png"))
        self.welcomText = PhotoImage(file=resource_path("resources/adminlogin/WelcomeText.png"))
        self.Logo = PhotoImage(file=resource_path("resources/adminlogin/Logo.png"))
        self.LogoBg = PhotoImage(file=resource_path("resources/adminlogin/loginBg.png"))
        self.TextBoxBG = PhotoImage(file=resource_path("resources/adminlogin/textBOX.png"))
        self.loginButtonBG = PhotoImage(file=resource_path("resources/adminlogin/blueBG.png"))
        self.loginButtonPic = PhotoImage(file=resource_path("resources/adminlogin/loginButton.png"))
        self.SignUpButtonPic = PhotoImage(file=resource_path("resources/adminlogin/signupButton.png"))
        self.HomePic = PhotoImage(file=resource_path("resources/adminlogin/HomeButton.png"))
                                     




        self.create_image(0, 0, image=self.GradiantBg, anchor="nw")
        self.create_image(600.0, 250.0, image=self.LogoBg)
        self.create_image(610.0, 145, image=self.Logo)
        self.create_image(300.0, 250, image=self.welcomText)
        self.create_image(603.0, 195.0, image=self.TextBoxBG)
        self.create_image(603.0, 240.0, image=self.TextBoxBG)
        
        self.create_image(603.0, 305.0, image=self.loginButtonBG)

        self.HomeButton = tk.Button(self, image=self.HomePic, command=self.go_to_applicant_admin,borderwidth=0, highlightthickness=0)
        self.HomeButton.place(x=25.0, y=25.0, anchor="center", width=48, height=50)

        self.create_text(475.0, 265.0, anchor="nw", text="Remember Me", fill="#000000", font=("Nokora", 12 * -1))
        self.CheckButton = tk.Checkbutton(self, bg="#FFFFFF", activebackground="#FFFFFF", selectcolor="#FFFFFF")
        self.CheckButton.place(x=560.0, y=263.0, width=20.0, height=20.0)

        self.LoginButton = tk.Button(self, image=self.loginButtonPic, command=self.loginAdmin,borderwidth=0, highlightthickness=0)
        self.LoginButton.place(x=480.0, y=290.0, width=250.0, height=31.0)


        self.UserName = Entry(self, font=("Nokora", 10), bd=0, bg="#FFFFFF", highlightthickness=0)
        self.UserName.place(x=480.0, y=183.0, width=240.0, height=25.0)
        self.Password = Entry(self, font=("Nokora", 10), bd=0, bg="#FFFFFF", highlightthickness=0,show="•")
        self.Password.place(x=480.0, y=229.0, width=240.0, height=25.0)


        self.username_placeholder = tk.Label(self, text="Username", fg="grey", bg="white")
        self.username_placeholder.place(x=485.0, y=185.0)
        self.password_placeholder = tk.Label(self, text="Password", fg="grey", bg="white")
        self.password_placeholder.place(x=485.0, y=230.0)

        # Bind focus in and focus out events
        self.UserName.bind("<FocusIn>", self.clear_placeholder)
        self.UserName.bind("<FocusOut>", self.show_placeholder)
        self.Password.bind("<FocusIn>", self.clear_placeholder)
        self.Password.bind("<FocusOut>", self.show_placeholder)


        self.show_placeholder(None)

    def clear_placeholder(self, event):
        widget = event.widget
        if widget == self.UserName:
            self.username_placeholder.place_forget()
        elif widget == self.Password:
            self.password_placeholder.place_forget()

    def show_placeholder(self, event):
        if not self.UserName.get():
            self.username_placeholder.place(x=485.0, y=185.0)
        if not self.Password.get():
            self.password_placeholder.place(x=485.0, y=230.0)

    def loginAdmin(self):
        username = self.UserName.get()
        print(username)
        password = self.Password.get()
        print(password)
        if self.database.loginAdminData(username, password):
            print("Login successful!")
            self.GoAdminPage()

        else:
            messagebox.showerror("Login Error", "Invalid username or password")






    def GoAdminPage(self):
            print("GoAdmin called")
            if self.switch_frame:
                print("Switching to adminhomepage...")
                self.switch_frame('adminhomepage')


    def go_to_applicant_admin(self):
        if self.switch_frame:
            self.switch_frame('applicantadmin')