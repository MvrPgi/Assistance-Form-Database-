import sys
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox, Entry


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class Register(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)



        #LOAD THE IMAGES
        self.image_image_1 = PhotoImage(file=resource_path("resources/APP_1/image_1.png"))  
        self.image_entry_3 = PhotoImage(file=resource_path("resources/APP_1/entry_3.png"))
        self.image_entry_5 = PhotoImage(file=resource_path("resources/APP_1/entry_5.png"))
        self.image_image_6 = PhotoImage(file=resource_path("resources/APP_1/image_6.png"))
        self.image_entry_11 = PhotoImage(file=resource_path("resources/APP_1/entry_11.png"))
        self.image_entry_12 = PhotoImage(file=resource_path("resources/APP_1/entry_12.png"))    
        self.image_entry_9 = PhotoImage(file=resource_path("resources/APP_1/entry_9.png"))
        self.image_entry_16 = PhotoImage(file=resource_path("resources/APP_1/entry_16.png"))
        self.button_image_1 = PhotoImage(file=resource_path("resources/APP_1/button_1.png"))
       
        
        #BACKGROUND IMAGE
        self.create_image(120.0, 150.5, image=self.image_image_6)
        self.create_image(405.0, 46.0, image=self.image_image_1)

        #ENTRY IMAGES
        self.pageImage1_id = [] # Store the image ids to hide them later
        self.pageImage1_id.append(self.create_image(409.0, 190.5, image=self.image_entry_3))
        self.pageImage1_id.append(self.create_image(409.0, 237.5, image=self.image_entry_3))
        self.pageImage1_id.append(self.create_image(397.0, 120.5, image=self.image_entry_11))
        self.pageImage1_id.append(self.create_image(155.5, 120.5, image=self.image_entry_11))
        self.pageImage1_id.append(self.create_image(120.5, 310.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(298.5, 310.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(120.5, 340.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(298.5, 340.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(490.5, 342.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(120.5, 410.5, image=self.image_entry_5))
        self.pageImage1_id.append(self.create_image(280.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(472.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(612.5, 410.5, image=self.image_entry_16))
        self.pageImage1_id.append(self.create_image(750.5, 410.5, image=self.image_entry_16))      

        
        #CREATE THE TEXTS OF FIRST PAGE
        self.PageText1_id = []     
        self.PageText1_id.append(self.create_text(49.0, 100.0, anchor="nw", text="Reference No:", fill="#000000", font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(289.0, 100,anchor ="nw", text="Date:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0,172.0,anchor ="nw", text="Full Name Of The Patient    ",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(87.0,203.0,anchor ="nw", text="Surname",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(385., 205,anchor ="nw", text="First Name", fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(691.0,204,anchor ="nw", text="Middle Name",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 219.0,anchor ="nw", text="Permanent Address",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(87.0, 250.0,anchor ="nw", text="No",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(120.0, 250.0,anchor ="nw", text="Street",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(180.0, 250.0,anchor ="nw", text="Barangay",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(320.0, 250.0,anchor ="nw", text="Municipality/City",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(500.0, 250.0,anchor ="nw", text="Province",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(700, 250.0,anchor ="nw", text="Region",fill="#000000",font=("Mada Regular", 8 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 265.0,anchor ="nw", text="Civil Status",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 290.0,anchor ="nw", text="Birthdate:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 290.0,anchor ="nw", text="Age:",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 290.0,anchor ="nw", text = "Sex",fill="#000000",font=("Mada Regular", 10 * -1)))      
        self.PageText1_id.append(self.create_text(49.0, 321.5,anchor ="nw", text = "Nationality",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 321.5,anchor ="nw", text = "Religion",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 353, anchor ="nw", text = "Highest Educational Attainment",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 321, anchor ="nw", text = "Occupation",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(650.0, 321, anchor ="nw", text = "Membership",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(49.0, 390, anchor ="nw", text = "Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(227.0, 390, anchor ="nw", text = "Other Sources Of Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(420.0, 390, anchor ="nw", text = "Monthly Expenditure",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(559.0, 390, anchor ="nw", text = "Gross Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
        self.PageText1_id.append(self.create_text(700.0, 390, anchor ="nw", text = "Net Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))

                

    # Creating and placing the entry widget of the first page
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
        self.Religion = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Religion.place(
        x=230.0,
        y=335.5,
        width=142.0,
        height=10.0
)
        self.Occupation = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Occupation.place(
        x=420.0,
        y=335.5,
        width=142.0,
        height=10.0
)

        self.Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Monthly_Income.place(
        x=52.0,
        y=405.5,
        width=110.0,
        height=10.0
)
        self.Other_Sources_Of_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Other_Sources_Of_Income.place(
        x=230.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Monthly_Expenditure = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Monthly_Expenditure.place(
        x=420.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Gross_Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Gross_Monthly_Income.place(
        x=559.0,
        y=405.5,
        width=105.0,
        height=10.0
)
        self.Net_Monthly_Income = Entry(
        bd=0,
        bg="#FFE5AB",
        fg="#000716",
        highlightthickness=0
)
        self.Net_Monthly_Income.place(
        x=700.0,
        y=405.5,
        width=105.0,
        height=10.0
)

        # Creating and placing the button widget
        self.button_1 = tk.Button(
        image=self.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command = self.hide
      
)
        self.button_1.place(
        x=405.0,
        y=450.0,
        width=100.0,
        height=30.0
)
        self.button_2 = tk.Button(
        image=self.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command = self.show
)   
        self.button_2.place(
        x=505.0,
        y=450.0,
        width=100.0,
        height=30.0
)
# 2ND PAGE
            
# HIDE THE WIDGETS
    def hide(self):
            for image_id in self.pageImage1_id:
                self.itemconfigure(image_id, state="hidden")
            for text_id in self.PageText1_id:
                self.itemconfigure(text_id, state="hidden")
            self.Reference_No.place_forget()
            self.Date.place_forget()
            self.FullName.place_forget()
            self.Permanent_Address.place_forget()
            self.Birthdate.place_forget()
            self.Age.place_forget()
            self.Nationality.place_forget()
            self.Religion.place_forget()
            self.Occupation.place_forget()
            self.Monthly_Income.place_forget()
            self.Other_Sources_Of_Income.place_forget()
            self.Monthly_Expenditure.place_forget()
            self.Gross_Monthly_Income.place_forget()
            self.Net_Monthly_Income.place_forget()
            self.button_1.place_forget()

    
# SHOW THE WIDGETS
    def show(self):
        for image_id in self.pageImage1_id:
            self.itemconfigure(image_id, state="normal")
        for text_id in self.PageText1_id:
            self.itemconfigure(text_id, state="normal")
            self.Reference_No.place()
            self.Date.place()
            self.FullName.place()
            self.Permanent_Address.place()
            self.Birthdate.place()
            self.Age.place()
            self.Nationality.place()
            self.Religion.place()
            self.Occupation.place()
            self.Monthly_Income.place()
            self.Other_Sources_Of_Income.place()
            self.Monthly_Expenditure.place()
            self.Gross_Monthly_Income.place()
            self.Net_Monthly_Income.place()     
     





            

        
       

    
