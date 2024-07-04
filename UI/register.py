from resources.FileTracker.tracker import resource_path
import tkinter as tk
from tkinter import PhotoImage, messagebox, Entry, Radiobutton
import mysql.connector as mysql
from mysql_connection import DatabaseConnection



class Register(tk.Canvas):
    
    def __init__(self, master=None, switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.applicant_details = DatabaseConnection() # Create an instance of the Applicant_Details class
        self.ReferenceHandle = DatabaseConnection()
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        
        # LOADING IMAGES
        self.applicantInfo = PhotoImage(file=resource_path("resources/register1/applicant_info.png"))
        self.blueHeader = PhotoImage(file=resource_path("resources/register1/header_bg.png"))
        self.pcsoLogo = PhotoImage(file=resource_path("resources/register1/pcso_logo.png"))
        self.whiteBG = PhotoImage(file=resource_path("resources/register1/white_bg.png"))
        self.gradiantBG = PhotoImage(file=resource_path("resources/adminhome/gradiant.png"))
        self.pcsoText = PhotoImage(file=resource_path("resources/register1/pcso_imap.png"))
        


        # LOADING ENTRY
        self.referenceEntry = PhotoImage(file=resource_path("resources/register1/reference_no.png"))
        self.entry1 = PhotoImage(file=resource_path("resources/register1/date_age.png"))
        self.entry2 = PhotoImage(file=resource_path("resources/register1/name_address.png"))
        self.entry3 = PhotoImage(file=resource_path("resources/register1/entries_all.png"))



        # LOADING BUTTONS
        self.button1 = PhotoImage(file=resource_path("resources/register1/button_1.png"))
        self.button2 = PhotoImage(file=resource_path("resources/register1/home_button.png"))



        # LOADING TEXT IMAGE
        self.appstatus_text = PhotoImage(file=resource_path("resources/register1/appstatus_text.png"))
        self.refno_text = PhotoImage(file=resource_path("resources/register1/text_refno.png"))
        self.date_text = PhotoImage(file=resource_path("resources/register1/text_date.png"))
        self.name_text = PhotoImage(file=resource_path("resources/register1/name_text.png"))
        self.address_text = PhotoImage(file=resource_path("resources/register1/address_text.png"))
        self.birthdate_text = PhotoImage(file=resource_path("resources/register1/birthdate_text.png"))
        self.nationality_text = PhotoImage(file=resource_path("resources/register1/nationality_text.png"))
        self.age_text = PhotoImage(file=resource_path("resources/register1/age_text.png"))
        self.religion_text = PhotoImage(file=resource_path("resources/register1/religion_text.png"))
        self.occupation_text = PhotoImage(file=resource_path("resources/register1/occupation_text.png"))
        self.monthlyincome_text = PhotoImage(file=resource_path("resources/register1/monthlyincome_text.png"))
        self.otherincome_text = PhotoImage(file=resource_path("resources/register1/otherincome_text.png"))
        self.expenditures_text = PhotoImage(file=resource_path("resources/register1/expenditures_text.png"))
        self.sex_text = PhotoImage(file=resource_path("resources/register1/sex_text.png"))
        self.membership_text = PhotoImage(file=resource_path("resources/register1/membership_text.png"))
        self.civilstatus_text = PhotoImage(file=resource_path("resources/register1/civilstatus_text.png"))
        self.educattainment_text = PhotoImage(file=resource_path("resources/register1/educattainment_text.png"))
        self.gmi_text = PhotoImage(file=resource_path("resources/register1/gmi_text.png"))
        self.nmi_text = PhotoImage(file=resource_path("resources/register1/nmi_text.png"))
        

        # CREATE BACKGROUND IMAGE
        self.create_image(410.0, 250.0, image = self.gradiantBG)
        self.create_image(395.0, 5.0, image = self.blueHeader)
        self.create_image(673.0, 17.0, image = self.pcsoLogo)
        self.create_image(750.0, 16.0, image = self.pcsoText)
        
        self.backgroundImage = []
        self.backgroundImage.append(self.create_image(406.0, 262.0, image = self.whiteBG))
        self.backgroundImage.append(self.create_image(140.0, 140.0, image=self.applicantInfo))

        # CREATE TEXT IMAGE
        self.textImage = []
        self.textImage.append(self.create_image(113.0, 85.0, image=self.appstatus_text))
        self.textImage.append(self.create_image(425.0, 82.0, image=self.refno_text))
        self.textImage.append(self.create_image(631.0, 87.0, image=self.date_text))
        self.textImage.append(self.create_image(124.0, 169.0, image=self.name_text))
        self.textImage.append(self.create_image(110.0, 209.0, image=self.address_text))
        self.textImage.append(self.create_image(83.0, 260.0, image=self.birthdate_text))
        self.textImage.append(self.create_image(88.0, 300.0, image=self.nationality_text))
        self.textImage.append(self.create_image(88.0, 340.0, image=self.occupation_text))
        self.textImage.append(self.create_image(260.0, 260.0, image=self.age_text))
        self.textImage.append(self.create_image(272.0, 300.0, image=self.religion_text))
        self.textImage.append(self.create_image(295.0, 340.0, image=self.monthlyincome_text))
        self.textImage.append(self.create_image(490.0, 169.0, image=self.sex_text))
        self.textImage.append(self.create_image(515.0, 209.0, image=self.membership_text))
        self.textImage.append(self.create_image(510.0, 256.0, image=self.civilstatus_text))
        self.textImage.append(self.create_image(568.0, 320.0, image=self.educattainment_text))
        self.textImage.append(self.create_image(122.0, 400.0, image=self.otherincome_text))
        self.textImage.append(self.create_image(310.0, 400.0, image=self.expenditures_text))
        self.textImage.append(self.create_image(496.0, 400.0, image=self.gmi_text))
        self.textImage.append(self.create_image(670.0, 400.0, image=self.nmi_text))

        
        # CREATE ENTRY
        self.ReferenceNo = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Date = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.FullName = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.PermanentAddress = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Birthdate = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Age = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Nationality = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Religion = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Occupation = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.MonthlyIncome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.OtherSourceOfIncome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.MonthlyExpenditure = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.GrossMonthlyIncome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.NetMonthlyIncome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)



        # ENTRY PLACE
        self.ReferenceNo.place(x=385, y=95, width=170.0, height=15.0)   
        self.Date.place(x=620, y=95, width=100.0, height=15.0)
        self.FullName.place(x=60, y=180, width=250.0, height=15.0)
        self.PermanentAddress.place(x=60, y=220, width=250.0, height=15.0)
        self.Birthdate.place(x=60, y=270, width=100.0, height=15.0)
        self.Age.place(x=250, y=269, width=50.0, height=15.0)
        self.Nationality.place(x=60, y=310, width=100.0, height=15.0)
        self.Religion.place(x=250, y=309, width=100.0, height=15.0)
        self.Occupation.place(x=60, y=350, width=100.0, height=15.0)
        self.MonthlyIncome.place(x=250, y=349, width=100.0, height=15.0)
        self.OtherSourceOfIncome.place(x=60, y=413, width=100.0, height=15.0)
        self.MonthlyExpenditure.place(x=252, y=413, width=100.0, height=15.0)
        self.GrossMonthlyIncome.place(x=440, y=413, width=100.0, height=15.0)
        self.NetMonthlyIncome.place(x=620, y=413, width=100.0, height=15.0)
        


        # ENTRY IMAGES
        self.entryImage = []
        self.entryImage.append(self.create_image(490.0, 102.0, image=self.referenceEntry))
        self.entryImage.append(self.create_image(688.0, 102.0, image=self.entry1))
        self.entryImage.append(self.create_image(240.0, 187.0, image=self.entry2))
        self.entryImage.append(self.create_image(240.0, 227.0, image=self.entry2))
        self.entryImage.append(self.create_image(127.0, 277.0, image=self.entry3))
        self.entryImage.append(self.create_image(127.0, 317.0, image=self.entry3))
        self.entryImage.append(self.create_image(127.0, 357.0, image=self.entry3))
        self.entryImage.append(self.create_image(320.0, 276.0, image=self.entry3))
        self.entryImage.append(self.create_image(320.0, 316.0, image=self.entry3))
        self.entryImage.append(self.create_image(320.0, 356.0, image=self.entry3))
        self.entryImage.append(self.create_image(127.0, 420.0, image=self.entry3))
        self.entryImage.append(self.create_image(320.0, 420.0, image=self.entry3))
        self.entryImage.append(self.create_image(505.0, 420.0, image=self.entry3))
        self.entryImage.append(self.create_image(685.0, 420.0, image=self.entry3))



        # RADIOBUTTON
        self.radiobuttonFont = ("Nokora Bold", 12 * -1)
        self.ApplicantStatus = tk.StringVar()
        self.Sex = tk.StringVar()
        self.Membership = tk.StringVar()
        self.CivilStatus = tk.StringVar()
        self.EducationalAttainment = tk.StringVar()
        
        self.ApplicantStatus.set(None)
        self.Sex.set(None)
        self.Membership.set(None)
        self.CivilStatus.set(None)
        self.EducationalAttainment.set(None)

        self.NewApplicant = Radiobutton(self, text="New Applicant", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="New Applicant", variable=self.ApplicantStatus, font = self.radiobuttonFont)
        self.OldApplicant = Radiobutton(self, text="Old Applicant", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Old Applicant", variable=self.ApplicantStatus, font = self.radiobuttonFont)
        self.Male = Radiobutton(self, text="Male", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.Sex, font=self.radiobuttonFont)
        self.Female = Radiobutton(self, text="Female", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="F", variable=self.Sex, font=self.radiobuttonFont)
        self.Member = Radiobutton(self, text="Member", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Member", variable = self.Membership, font=self.radiobuttonFont)
        self.NonMember = Radiobutton(self, text="Non-Member", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Non-Member", variable = self.Membership, font=self.radiobuttonFont)
        self.Dependent = Radiobutton(self, text="Dependent", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Dependent", variable = self.Membership, font=self.radiobuttonFont)
        self.Single = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Single", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.Married = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Married", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.Widow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Widow", variable=self.CivilStatus, font=self.radiobuttonFont) 
        self.Separated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Separated", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.WithPartner = Radiobutton(self, text="With Common Law Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="With Partner", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.PostGraduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.College = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.Elementary = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.Vocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.HighSchool = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self._None = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="None", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        
        # RADIOBUTTON PLACE
        self.NewApplicant.place(x=55.0, y=96, width=100.0, height=20.0)
        self.OldApplicant.place(x=160.0, y=96, width=100.0, height=20.0)
        self.Male.place(x=472.0, y=180.0, width=60.0, height=15.0)
        self.Female.place(x=564.0, y=180.0, width=60.0, height=15.0)
        self.Member.place(x=472.0, y=220.0, width=80.0, height=15.0)
        self.NonMember.place(x=550.0, y=220.0, width=120.0, height=15.0)
        self.Dependent.place(x=660.0, y=220.0, width=100.0, height=15.0)
        self.Single.place(x=477.0, y=270.0, width=60.0, height=15.0)
        self.Married.place(x=564.0, y=270.0, width=60.0, height=15.0)
        self.Widow.place(x=668.0, y=270.0, width=60.0, height=15.0)
        self.Separated.place(x=477.0, y=288.0, width=80.0, height=15.0)
        self.WithPartner.place(x=563.0, y=288.0, width=170.0, height=15.0)
        self.PostGraduate.place(x=468.0, y=330.0, width=120.0, height=15.0)
        self.College.place(x=590.0, y=330.0, width=80.0, height=15.0)
        self.Elementary.place(x=670.0, y=330.0, width=100.0, height=15.0)
        self.Vocational.place(x=467.0, y=348.0, width=100.0, height=15.0)
        self.HighSchool.place(x=570.0, y=348.0, width=100.0, height=15.0)
        self._None.place(x=674.0, y=348.0, width=60.0, height=15.0)



        # BUTTONS
        self.homeButton = tk.Button(image=self.button2, borderwidth=0, highlightthickness=0, command=self.backtoHome, relief="flat")
        self.nextButton = tk.Button(image=self.button1, borderwidth=0, highlightthickness=0, command=self.next_page, relief="flat")

        # BUTTON PLACE
        self.homeButton.place(x=7.0, y=3.0, width=30.0, height=29.0)
        self.nextButton.place(x=645.0, y=451.0, width=125.0, height=26.515151977539062)




















        # #LOAD THE IMAGES
        # self.image_image_1 = PhotoImage(file=resource_path("resources/APP_1/image_1.png"))  
        # self.image_entry_3 = PhotoImage(file=resource_path("resources/APP_1/entry_3.png"))
        # self.image_entry_5 = PhotoImage(file=resource_path("resources/APP_1/entry_5.png"))
        # self.image_image_6 = PhotoImage(file=resource_path("resources/APP_1/image_6.png"))
        # self.image_entry_11 = PhotoImage(file=resource_path("resources/APP_1/entry_11.png"))
        # self.image_entry_12 = PhotoImage(file=resource_path("resources/APP_1/entry_12.png"))    
        # self.image_entry_9 = PhotoImage(file=resource_path("resources/APP_1/entry_9.png"))
        # self.image_entry_16 = PhotoImage(file=resource_path("resources/APP_1/entry_16.png"))
        # self.button_image_1 = PhotoImage(file=resource_path("resources/APP_1/button_1.png"))
 
       
        
#         #BACKGROUND IMAGE
       
#         self.create_image(405.0, 46.0, image=self.image_image_1)

#         #ENTRY IMAGES
#         self.pageImage1_id = [] # Store the image ids to hide them later
#         self.pageImage1_id.append(self.create_image(120.0, 150.5, image=self.image_image_6))
#         self.pageImage1_id.append(self.create_image(409.0, 190.5, image=self.image_entry_3))
#         self.pageImage1_id.append(self.create_image(409.0, 237.5, image=self.image_entry_3))
#         self.pageImage1_id.append(self.create_image(397.0, 120.5, image=self.image_entry_11))
#         # self.pageImage1_id.append(self.create_image(155.5, 120.5, image=self.image_entry_11))
#         self.pageImage1_id.append(self.create_image(120.5, 310.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(298.5, 310.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(120.5, 340.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(298.5, 340.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(490.5, 342.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(120.5, 410.5, image=self.image_entry_5))
#         self.pageImage1_id.append(self.create_image(280.5, 410.5, image=self.image_entry_16))
#         self.pageImage1_id.append(self.create_image(472.5, 410.5, image=self.image_entry_16))
#         self.pageImage1_id.append(self.create_image(612.5, 410.5, image=self.image_entry_16))
#         self.pageImage1_id.append(self.create_image(750.5, 410.5, image=self.image_entry_16))      

        
#         #CREATE THE TEXTS OF FIRST PAGE
#         self.pageText1_id = []     
#         self.pageText1_id.append(self.create_text(49.0, 100.0, anchor="nw", text="Reference No:", fill="#000000", font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(289.0, 100,anchor ="nw", text="Date:",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(550.0, 100.0,anchor ="nw", text="Applicant Status:",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(49.0,172.0,anchor ="nw", text="Full Name Of The Patient    ",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(87.0,203.0,anchor ="nw", text="Surname",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(385., 205,anchor ="nw", text="First Name", fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(691.0,204,anchor ="nw", text="Middle Name",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(49.0, 219.0,anchor ="nw", text="Permanent Address",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(87.0, 250.0,anchor ="nw", text="No",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(120.0, 250.0,anchor ="nw", text="Street",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(180.0, 250.0,anchor ="nw", text="Barangay",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(320.0, 250.0,anchor ="nw", text="Municipality/City",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(500.0, 250.0,anchor ="nw", text="Province",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(700, 250.0,anchor ="nw", text="Region",fill="#000000",font=("Mada Regular", 8 * -1)))
#         self.pageText1_id.append(self.create_text(49.0, 265.0,anchor ="nw", text="Civil Status",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(49.0, 290.0,anchor ="nw", text="Birthdate:",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(227.0, 290.0,anchor ="nw", text="Age:",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(420.0, 290.0,anchor ="nw", text = "Sex",fill="#000000",font=("Mada Regular", 10 * -1)))      
#         self.pageText1_id.append(self.create_text(49.0, 321.5,anchor ="nw", text = "Nationality",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(227.0, 321.5,anchor ="nw", text = "Religion",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(49.0, 353, anchor ="nw", text = "Highest Educational Attainment",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(420.0, 321, anchor ="nw", text = "Occupation",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(650.0, 321, anchor ="nw", text = "Membership",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(49.0, 390, anchor ="nw", text = "Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(227.0, 390, anchor ="nw", text = "Other Sources Of Income",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(420.0, 390, anchor ="nw", text = "Monthly Expenditure",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(559.0, 390, anchor ="nw", text = "Gross Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))
#         self.pageText1_id.append(self.create_text(700.0, 390, anchor ="nw", text = "Net Monthly Income",fill="#000000",font=("Mada Regular", 10 * -1)))

# # RADIO BUTTON
#         self.Applicant_Status = tk.StringVar() 
#         self.Applicant_Status.set("New Applicant") # Default value
#         self.Civil_Status = tk.StringVar() 
#         self.Civil_Status.set("S ")
#         self.Membership = tk.StringVar()
#         self.Membership.set("Member")
#         self.Sex = tk.StringVar()
#         self.Sex.set("F")
#         self.Highest_Educational_Attainment = tk.StringVar()
#         self.Highest_Educational_Attainment.set("None")
# #Radio Button
#         self.New_Status = Radiobutton(self, text="New", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="New Applicant", variable=self.Applicant_Status)
#         self.Old_Status = Radiobutton(self, text="Old", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Old Applicant", variable=self.Applicant_Status)
#         self.Single = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="S", variable=self.Civil_Status, font=("Mada Regular", 10 * -1))
#         self.Widow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Widow", variable=self.Civil_Status, font=("Mada Regular", 10 * -1))
#         self.Married = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.Civil_Status, font=("Mada Regular", 10 * -1))
#         self.Separated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="SE", variable=self.Civil_Status, font=("Mada Regular", 10 * -1))
#         self.With_Partner = Radiobutton(self, text="With Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="C", variable=self.Civil_Status, font=("Mada Regular", 10 * -1))

#         self.Male = Radiobutton(self, text="Male", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.Sex, font=("Mada Regular", 10 * -1))
#         self.Female = Radiobutton(self, text="Female", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="F", variable=self.Sex, font=("Mada Regular", 10 * -1))
#         self.Post_Graduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self.College = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self.Elementary_School = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self.Vocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self.High_School = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self._None = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="None", variable=self.Highest_Educational_Attainment, font=("Mada Regular", 10 * -1))
#         self.Member = Radiobutton(self, text="Member", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Member", variable=self.Membership, font=("Mada Regular", 10 * -1))
#         self.Non_Member = Radiobutton(self, text="Non-Member", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Non-Member", variable=self.Membership, font=("Mada Regular", 10 * -1))
#         self.Dependent = Radiobutton(self, text="Dependent", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Dependent", variable=self.Membership, font=("Mada Regular", 10 * -1))
        
# #Radio Button Place
#         self.New_Status.place(x=550.0, y=115.5, width=50.0, height=10.0)
#         self.Old_Status.place(x=640.0, y=115.5, width=50.0, height=10.0)
#         self.Single.place(x=49.0, y=275.5, width=60.0, height=15.0)
#         self.Widow.place(x=170.0, y=275.5, width=60.0, height=15.0)
#         self.Married.place(x=270.0, y=275.5, width=60.0, height=15.0)
#         self.Separated.place(x=370.0, y=275.5, width=70.0, height=15.0)
#         self.With_Partner.place(x=470.0, y=276.5, width=80.0, height=15.0)
#         self.Male.place(x=410.0, y=305.5, width=60.0, height=15.0)
#         self.Female.place(x=500.0, y=305.5, width=60.0, height=15.0)
#         self.Post_Graduate.place(x=49.0, y=370.5, width=100.0, height=15.0)
#         self.College.place(x=170.0, y=370.5, width=60.0, height=15.0)
#         self.Elementary_School.place(x=270.0, y=370.5, width=80.0, height=15.0)
#         self.Vocational.place(x=370.0, y=370.5, width=80.0, height=15.0)
#         self.High_School.place(x=470.0, y=370.5, width=80.0, height=15.0)
#         self._None.place(x=570.0, y=370.5, width=60.0, height=15.0)
#         self.Member.place(x=585.0, y=335.5, width=59.0, height=15.0)
#         self.Non_Member.place(x=655.0, y=335.5, width=75.0, height=15.0)
#         self.Dependent.place(x=730.0, y=335.5, width=80.0, height=15.0)


        
# #ENTRY
#         initial_reference_id = self.ReferenceHandle.get_last_reference_id()
#         self.Reference_No = Entry(self,bd=0,bg="#FFFFFF", fg="#000716", highlightthickness=0)
#         self.Reference_No.insert(0, initial_reference_id)
#         self.Reference_No.config(state='readonly')

#         self.Date = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.FullName = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Permanent_Address = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Birthdate = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Age = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Nationality = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Religion = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Occupation = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Monthly_Income = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Other_Sources_Of_Income = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Monthly_Expenditure = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Gross_Monthly_Income = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
#         self.Net_Monthly_Income = Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0);
# #PLACE ENTRY
#         self.Reference_No.place(x=60.0, y=115.5, width=43.0, height=10.0)
#         self.Date.place(x=290.0, y=115.5, width=208.0, height=10.0)
#         self.FullName.place(x=53.0, y=185.5, width=712.0, height=10.0)
#         self.Permanent_Address.place(x=52.0, y=232.5, width=716.0, height=10.0)
#         self.Birthdate.place(x=52.0, y=305.5, width=142.0, height=10.0)
#         self.Age.place(x=230.0, y=305.5, width=140.0, height=10.0)
#         self.Nationality.place(x=52.0, y=335.5, width=142.0, height=10.0)
#         self.Religion.place(x=230.0, y=335.5, width=142.0, height=10.0)
#         self.Occupation.place(x=420.0, y=335.5, width=142.0, height=10.0)
#         self.Monthly_Income.place(x=52.0, y=405.5, width=110.0, height=10.0)
#         self.Other_Sources_Of_Income.place(x=230.0, y=405.5, width=105.0, height=10.0)
#         self.Monthly_Expenditure.place(x=420.0, y=405.5, width=105.0, height=10.0)
#         self.Gross_Monthly_Income.place(x=559.0, y=405.5, width=105.0, height=10.0)
#         self.Net_Monthly_Income.place(x=700.0, y=405.5, width=105.0, height=10.0)


# 2ND PAGE
#LOAD THE IMAGES        
        self.add_Button = PhotoImage(file=resource_path("resources/register2/addButton.png"))
        self.back_Button = PhotoImage(file=resource_path("resources/register2/backButton.png"))
        self.delete_Button = PhotoImage(file=resource_path("resources/register2/deleteButton.png"))
        self.submit_Button = PhotoImage(file=resource_path("resources/register2/submitButton.png"))

        self.householdInfo = PhotoImage(file=resource_path("resources/register2/householdInfo.png"))
        self.whiteBg = PhotoImage(file=resource_path("resources/register2/whiteBg.png"))

        self.membersText = PhotoImage(file=resource_path("resources/register2/members_text.png"))
        self.nameText = PhotoImage(file=resource_path("resources/register2/name_text.png"))
        self.relationText = PhotoImage(file=resource_path("resources/register2/relation_text.png"))
        self.age_text = PhotoImage(file=resource_path("resources/register1/age_text.png"))
        self.occupation_text = PhotoImage(file=resource_path("resources/register1/occupation_text.png"))
        self.monthlyincome_text = PhotoImage(file=resource_path("resources/register1/monthlyincome_text.png"))

        self.nameEntry = PhotoImage(file=resource_path("resources/register2/name_entry.png"))
        self.entryAll = PhotoImage(file=resource_path("resources/register2/entry_all.png"))
        
        # IMAGES
        self.backgroundImage2 = []
        self.backgroundImage2.append(self.create_image(405.0, 46.0, image=self.householdInfo, state = "hidden"))
        self.backgroundImage2.append(self.create_image(405.0, 46.0, image=self.whiteBg, state = "hidden"))

        # ENTRY IMAGES
        self.entryImage2 = []
        self.entryImage2.append(self.create_image(91.0, 226.0, image=self.nameEntry,state = "hidden"))
        self.entryImage2.append(self.create_image(91.0, 280.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(91.0, 334.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(285.0, 280.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(285.0, 334.0, image=self.entryAll, state = "hidden"))

        # CREATE TEXT IMAGE
        self.textImage2 = []
        self.textImage2.append(self.create_image(75.0, 126, image=self.membersText, state = "hidden"))
        self.textImage2.append(self.create_image(94.0, 206.0, image=self.nameText, state = "hidden"))
        self.textImage2.append(self.create_image(94.0, 263.0, image=self.relationText, state = "hidden"))
        self.textImage2.append(self.create_image(288.0, 263.5, image=self.age_text, state = "hidden"))
        self.textImage2.append(self.create_image(94.0, 317.0, image=self.occupation_text, state = "hidden"))
        self.textImage2.append(self.create_image(288.0, 322.5, image=self.monthlyincome_text, state = "hidden"))
        
                
        #RADIO BUTTON
        self.HCivilStatus = tk.StringVar()
        self.HCivilStatus.set("S")
        self.HHigeshtEducationalAttainment = tk.StringVar()
        self.HHigeshtEducationalAttainment.set("None")

        self.HSingle = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="S", variable=self.HCivilStatus, font=("Mada Regular", 10 * -1))
        self.HWidow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="W", variable=self.HCivilStatus, font=("Mada Regular", 10 * -1))
        self.HMarried = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.HCivilStatus, font=("Mada Regular", 10 * -1))
        self.HSeparated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="SE", variable=self.HCivilStatus, font=("Mada Regular", 10 * -1))
        self.HWithPartner = Radiobutton(self, text="With Common Law Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="C", variable=self.HCivilStatus, font=("Mada Regular", 10 * -1))

        self.HPost_Graduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))
        self.HCollege = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))
        self.HElementary_School = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))
        self.HVocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))
        self.HHigh_School = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))
        self.HNone = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="None", variable=self.HHigeshtEducationalAttainment, font=("Mada Regular", 10 * -1))

        #ENTRY            
        self.Hname = tk.Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Hage = tk.Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Hrelation = tk.Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Hoccupation = tk.Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)
        self.Hmonthlyincome = tk.Entry(self,bd=0, bg="#FFE5AB", fg="#000716", highlightthickness=0)

        
        # CREATE BUTTON
        self.addButton = tk.Button(self, image=self.add_Button, borderwidth=0, highlightthickness=0, command=lambda: print("Add Button is clicked"))
        self.deleteButton = tk.Button(self, image=self.delete_Button, borderwidth=0, highlightthickness=0, command=lambda: print("Delete Button is clicked"))
        self.backButton = tk.Button(self, image=self.back_Button, borderwidth=0, highlightthickness=0, command=self.back_page)
        self.submitButton = tk.Button(self, image=self.submit_Button, borderwidth=0, highlightthickness=0, command=self.commit_data)

        # PLACE BUTTON
        # self.addButton.place(x=651.0, y=102.0, width=100.0, height=30.0)
        # self.deleteButton.place(x=696.06, y=102.0, width=100.0, height=30.0)
        # self.backButton.place(x=198.28, y=435.0, width=100.0, height=30.0)
        # self.submitButton.place(x=615.0, y=410.0, width=100.0, height=30.0)
        

    def next_page(self):
        # HIDE THE WIDGETS PAGE 1
        for bg in self.backgroundImage:
            self.itemconfigure(bg, state="hidden")

        for image in self.entryImage:
            self.itemconfigure(image, state="hidden")

        for text in self.textImage:
            self.itemconfigure(text, state="hidden")

            self.NewApplicant.place_forget()
            self.OldApplicant.place_forget()
            self.Single.place_forget()
            self.Widow.place_forget()
            self.Married.place_forget()
            self.Separated.place_forget()
            self.WithPartner.place_forget()
            self.Male.place_forget()
            self.Female.place_forget()
            self.PostGraduate.place_forget()
            self.College.place_forget()
            self.Elementary.place_forget()
            self.Vocational.place_forget()
            self.HighSchool.place_forget()
            self._None.place_forget()
            self.Member.place_forget()
            self.NonMember.place_forget()
            self.Dependent.place_forget()
            self.ReferenceNo.place_forget()
            self.Date.place_forget()
            self.FullName.place_forget()
            self.PermanentAddress.place_forget()
            self.Birthdate.place_forget()
            self.Age.place_forget()
            self.Nationality.place_forget()
            self.Religion.place_forget()
            self.Occupation.place_forget()
            self.MonthlyIncome.place_forget()
            self.OtherSourceOfIncome.place_forget()
            self.MonthlyExpenditure.place_forget()
            self.GrossMonthlyIncome.place_forget()
            self.NetMonthlyIncome.place_forget()
            self.nextButton.place_forget()

# LOAD THE IMAGES PAGE 2
            for bg_id in self.backgroundImage2:
                self.itemconfigure(bg_id, state='normal')

            for image_id in self.entryImage2:
                self.itemconfigure(image_id, state="normal")

            for text_id in self.textImage2:
                self.itemconfigure(text_id, state="normal")
            self.HSingle.place(x=40.0, y=245.5, width=60.0, height=15.0)
            self.HWidow.place(x=120.0, y=245.5, width=60.0, height=15.0)
            self.HMarried.place(x=40.0, y=265.5, width=60.0, height=15.0)
            self.HSeparated.place(x=123.0, y=265.5, width=70.0, height=15.0)
            self.HPost_Graduate.place(x=360.0, y=310.5, width=100.0, height=15.0)
            self.HHigh_School.place(x=470.0, y=310.5, width=100.0, height=15.0)
            self.HVocational.place(x=360.0, y=330.5, width=83.0, height=15.0)
            self.HElementary_School.place(x=470.0, y=330.5, width=95.0, height=15.0)
            self.HCollege.place(x=360.0, y=350.5, width=70.0, height=15.0)
            self.HNone.place(x=470.0, y=350.5, width=65.0, height=15.0)
            self.Hname.place(x=40.0, y=195.0, width=515.0, height=10.0)
            self.Hage.place(x=637.0, y=194.0, width=50.0, height=10.0)
            self.Hrelation.place(x=40.0, y=314.0, width=245.0, height=10.0)
            self.Hoccupation.place(x=40.0, y=410.0, width=200.0, height=10.0)
            self.Hmonthlyincome.place(x=319.0, y=410.0, width=160.0, height=10.0)
            self.addButton.place(x=651.0, y=102.0, width=100.0, height=30.0)
            self.deleteButton.place(x=696.06, y=102.0, width=100.0, height=30.0)
            self.backButton.place(x=198.28, y=435.0, width=100.0, height=30.0)
            self.submitButton.place(x=615.0, y=410.0, width=100.0, height=30.0)
                        

#SHOW THE WIDGETS
    def back_page(self):
#SHOW THE WIDGETS PAGE 1
            for image_id in self.entryImage:
                self.itemconfigure(image_id, state="normal")
            for text_id in self.textImage:
                self.itemconfigure(text_id, state="normal")
#HIDE THE WIDGETS PAGE 2
            for image_id in self.entryImage2:
                self.itemconfigure(image_id, state="hidden")
            for text_id in self.textImage2:
                self.itemconfigure(text_id, state="hidden")
                self.button_2.place(x=100.0,y=450.0,width=100.0,height=30.0)
                self.HSingle.place_forget()
                self.HWidow.place_forget()
                self.HMarried.place_forget()
                self.HSeparated.place_forget()
                self.HPost_Graduate.place_forget()
                self.HHigh_School.place_forget()
                self.HVocational.place_forget()
                self.HElementary_School.place_forget()
                self.HCollege.place_forget()
                self.HNone.place_forget()
                self.Hname.place_forget()
                self.Hage.place_forget()
                self.Hrelation.place_forget()
                self.Hoccupation.place_forget()
                self.Hmonthlyincome.place_forget()
                self.Reference_No.place(x=50.0, y=115.5, width=210.0, height=10.0)
                self.Date.place(x=290.0, y=115.5, width=208.0, height=10.0)
                self.FullName.place(x=53.0, y=185.5, width=712.0, height=10.0)
                self.Permanent_Address.place(x=52.0, y=232.5, width=716.0, height=10.0)
                self.Birthdate.place(x=52.0, y=305.5, width=142.0, height=10.0)
                self.Age.place(x=230.0, y=305.5, width=140.0, height=10.0)
                self.Nationality.place(x=52.0, y=335.5, width=142.0, height=10.0)
                self.Religion.place(x=230.0, y=335.5, width=142.0, height=10.0)
                self.Occupation.place(x=420.0, y=335.5, width=142.0, height=10.0)
                self.Monthly_Income.place(x=52.0, y=405.5, width=110.0, height=10.0)
                self.Other_Sources_Of_Income.place(x=230.0, y=405.5, width=105.0, height=10.0)
                self.Monthly_Expenditure.place(x=420.0, y=405.5, width=105.0, height=10.0)
                self.Gross_Monthly_Income.place(x=559.0, y=405.5, width=105.0, height=10.0)
                self.Net_Monthly_Income.place(x=700.0, y=405.5, width=105.0, height=10.0)
                self.New_Status.place(x=550.0, y=115.5, width=50.0, height=10.0)
                self.Old_Status.place(x=640.0, y=115.5, width=50.0, height=10.0)
                self.Single.place(x=49.0, y=275.5, width=60.0, height=15.0)
                self.Widow.place(x=170.0, y=275.5, width=60.0, height=15.0)
                self.Married.place(x=270.0, y=275.5, width=60.0, height=15.0)
                self.Separated.place(x=370.0, y=275.5, width=70.0, height=15.0)
                self.With_Partner.place(x=470.0, y=276.5, width=80.0, height=15.0)
                self.Male.place(x=410.0, y=305.5, width=60.0, height=15.0)
                self.Female.place(x=500.0, y=305.5, width=60.0, height=15.0)
                self.Post_Graduate.place(x=49.0, y=370.5, width=100.0, height=15.0)
                self.College.place(x=170.0, y=370.5, width=60.0, height=15.0)
                self.Elementary_School.place(x=270.0, y=370.5, width=80.0, height=15.0)
                self.Vocational.place(x=370.0, y=370.5, width=80.0, height=15.0)
                self.High_School.place(x=470.0, y=370.5, width=80.0, height=15.0)
                self._None.place(x=570.0, y=370.5, width=60.0, height=15.0)
                self.Member.place(x=585.0, y=335.5, width=59.0, height=15.0)
                self.Non_Member.place(x=655.0, y=335.5, width=75.0, height=15.0)
                self.Dependent.place(x=730.0, y=335.5, width=80.0, height=15.0)
                self.button_1.place(x=635.0,y=450.0,width=100.0,height=30.0)
                self.button_2.place_forget()
                self.button_3.place_forget()

            
            

    
    def commit_data(self):
        try:
            # Insert applicant details
            self.applicant_details.insert_applicant_details(
                self.FullName.get(),
                self.Permanent_Address.get(),
                self.Civil_Status.get(),
                self.Birthdate.get(),
                self.Age.get(),
                self.Sex.get(),
                self.Nationality.get(),
                self.Religion.get(),
                self.Highest_Educational_Attainment.get(),
                self.Occupation.get(),
                self.Monthly_Income.get(),
                self.Membership.get(),
                self.Other_Sources_Of_Income.get(),
                self.Monthly_Expenditure.get(),
                self.Gross_Monthly_Income.get(),
                self.Net_Monthly_Income.get()
            )

            # Insert household details
            self.applicant_details.insert_household_details(
                self.Hname.get(),
                self.Hage.get(),
                self.HCivilStatus.get(),
                self.Hrelation.get(),
                self.HHigeshtEducationalAttainment.get(),
                self.Hoccupation.get(),
                self.Hmonthlyincome.get()
            )
            self.applicant_details.insert_household_details(
                "John Doe",  # Hname
                42,  # Hage
                "M",  # HCivilStatus
                "Spouse",  # Hrelation
                "College Graduate",  # HHighestEducationalAttainment
                "Software Engineer",  # Hoccupation
                7500  # Hmonthlyincome
            )           

            # Insert reference details
            self.applicant_details.insert_reference_details(
                self.Reference_No.get(),
                self.Date.get(),
                self.Applicant_Status.get()
            )

        except mysql.Error as err:
            messagebox.showerror(title="Database Error", message=f"Error: {err}")

        finally:
            print("Data insertion completed")


    def get_reference_id(self):
        # Call get_last_reference_id from DatabaseHandler instance
        reference_id = self.ReferenceHandle.get_last_reference_id()
        self.Reference_No.delete(0, 'end')  # Clear previous content if any
        self.Reference_No.insert(0, reference_id)
        print(f"Fetched Reference ID: {reference_id}")
        return reference_id
    

    def backtoHome(self):
        print("Back to Home")
        if self.switch_frame:
            print("Switching to Home")
            self.switch_frame('applicantadmin')
        else:
            print("Switch frame not none")


        
       

    
