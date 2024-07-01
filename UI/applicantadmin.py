import sys
import os
import tkinter as tk
from tkinter import PhotoImage, Entry
from resources.FileTracker.tracker import resource_path

class ApplicantAdmin(tk.Canvas):
    def __init__ (self, master = None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)

        #BUTTON
        self.image_button_1 = PhotoImage(file=resource_path("resources/applicantadmin/button_1.png"))
        self.image_button_2 = PhotoImage(file=resource_path("resources/applicantadmin/button_2.png"))

        #IMAGES
        self.image_1 = PhotoImage(file=resource_path("resources/applicantadmin/image_1.png")) #PCSO Building Picture
        self.image_2 = PhotoImage(file=resource_path("resources/applicantadmin/image_2.png")) #Black Rectangle Clear
        self.image_3 = PhotoImage(file=resource_path("resources/applicantadmin/image_4.png")) #Dark Blue Rectangle
        self.image_4 = PhotoImage(file=resource_path("resources/applicantadmin/image_5.png")) #PCSO Logo
        self.image_5 = PhotoImage(file=resource_path("resources/applicantadmin/image_7.png")) #White Square
        self.image_6 = PhotoImage(file=resource_path("resources/applicantadmin/image_9.png")) #PCSO Text

        #IMAGES PLACE
        self.create_image(275.0, 250.0, image = self.image_1) #PCSO Building Picture
        self.create_image(265.0, 250.0, image = self.image_2) #Black Rectangle Clear
        self.create_image(670.0, 250.0, image = self.image_3) #Blue Rectangle with Edges
        self.create_image(589.0, 73.0, image = self.image_4) #PCSO Logo
        self.create_image(661.0, 290.0, image = self.image_5) #White Square
        self.create_image(250.0, 220.0, image = self.image_6) #PCSO Text

        #TEXT PLACE
        self.create_text(531.0, 132.0, anchor = "nw", text = "Welcome to our Application!", fill="#FFFFFF", font=("Mada Bold", 21 * -1))
        self.create_text(580.0, 225.0, anchor = "nw", text = "Please click your destination", fill="#000000", font=("Mada SemiBold", 13 * -1)) 
        self.create_text(625.0, 49.0, anchor = "nw", text = "PCSO IMAP\nAPPLICATION", fill="#FFFFFF", font=("Mada Bold", 20 * -1))
        self.create_text(84.0, 273.0, anchor = "nw", text = "Philippine Charity Sweepstakes Office", fill="#FFFFFF", font=("Mada Bold", 19 * -1))

        #BUTTON
        self.Button_1 = tk.Button(self, image=self.image_button_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.Button_1.place(x=535.0, y=315.0, width=248.0, height=39.0)

        self.Button_2 = tk.Button(self, image=self.image_button_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
        self.Button_2.place(x=535.0, y=260.0, width=248.0, height=39.0)




   




