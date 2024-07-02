
import tkinter as tk
from tkinter import PhotoImage, Entry
from resources.FileTracker.tracker import resource_path

class AdminLogin(tk.Canvas,):
    def __init__ (self, master = None, switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        

        #BUTTON
        self.image_button_1 = PhotoImage(file=resource_path("resources/adminlogin/button_1.png"))

        #ENTRY
        self.image_entry_1 = PhotoImage(file=resource_path("resources/login/entry_1.png"))
        self.image_entry_2 = PhotoImage(file=resource_path("resources/login/entry_1.png"))

        #IMAGES
        self.image_2 = PhotoImage(file=resource_path("resources/login/image_2.png"))
        self.image_3 = PhotoImage(file=resource_path("resources/login/image_3.png"))
        self.image_4 = PhotoImage(file=resource_path("resources/login/image_4.png"))
        self.image_5 = PhotoImage(file=resource_path("resources/login/image_5.png"))
        self.image_8 = PhotoImage(file=resource_path("resources/login/image_8.png"))
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
        self.create_text(531.0, 206.0, anchor = "nw", text = "Email", fill="#000000", font=("Mada Bold", 17 * -1))
        self.create_text(531.0, 262.0, anchor="nw",text="Password",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(160.0, 270.0, anchor="nw",text="Philippine Charity Sweepstakes Office",fill="#000000",font=("Mada Bold", 17 * -1))
        self.create_text(610.0, 62.0, anchor="nw",text="Admin Login",fill="#FFFFFF",font=("Mada Bold", 17 * -1))
        self.create_text(565.0, 94.0, anchor="nw", text = "Enter your admin credentials", fill="#FFFFFF", font=("Mada Light", 14 * -1))
        
        self.Email = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Email.place(x=531.0, y=232.0, width=241.0, height=18.0)

        self.Password = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Password.place(x=531.0, y=286.0, width=241.0, height=18.0)

        self.Button_1 = tk.Button(self, image=self.image_button_1, borderwidth=0, highlightthickness=0, command=self.GoAdminPage ,relief="flat")
        self.Button_1.place(x=532.0, y=358.0, width=234.0, height=29.0)

    def GoAdminPage(self):
            print("GoAdmin called")
            if self.switch_frame:
                print("Switching to adminhomepage...")
                self.switch_frame('adminhomepage')