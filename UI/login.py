import sys
import os
import tkinter as tk
from tkinter import PhotoImage, Entry
from resources.FileTracker.tracker import resource_path


class Login(tk.Canvas):
    def __init__(self, master = None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)

        #BUTTOn
        self.image_button_1 = PhotoImage(file=resource_path("resources/login/button_1.png"))
        
        #ENTRY
        self.image_entry_1 = PhotoImage(file=resource_path("resources/login/entry_1.png"))
        self.image_entry_2 = PhotoImage(file=resource_path("resources/login/entry_2.png"))

        #IMAGES
        self.image_1 = PhotoImage(file=resource_path("resources/login/image_1.png"))
        self.image_2 = PhotoImage(file=resource_path("resources/login/image_2.png"))
        self.image_3 = PhotoImage(file=resource_path("resources/login/image_3.png"))
        self.image_4 = PhotoImage(file=resource_path("resources/login/image_4.png"))
        self.image_5 = PhotoImage(file=resource_path("resources/login/image_5.png"))
        self.image_7 = PhotoImage(file=resource_path("resources/login/image_7.png"))
        self.image_8 = PhotoImage(file=resource_path("resources/login/image_8.png"))
        self.image_9 = PhotoImage(file=resource_path("resources/login/image_9.png"))
        self.image_12 = PhotoImage(file=resource_path("resources/login/image_12.png"))

        self.create_image(50.0, 250.0, image = self.image_2) #Blue Rectangle with Edges
        self.create_image(656.0, 250.0, image = self.image_3) #Pink Rectangle with Edges
        self.create_image(60.0, 250.0, image = self.image_4) # Line Circle
        self.create_image(79.0, 220.0, image = self.image_5) # PCSO Logo
        self.create_image(653.0, 160.0, image = self.image_12) # Blue Rectangle Horizontal
        self.create_image(653.0, 301.0, image = self.image_8)  # White Square
        
        self.create_text(134.0, 145.0, anchor = "nw", text = "PCSO", fill="#2065A5", font=("Mada Bold", 120 * -1, "bold"))
        self.create_text(531.0, 138.0, anchor = "nw", text = "Log In", fill="#FFFFFF", font=("Mada Bold", 17 * -1))
        self.create_text(531.0, 206.0, anchor = "nw", text = "Email", fill="#000000", font=("Mada Bold", 17 * -1))
        self.create_text(531.0, 262.0, anchor="nw",text="Password",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(160.0, 270.0, anchor="nw",text="Philippine Charity Sweepstakes Office",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(600.0, 62.0, anchor="nw",text="Welcome Back!",fill="#FFFFFF",font=("Mada Bold", 17 * -1))

        self.Email = Entry(bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Email.place(x=531.0, y=232.0, width=241.0, height=18.0)

        self.Password = Entry(bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Password.place(x=531.0, y=286.0, width=241.0, height=18.0)

        self.Button_1 = tk.Button(self, image=self.image_button_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.Button_1.place(x=532.0, y=358.0, width=234.0, height=29.0)

    # 6 10 Text
    # 11 Remove
        


        