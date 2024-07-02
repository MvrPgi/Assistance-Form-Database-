
import tkinter as tk
from UI.register import Register
from tkinter import PhotoImage, Entry, messagebox
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


        self.dashboardButton = PhotoImage(file=resource_path("resources/adminhome/dashboardButton.png"))
        self.tablesButton = PhotoImage(file=resource_path("resources/adminhome/tables.png"))
        self.profileButton = PhotoImage(file=resource_path("resources/adminhome/profile.png"))


        self.create_image(410.0, 250.0, image = self.gradiantBG) 
        self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(100.0, 250.0, image = self.dashboardBG)
        self.create_image(50.0, 60.0, image = self.dashboardLogo)

        self.create_text(100.0, 40.0, anchor = "nw", text = "ADMIN", fill="#FFFFFF", font=("Nokora", 17 * -1,"bold"))
        self.create_text(20.0, 110.0, anchor = "nw", text = "NAVIGATION", fill="#FFFFFF", font=("Nokora", 11 * -1,"bold"))
        self.create_line(20.0, 100.0, 200.0, 100.0, fill="#FFFFFF")






        self.DashboardButton = tk.Button(self, image=self.dashboardButton, borderwidth=0, highlightthickness=0, command=lambda:print("DashBoard"), relief="flat")
        self.DashboardButton.place(x=20.0, y=150.0, width=180.0, height=48.0)

        self.TablesButton = tk.Button(self, image=self.tablesButton, borderwidth=0, highlightthickness=0, command=self.go_to_maintable)

        self.TablesButton.place(x=20.0, y=210.0, width=180.0, height=48.0)


    def go_to_maintable(self):
        print("Go to maintable")
        if self.switch_frame:
            print("Switching to adminbench...")
            self.switch_frame('adminbench')



