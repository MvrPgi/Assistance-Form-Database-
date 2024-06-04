import sys
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox, Entry
from PIL import Image, ImageTk 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Main App")
        self.geometry("820x500") 
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")
        

        self.register = Register(self)
        self.register.place(x=0, y=0)

class Register(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)



        #CREATE THE TEXTS
        
        self.create_text(49.0, 100.0, anchor="nw", text="Reference No:", fill="#000000", font=("Mada Regular", 10 * -1))
        self.create_text(289.0, 100,anchor ="nw", text="Date:",fill="#000000",font=("Mada Regular", 10 * -1))
        ############################
        self.create_text(49.0,172.0,anchor ="nw", text="Full Name Of The Patient    ",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(87.0,203.0,anchor ="nw", text="Surname",fill="#000000",font=("Mada Regular", 8 * -1))   
        self.create_text(385., 205,anchor ="nw", text="First Name", fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(691.0,204,anchor ="nw", text="Middle Name",fill="#000000",font=("Mada Regular", 8 * -1))
        ############################
        self.create_text(49.0, 219.0,anchor ="nw", text="Permanent Address",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(87.0, 250.0,anchor ="nw", text="No",fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(120.0, 250.0,anchor ="nw", text="Street",fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(180.0, 250.0,anchor ="nw", text="Barangay",fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(320.0, 250.0,anchor ="nw", text="Municipality/City",fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(500.0, 250.0,anchor ="nw", text="Province",fill="#000000",font=("Mada Regular", 8 * -1))
        self.create_text(700, 250.0,anchor ="nw", text="Region",fill="#000000",font=("Mada Regular", 8 * -1))
        ############################
        self.create_text(49.0, 265.0,anchor ="nw", text="Civil Status",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(49.0, 290.0,anchor ="nw", text="Birthdate:",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(230.0, 290.0,anchor ="nw", text="Age:",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(49.0, 321.5,anchor ="nw", text = "Nationality",fill="#000000",font=("Mada Regular", 10 * -1))
        self.create_text(230.0, 321.5,anchor ="nw", text = "Religion",fill="#000000",font=("Mada Regular", 10 * -1))

        #LOAD THE IMAGES
        self.image_image_1 = PhotoImage(file=resource_path("resources/APP_1/image_1.png"))  
        self.image_entry_3 = PhotoImage(file=resource_path("resources/APP_1/entry_3.png"))
        self.image_entry_5 = PhotoImage(file=resource_path("resources/APP_1/entry_5.png"))
        self.image_image_6 = PhotoImage(file=resource_path("resources/APP_1/image_6.png"))
        self.image_entry_11 = PhotoImage(file=resource_path("resources/APP_1/entry_11.png"))
       

        #PLACE THE IMAGES
        self.create_image(415.0, 46.0, image=self.image_image_1)
        self.create_image(120.0, 150.5, image=self.image_image_6)
        self.create_image(409.0, 190.5, image=self.image_entry_3)
        self.create_image(409.0, 237.5, image=self.image_entry_3)
        self.create_image(397.0, 120.5, image=self.image_entry_11)
        self.create_image(155.5, 120.5, image=self.image_entry_11)
        self.create_image(120.5, 310.5, image=self.image_entry_5)
        self.create_image(298.5, 310.5, image=self.image_entry_5)   
        self.create_image(120.5, 340.5, image=self.image_entry_5)
        self.create_image(298.5, 340.5, image=self.image_entry_5)
  
        


    # Creating and placing the entry widget

        self.Reference_No = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Reference_No.place(  
        x=50.0,
        y=115.5,
        width=210.0,
        height=10.0
)
        self.Date = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Date.place(
        x=290.0,
        y=115.5,
        width=208.0,
        height=10.0
)
        self.FullName = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.FullName.place(
        x=53.0,
        y=185.5,
        width=712.0,
        height=10.0
)

        self.Permanent_Address = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Permanent_Address.place(
        x = 52.0,
        y = 232.5,
        width=716.0,
        height=10.0
)
        self.Birthdate = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)       
        self.Birthdate.place(
        x=52.0,
        y=305.5,
        width=142.0,
        height=10.0
)   
        self.Age = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Age.place(
        x=230.0,
        y=305.5,
        width=140.0,
        height=10.0
)
        self.Nationality = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Nationality.place(
        x=52.0,
        y=335.5,
        width=142.0,
        height=10.0
)











if __name__ == "__main__":
    app = App()
    app.mainloop()
