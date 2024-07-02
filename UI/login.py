
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

        #BUTTON
        self.image_button_1 = PhotoImage(file=resource_path("resources/login/button_1.png"))
        self.image_button_2 = PhotoImage(file=resource_path("resources/login/button_2.png"))
        #IMAGES
        self.image_1 = PhotoImage(file=resource_path("resources/login/image_1.png"))
        self.image_2 = PhotoImage(file=resource_path("resources/login/image_2.png"))
        self.image_3 = PhotoImage(file=resource_path("resources/login/image_3.png"))
        self.image_4 = PhotoImage(file=resource_path("resources/login/image_4.png"))
        self.image_5 = PhotoImage(file=resource_path("resources/login/image_5.png"))
        self.image_8 = PhotoImage(file=resource_path("resources/login/image_8.png"))
        self.image_9 = PhotoImage(file=resource_path("resources/login/image_9.png"))
        self.image_12 = PhotoImage(file=resource_path("resources/login/image_12.png"))
        self.image_13 = PhotoImage(file=resource_path("resources/adminlogin/image_5.png"))

        self.create_image(50.0, 250.0, image = self.image_2) #Blue Rectangle with Edges
        self.create_image(656.0, 250.0, image = self.image_3) #Pink Rectangle with Edges
        self.create_image(60.0, 250.0, image = self.image_4) # Line Circle
        self.create_image(79.0, 220.0, image = self.image_5) # PCSO Logo
        self.create_image(653.0, 160.0, image = self.image_12) # Blue Rectangle Horizontal
        self.create_image(653.0, 301.0, image = self.image_8)  # White Square
        self.create_image(300.0, 220.0, image = self.image_13) # PCSO Text
        
        
        self.create_text(531.0, 138.0, anchor = "nw", text = "Log In", fill="#FFFFFF", font=("Mada Bold", 17 * -1))
        self.create_text(531.0, 206.0, anchor = "nw", text = "Username", fill="#000000", font=("Mada Bold", 17 * -1))
        self.create_text(531.0, 262.0, anchor="nw",text="Password",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(160.0, 270.0, anchor="nw",text="Philippine Charity Sweepstakes Office",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(600.0, 62.0, anchor="nw",text="Welcome Back!",fill="#FFFFFF",font=("Mada Bold", 17 * -1))
        self.create_text(540.0, 94.0, anchor="nw", text = "Don't have an account yet?", fill="#FFFFFF", font=("Mada Light", 14 * -1))

        self.Username = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Username.place(x=531.0, y=232.0, width=241.0, height=18.0)

        self.Password = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0, show = "•")
        self.Password.place(x=531.0, y=286.0, width=241.0, height=18.0)

        self.Button_1 = tk.Button(self, image=self.image_button_1, borderwidth=0, highlightthickness=0, command= self.go_to_register, relief="flat")
        self.Button_1.place(x=532.0, y=358.0, width=234.0, height=29.0)

        self.Button_2 = tk.Button(self, image=self.image_button_2, borderwidth=0, highlightthickness=0, command=self.go_to_signup, relief ="flat")
        self.Button_2.place(x=715.0, y=90.0)

        self.database = DatabaseConnection()
    
    def login_button(self):
        mysqldb = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "practice")
        mycursor = mysqldb.cursor()

        username = self.Username.get()
        password = self.Password.get()

        mycursor.execute("SELECT username, _password FROM user")
        results = mycursor.fetchall()

        for x in results:
            if username == x[0] and password == x[1]:
                messagebox.showinfo("Login", "Login Successfully.")
                break
        else:
            messagebox.showerror("Login", "Invalid username or email.")


    def go_to_register(self):
        if self.switch_frame:
            self.switch_frame('register')

    def go_to_signup(self):
        if self.switch_frame:
            self.switch_frame('signup')





        