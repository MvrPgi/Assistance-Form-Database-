from resources.FileTracker.tracker import resource_path
import tkinter as tk
from tkinter import PhotoImage, messagebox, Entry, Radiobutton, ttk
import mysql.connector as mysql
from mysql_connection import DatabaseConnection
import datetime
from datetime import datetime, date



class Register(tk.Canvas):
    def __init__(self, master=None, switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)
        self.database = DatabaseConnection()
        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app
        
        
        # ================== PAGE 1 ==================


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
        self.appstatusText = PhotoImage(file=resource_path("resources/register1/appstatus_text.png"))
        self.refnoText = PhotoImage(file=resource_path("resources/register1/text_refno.png"))
        self.dateText = PhotoImage(file=resource_path("resources/register1/text_date.png"))
        self.nameText = PhotoImage(file=resource_path("resources/register1/name_text.png"))
        self.addressText = PhotoImage(file=resource_path("resources/register1/address_text.png"))
        self.birthdateText = PhotoImage(file=resource_path("resources/register1/birthdate_text.png"))
        self.nationalityText = PhotoImage(file=resource_path("resources/register1/nationality_text.png"))
        self.ageText = PhotoImage(file=resource_path("resources/register1/age_text.png"))
        self.religionText = PhotoImage(file=resource_path("resources/register1/religion_text.png"))
        self.occupationText = PhotoImage(file=resource_path("resources/register1/occupation_text.png"))
        self.monthlyincomeText = PhotoImage(file=resource_path("resources/register1/monthlyincome_text.png"))
        self.otherincomeText = PhotoImage(file=resource_path("resources/register1/otherincome_text.png"))
        self.expendituresText = PhotoImage(file=resource_path("resources/register1/expenditures_text.png"))
        self.sexText = PhotoImage(file=resource_path("resources/register1/sex_text.png"))
        self.membershipText = PhotoImage(file=resource_path("resources/register1/membership_text.png"))
        self.civilstatusText = PhotoImage(file=resource_path("resources/register1/civilstatus_text.png"))
        self.educattainmentText = PhotoImage(file=resource_path("resources/register1/educattainment_text.png"))
        self.gmiText = PhotoImage(file=resource_path("resources/register1/gmi_text.png"))
        self.nmiText = PhotoImage(file=resource_path("resources/register1/nmi_text.png"))
        

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
        self.textImage.append(self.create_image(113.0, 85.0, image=self.appstatusText))
        self.textImage.append(self.create_image(425.0, 82.0, image=self.refnoText))
        self.textImage.append(self.create_image(631.0, 87.0, image=self.dateText))
        self.textImage.append(self.create_image(124.0, 169.0, image=self.nameText))
        self.textImage.append(self.create_image(110.0, 209.0, image=self.addressText))
        self.textImage.append(self.create_image(83.0, 260.0, image=self.birthdateText))
        self.textImage.append(self.create_image(88.0, 300.0, image=self.nationalityText))
        self.textImage.append(self.create_image(88.0, 340.0, image=self.occupationText))
        self.textImage.append(self.create_image(260.0, 260.0, image=self.ageText))
        self.textImage.append(self.create_image(272.0, 300.0, image=self.religionText))
        self.textImage.append(self.create_image(295.0, 340.0, image=self.monthlyincomeText))
        self.textImage.append(self.create_image(490.0, 169.0, image=self.sexText))
        self.textImage.append(self.create_image(515.0, 209.0, image=self.membershipText))
        self.textImage.append(self.create_image(510.0, 256.0, image=self.civilstatusText))
        self.textImage.append(self.create_image(568.0, 320.0, image=self.educattainmentText))
        self.textImage.append(self.create_image(122.0, 400.0, image=self.otherincomeText))
        self.textImage.append(self.create_image(310.0, 400.0, image=self.expendituresText))
        self.textImage.append(self.create_image(496.0, 400.0, image=self.gmiText))
        self.textImage.append(self.create_image(670.0, 400.0, image=self.nmiText))

        
        # CREATE ENTRY
        self.ReferenceNo = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0,state="normal")
        initial_reference_id = self.database.get_last_reference_id()
        self.ReferenceNo = Entry(self,bd=0,bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.ReferenceNo.insert(0, initial_reference_id)
        self.ReferenceNo.config(state='readonly')

        self.Date = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0,state="normal")
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
        self.PermanentAddress.place(x=60, y=220, width=360.0, height=15.0)
        self.Birthdate.place(x=60, y=270, width=100.0, height=15.0)
        self.Age.place(x=252, y=269, width=100.0, height=15.0)
        self.Nationality.place(x=60, y=310, width=100.0, height=15.0)
        self.Religion.place(x=252, y=309, width=100.0, height=15.0)
        self.Occupation.place(x=60, y=350, width=100.0, height=15.0)
        self.MonthlyIncome.place(x=252, y=349, width=100.0, height=15.0)
        self.OtherSourceOfIncome.place(x=60, y=413, width=100.0, height=15.0)
        self.MonthlyExpenditure.place(x=252, y=413, width=100.0, height=15.0)
        self.GrossMonthlyIncome.place(x=440, y=413, width=100.0, height=15.0)
        self.NetMonthlyIncome.place(x=620, y=413, width=100.0, height=15.0)
        
        applicationDate = datetime.now().strftime('%Y-%m-%d')
        self.Date.insert(0, applicationDate)
        self.Date.config(state='readonly')

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
        
        self.Single = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="S", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.Married = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.Widow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="W", variable=self.CivilStatus, font=self.radiobuttonFont) 
        self.Separated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="SE", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.WithPartner = Radiobutton(self, text="w/ Common Law Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="C", variable=self.CivilStatus, font=self.radiobuttonFont)
        self.Other = Radiobutton(self, text="Other", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="O", variable=self.CivilStatus, font=self.radiobuttonFont)

        self.PostGraduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.College = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.Elementary = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.Vocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.HighSchool = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        self.N0ne = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="NONE", variable=self.EducationalAttainment, font=self.radiobuttonFont)
        
        # RADIOBUTTON PLACE
        self.NewApplicant.place(x=55.0, y=96, width=100.0, height=20.0)
        self.OldApplicant.place(x=160.0, y=96, width=100.0, height=20.0)

        self.Male.place(x=472.0, y=180.0, width=60.0, height=15.0)
        self.Female.place(x=564.0, y=180.0, width=60.0, height=15.0)

        self.Member.place(x=472.0, y=220.0, width=80.0, height=15.0)
        self.NonMember.place(x=550.0, y=220.0, width=120.0, height=15.0)
        self.Dependent.place(x=660.0, y=220.0, width=100.0, height=15.0)

        self.Single.place(x=477.0, y=270.0, width=60.0, height=15.0)
        self.Married.place(x=550.0, y=270.0, width=60.0, height=15.0)
        self.Widow.place(x=620.0, y=270.0, width=60.0, height=15.0)
        self.Separated.place(x=477.0, y=288.0, width=80.0, height=15.0)
        self.WithPartner.place(x=557.0, y=288.0, width=170.0, height=15.0)
        self.Other.place(x=680.0, y=270.0, width=60.0, height=15.0)
        
        self.PostGraduate.place(x=468.0, y=330.0, width=120.0, height=15.0)
        self.College.place(x=590.0, y=330.0, width=80.0, height=15.0)
        self.Elementary.place(x=670.0, y=330.0, width=100.0, height=15.0)
        self.Vocational.place(x=467.0, y=348.0, width=100.0, height=15.0)
        self.HighSchool.place(x=570.0, y=348.0, width=100.0, height=15.0)
        self.N0ne.place(x=674.0, y=348.0, width=60.0, height=15.0)



        # BUTTONS
        self.homeButton = tk.Button(self, image=self.button2, borderwidth=0, highlightthickness=0, command=self.backtoHome, relief="flat")
        self.nextButton = tk.Button(self, image=self.button1, borderwidth=0, highlightthickness=0, command=self.next_page, relief="flat")

        # BUTTON PLACE
        self.homeButton.place(x=7.0, y=3.0, width=30.0, height=29.0)
        self.nextButton.place(x=645.0, y=451.0, width=125.0, height=26.515151977539062)

        # ================== END OF PAGE 1 ==================



















        # ================== PAGE 2 ==================

        #LOAD THE IMAGES        
        self.add_Button = PhotoImage(file=resource_path("resources/register2/addButton.png"))
        self.back_Button = PhotoImage(file=resource_path("resources/register2/backButton.png"))
        self.delete_Button = PhotoImage(file=resource_path("resources/register2/deleteButton.png"))
        self.submit_Button = PhotoImage(file=resource_path("resources/register2/submitButton.png"))

        self.householdInfo = PhotoImage(file=resource_path("resources/register2/householdInfo.png"))
        self.whiteBg = PhotoImage(file=resource_path("resources/register2/whiteBg.png"))
        self.buttonBg = PhotoImage(file=resource_path("resources/register2/button_bg.png"))

        self.HmembersText = PhotoImage(file=resource_path("resources/register2/members_text.png"))
        self.HnameText = PhotoImage(file=resource_path("resources/register2/name_text.png"))
        self.HrelationText = PhotoImage(file=resource_path("resources/register2/relation_text.png"))
        self.Hage_text = PhotoImage(file=resource_path("resources/register2/text_age.png"))
        self.Hoccupation_text = PhotoImage(file=resource_path("resources/register2/text_occupation.png"))
        self.Hmonthlyincome_text = PhotoImage(file=resource_path("resources/register2/text_monthlyIncome.png"))
        self.HcivilStatus_text = PhotoImage(file=resource_path("resources/register2/text_civilStatus.png"))
        self.HeducAttainment_text = PhotoImage(file=resource_path("resources/register2/text_educAttain.png"))

        self.nameEntry = PhotoImage(file=resource_path("resources/register2/name_entry.png"))
        self.entryAll = PhotoImage(file=resource_path("resources/register2/entry_all.png"))
        
        # IMAGES
        self.backgroundImage2 = []
        self.backgroundImage2.append(self.create_image(165.0, 100.0, image=self.householdInfo, state = "hidden"))
        self.backgroundImage2.append(self.create_image(405.0, 300.0, image=self.whiteBg, state = "hidden"))
        self.backgroundImage2.append(self.create_image(692.0, 120.0, image=self.buttonBg, state = "hidden"))

        #ENTRY            
        self.Member1_HName = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member1_HRelation = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member1_HAge = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member1_HOccupation = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member1_HMonthlyincome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)

        self.Member2_HName = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member2_HRelation = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member2_HAge = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member2_HOccupation = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)
        self.Member2_HMonthlyincome = Entry(self, bd=0, bg="#EAEAEA", fg="#000716", highlightthickness=0)

        # ENTRY IMAGES
        self.entryImage2 = []
        self.entryImage2.append(self.create_image(285.0, 258.0, image=self.nameEntry,state = "hidden"))
        self.entryImage2.append(self.create_image(187.0, 307.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(187.0, 356.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(381.0, 307.0, image=self.entryAll, state = "hidden"))
        self.entryImage2.append(self.create_image(381.0, 356.0, image=self.entryAll, state = "hidden"))

        # CREATE TEXT IMAGE
        self.textImage2 = []
        self.textImage2.append(self.create_image(100.0, 135, image=self.HmembersText, state = "hidden"))
        self.textImage2.append(self.create_image(120.0, 235.0, image=self.HnameText, state = "hidden"))
        self.textImage2.append(self.create_image(160.0, 285.0, image=self.HrelationText, state = "hidden"))
        self.textImage2.append(self.create_image(135.0, 335.0, image=self.Hoccupation_text, state = "hidden"))
        self.textImage2.append(self.create_image(308.0, 287.0, image=self.Hage_text, state = "hidden"))
        self.textImage2.append(self.create_image(345.0, 335.0, image=self.Hmonthlyincome_text, state = "hidden"))
        self.textImage2.append(self.create_image(528.0, 235.0, image=self.HcivilStatus_text, state = "hidden"))
        self.textImage2.append(self.create_image(593.0, 300.0, image=self.HeducAttainment_text, state = "hidden"))
                
        #RADIO BUTTON
        self.Member1_HCivilStatus = tk.StringVar()
        self.Member1_HCivilStatus.set(None)
        self.Member1_HEducationalAttainment = tk.StringVar()
        self.Member1_HEducationalAttainment.set(None)

        # MEMBER 1
        self.Member1_HSingle = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="S", variable=self.Member1_HCivilStatus, font = self.radiobuttonFont)
        self.Member1_HWidow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="W", variable=self.Member1_HCivilStatus, font = self.radiobuttonFont)
        self.Member1_HMarried = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.Member1_HCivilStatus, font = self.radiobuttonFont)
        self.Member1_HSeparated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="SE", variable=self.Member1_HCivilStatus, font = self.radiobuttonFont)
        self.Member1_HWithPartner = Radiobutton(self, text="w/ Common Law Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="C", variable=self.Member1_HCivilStatus, font = self.radiobuttonFont)      

        self.Member1_HPost_Graduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member1_HCollege = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member1_HElementary_School = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member1_HVocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member1_HHigh_School = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member1_HNone = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="NONE", variable=self.Member1_HEducationalAttainment, font=self.radiobuttonFont)

        # MEMBER 2
        self.Member2_HCivilStatus = tk.StringVar()
        self.Member2_HCivilStatus.set(None)
        self.Member2_HEducationalAttainment = tk.StringVar()
        self.Member2_HEducationalAttainment.set(None)

        self.Member2_HSingle = Radiobutton(self, text="Single", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="S", variable=self.Member2_HCivilStatus, font = self.radiobuttonFont)
        self.Member2_HWidow = Radiobutton(self, text="Widow", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="W", variable=self.Member2_HCivilStatus, font = self.radiobuttonFont)
        self.Member2_HMarried = Radiobutton(self, text="Married", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="M", variable=self.Member2_HCivilStatus, font = self.radiobuttonFont)
        self.Member2_HSeparated = Radiobutton(self, text="Separated", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="SE", variable=self.Member2_HCivilStatus, font = self.radiobuttonFont)
        self.Member2_HWithPartner = Radiobutton(self, text="w/ Common Law Partner", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="C", variable=self.Member2_HCivilStatus, font = self.radiobuttonFont)

        self.Member2_HPost_Graduate = Radiobutton(self, text="Post Graduate", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Post Graduate", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member2_HCollege = Radiobutton(self, text="College", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="College", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member2_HElementary_School = Radiobutton(self, text="Elementary", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Elementary", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member2_HVocational = Radiobutton(self, text="Vocational", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="Vocational", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member2_HHigh_School = Radiobutton(self, text="High School", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="High School", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)
        self.Member2_HNone = Radiobutton(self, text="None", bg="#FFFFFF", fg="#000716", activebackground="#FFFFFF", activeforeground="#000716", borderwidth=0, highlightthickness=0, value="NONE", variable=self.Member2_HEducationalAttainment, font=self.radiobuttonFont)

        # CREATE BUTTON
        self.addButton = tk.Button(self, image=self.add_Button, borderwidth=0, highlightthickness=0, command=self.getHouseholdMember)
        self.deleteButton = tk.Button(self, image=self.delete_Button, borderwidth=0, highlightthickness=0, command=self.deleteMember)
        self.backButton = tk.Button(self, image=self.back_Button, borderwidth=0, highlightthickness=0, command=self.back_page)
        self.submitButton = tk.Button(self, image=self.submit_Button, borderwidth=0, highlightthickness=0, command=self.commit_data)


        self.householdMember = ["Member 1", "Member 2"]
        self.combobox = ttk.Combobox(self, values=self.householdMember, state="hidden")
        self.combobox.set("Member 1")
        self.combobox.bind("<<ComboboxSelected>>", self.hideEntries)


    def deleteMember(self):
        if self.combobox.get() == "Member 1" or self.combobox.get() == self.HName1:
            self.combobox.config(state="normal")
            self.householdMember[0] = "Member 1"
            self.combobox['values'] = self.householdMember
            self.combobox.set(self.householdMember[0])
            self.combobox.config(state="readonly")
            
            self.Member1_HName.delete(0, 'end')
            self.Member1_HRelation.delete(0, 'end')
            self.Member1_HOccupation.delete(0, 'end')
            self.Member1_HAge.delete(0, 'end')
            self.Member1_HMonthlyincome.delete(0, 'end')
            self.Member1_HCivilStatus.set(None)
            self.Member1_HEducationalAttainment.set(None)
        elif self.combobox.get() == "Member 2" or self.combobox.get() == self.HName2:
            self.combobox.config(state="normal")
            self.householdMember[1] = "Member 2"
            self.combobox['values'] = self.householdMember
            self.combobox.set(self.householdMember[1])
            self.combobox.config(state="readonly")

            self.Member2_HName.delete(0, 'end')
            self.Member2_HRelation.delete(0, 'end')
            self.Member2_HOccupation.delete(0, 'end')
            self.Member2_HAge.delete(0, 'end')
            self.Member2_HMonthlyincome.delete(0, 'end')
            self.Member2_HCivilStatus.set(None)
            self.Member2_HEducationalAttainment.set(None)


    def hideEntries(self, event):
        if self.combobox.get() == "Member 1" or self.combobox.get() == self.HName1:
            self.Member2_HName.place_forget()
            self.Member2_HRelation.place_forget()
            self.Member2_HOccupation.place_forget()
            self.Member2_HAge.place_forget()
            self.Member2_HMonthlyincome.place_forget()

            self.Member2_HSingle.place_forget()
            self.Member2_HWidow.place_forget()
            self.Member2_HMarried.place_forget()
            self.Member2_HSeparated.place_forget()
            self.Member2_HWithPartner.place_forget()

            self.Member2_HPost_Graduate.place_forget()
            self.Member2_HCollege.place_forget()
            self.Member2_HHigh_School.place_forget()
            self.Member2_HElementary_School.place_forget()
            self.Member2_HVocational.place_forget()
            self.Member2_HNone.place_forget()

            self.Member1_HName.place(x=108.0, y=251.0, width=300.0, height=15.0)
            self.Member1_HRelation.place(x=108.0, y=300.0, width=100.0, height=15.0)
            self.Member1_HOccupation.place(x=108.0, y=349.0, width=100.0, height=15.0)
            self.Member1_HAge.place(x=300.0, y=300.0, width=100.0, height=15.0)
            self.Member1_HMonthlyincome.place(x=300.0, y=349.0, width=100.0, height=15.0)

            self.Member1_HSingle.place(x=490.0, y=250.0, width=60.0, height=15.0)
            self.Member1_HWidow.place(x=560.0, y=250.0, width=60.0, height=15.0)
            self.Member1_HMarried.place(x=630.0, y=250.0, width=60.0, height=15.0)
            self.Member1_HSeparated.place(x=490.0, y=268.0, width=80.0, height=15.0)
            self.Member1_HWithPartner.place(x=570.0, y=268.0, width=160.0, height=15.0)

            self.Member1_HPost_Graduate.place(x=480.0, y=315.0, width=120.0, height=15.0)
            self.Member1_HCollege.place(x=600.0, y=315.0, width=80.0, height=15.0)
            self.Member1_HHigh_School.place(x=484.0, y=333.0, width=100.0, height=15.0)
            self.Member1_HElementary_School.place(x=599.0, y=333.0, width=100.0, height=15.0)
            self.Member1_HVocational.place(x=479.0, y=350.0, width=100.0, height=15.0)
            self.Member1_HNone.place(x=603.0, y=350.0, width=60.0, height=15.0)

        if self.combobox.get() == "Member 2" or self.combobox.get() == self.HName2:
            self.Member1_HName.place_forget()
            self.Member1_HRelation.place_forget()
            self.Member1_HOccupation.place_forget()
            self.Member1_HAge.place_forget()
            self.Member1_HMonthlyincome.place_forget()

            self.Member1_HSingle.place_forget()
            self.Member1_HWidow.place_forget()
            self.Member1_HMarried.place_forget()
            self.Member1_HSeparated.place_forget()
            self.Member1_HWithPartner.place_forget()

            self.Member1_HPost_Graduate.place_forget()
            self.Member1_HCollege.place_forget()
            self.Member1_HHigh_School.place_forget()
            self.Member1_HElementary_School.place_forget()
            self.Member1_HVocational.place_forget()
            self.Member1_HNone.place_forget()

            self.Member2_HName.place(x=108.0, y=251.0, width=300.0, height=15.0)
            self.Member2_HRelation.place(x=108.0, y=300.0, width=100.0, height=15.0)
            self.Member2_HOccupation.place(x=108.0, y=349.0, width=100.0, height=15.0)
            self.Member2_HAge.place(x=300.0, y=300.0, width=100.0, height=15.0)
            self.Member2_HMonthlyincome.place(x=300.0, y=349.0, width=100.0, height=15.0)

            self.Member2_HSingle.place(x=490.0, y=250.0, width=60.0, height=15.0)
            self.Member2_HWidow.place(x=560.0, y=250.0, width=60.0, height=15.0)
            self.Member2_HMarried.place(x=630.0, y=250.0, width=60.0, height=15.0)
            self.Member2_HSeparated.place(x=490.0, y=268.0, width=80.0, height=15.0)
            self.Member2_HWithPartner.place(x=570.0, y=268.0, width=160.0, height=15.0)

            self.Member2_HPost_Graduate.place(x=480.0, y=315.0, width=120.0, height=15.0)
            self.Member2_HCollege.place(x=600.0, y=315.0, width=80.0, height=15.0)
            self.Member2_HHigh_School.place(x=484.0, y=333.0, width=100.0, height=15.0)
            self.Member2_HElementary_School.place(x=599.0, y=333.0, width=100.0, height=15.0)
            self.Member2_HVocational.place(x=479.0, y=350.0, width=100.0, height=15.0)
            self.Member2_HNone.place(x=603.0, y=350.0, width=60.0, height=15.0)

    def getHouseholdMember(self):
        try:
            if self.combobox.get() == "Member 1":
                self.HName1 = self.Member1_HName.get()
                self.HRelation1 = self.Member1_HRelation.get()
                self.HOccupation1 = self.Member1_HOccupation.get()
                self.HAge1 = int(self.Member1_HAge.get())
                self.HMonthlyIncome1 = int(self.Member1_HMonthlyincome.get())
                self.HCivilStatus1 = self.Member1_HCivilStatus.get()
                self.HEducationalAttainment1 = self.Member1_HEducationalAttainment.get()
                
                if not self.HName1.replace(" ", "").isalpha() or not self.HRelation1.replace(" ", "").isalpha() or not self.HOccupation1.replace(" ", "").isalpha():
                    messagebox.showerror("Invalid Input", "Name, Relation, and Occupation should only contain alphabetic characters.")
                    return
                if self.Member1_HCivilStatus.get() == "None" or self.Member1_HEducationalAttainment.get() == "None":
                    messagebox.showerror("Invalid Input", "Please select a Civil Status or Educational Attainment.")
                    return

                self.combobox.config(state="normal")
                self.householdMember.pop(0)
                self.householdMember.insert(0, self.HName1)
                self.combobox['values'] = self.householdMember
                self.combobox.set(self.HName1)
                self.combobox.config(state="readonly")
                
            if self.combobox.get() == "Member 2":
                self.HName2 = self.Member2_HName.get()
                self.HRelation2 = self.Member2_HRelation.get()
                self.HOccupation2 = self.Member2_HOccupation.get()
                self.HAge2 = int(self.Member2_HAge.get())
                self.HMonthlyIncome2 = int(self.Member2_HMonthlyincome.get())
                self.HCivilStatus2 = self.Member2_HCivilStatus.get()
                self.HEducationalAttainment2 = self.Member2_HEducationalAttainment.get()

                if not self.HName2.replace(" ", "").isalpha() or not self.HRelation2.replace(" ", "").isalpha() or not self.HOccupation2.replace(" ", "").isalpha():
                    messagebox.showerror("Invalid Input", "Name, Relation, and Occupation should only contain alphabetic characters.")
                    return
                if self.Member2_HCivilStatus.get() == "None" or self.Member2_HEducationalAttainment.get() == "None":
                    messagebox.showerror("Invalid Input", "Please select a Civil Status or Educational Attainment.")
                    return

                self.combobox.config(state="normal")
                self.householdMember.pop(1)
                self.householdMember.insert(1, self.HName2)
                self.combobox['values'] = self.householdMember
                self.combobox.set(self.HName2)
                self.combobox.config(state="readonly")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid value for Age or Monthly Income.")
            return
        except:
            messagebox.showerror("Invalid Input", "An error occurred. Please try again.")
            return


    def check_date(self):
        date_str = self.Birthdate.get()
        date_format = '%Y-%m-%d'
        
        if not date_str:
            messagebox.showerror("Invalid Input", "Please fill out the birthdate.")
            return False

        try:
            # Check if date is in 'YYYY/MM/DD' format
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter the date in YYYY-MM-DD format.")
            return False

    def validate_entries(self):
        if self.FullName.get() == "" or self.PermanentAddress.get() == "" or self.Age.get() == "" or self.Nationality.get() == "" or self.Religion.get() == "" or self.Occupation.get() == "" or self.MonthlyIncome.get() == "" or self.OtherSourceOfIncome.get() == "" or self.MonthlyExpenditure.get() == "" or self.GrossMonthlyIncome.get() == "" or self.NetMonthlyIncome.get() == "":
            messagebox.showerror("Invalid Input", "Please fill out all the fields.")
            return False
        if self.ApplicantStatus.get() == "None" or self.ApplicantStatus.get() == "":
            messagebox.showerror("Invalid Input", "Please select an Applicant Status.")
            return False
        if self.FullName.get() == "" or not self.FullName.get().replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Full Name.")
            return False
        if self.PermanentAddress.get() == "":
            messagebox.showerror("Invalid Input", "Please enter a valid value for Permanent Address.")
            return False
        if self.Age.get() == "" or not self.Age.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Age.")
            return False
        if self.Nationality.get() == "" or not self.Nationality.get().replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Nationality")
            return False
        if self.Religion.get() == "" or not self.Religion.get().replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Religion.")
            return False
        if self.Occupation.get() == "" or not self.Occupation.get().replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Occupation.")
            return False
        if self.MonthlyIncome.get() == "" or not self.MonthlyIncome.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Monthly Income.")
            return False
        if self.OtherSourceOfIncome.get() == "" or not self.OtherSourceOfIncome.get().replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Other Source of Income.")
            return False
        if self.MonthlyExpenditure.get() == "" or not self.MonthlyExpenditure.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Monthly Expenditure.")
            return False
        if self.GrossMonthlyIncome.get() == "" or not self.GrossMonthlyIncome.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Gross Monthly Income.")
            return False
        if self.NetMonthlyIncome.get() == "" or not self.NetMonthlyIncome.get().isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid value for Net Monthly Income.")
            return False
        if self.Sex.get() == "None" or self.Sex.get() == "":
            messagebox.showerror("Invalid Input", "Please select a Sex.")
            return False
        if self.Membership.get() == "None" or self.Membership.get() == "":
            messagebox.showerror("Invalid Input", "Please select a Membership.")
            return False
        if self.CivilStatus.get() == "None" or self.CivilStatus.get() == "":
            messagebox.showerror("Invalid Input", "Please select a Civil Status.")
            return False
        if self.EducationalAttainment.get() == "None" or self.EducationalAttainment.get() == "":
            messagebox.showerror("Invalid Input", "Please select an Educational Attainment.")
            return False
        
        return True

    def next_page(self):
        if not self.check_date():
            return
        
        if not self.validate_entries():
            return

        self.result = messagebox.askyesno("Household Member", "Do you want to add a household member?")
        if not self.result:
            self.InsertApplicant()
            self.switch_frame('applicanthomepage')
            return

        # HIDE THE WIDGETS PAGE 1
        for image_id in self.entryImage:
            self.itemconfigure(image_id, state="hidden")
        for text_id in self.textImage:
            self.itemconfigure(text_id, state="hidden")
        for bg_id in self.backgroundImage:
            self.itemconfigure(bg_id, state="hidden")

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
        self.NewApplicant.place_forget()
        self.OldApplicant.place_forget()
        self.Male.place_forget()
        self.Female.place_forget()
        self.Member.place_forget()
        self.NonMember.place_forget()
        self.Dependent.place_forget()
        self.Single.place_forget()
        self.Married.place_forget()
        self.Widow.place_forget()
        self.Separated.place_forget()
        self.WithPartner.place_forget()
        self.Other.place_forget()
        self.PostGraduate.place_forget()
        self.College.place_forget()
        self.Elementary.place_forget()
        self.Vocational.place_forget()
        self.HighSchool.place_forget()
        self.N0ne.place_forget()
        self.nextButton.place_forget()

        for bg_id2 in self.backgroundImage2:
            self.itemconfigure(bg_id2, state="normal")
        for text_id2 in self.textImage2:
            self.itemconfigure(text_id2, state="normal")
        for image_id2 in self.entryImage2:
            self.itemconfigure(image_id2, state="normal")
        
        self.Member1_HName.place(x=108.0, y=251.0, width=300.0, height=15.0)
        self.Member1_HRelation.place(x=108.0, y=300.0, width=100.0, height=15.0)
        self.Member1_HOccupation.place(x=108.0, y=349.0, width=100.0, height=15.0)
        self.Member1_HAge.place(x=300.0, y=300.0, width=100.0, height=15.0)
        self.Member1_HMonthlyincome.place(x=300.0, y=350.0, width=100.0, height=15.0)

        self.addButton.place(x=650.0, y=103.0, width=40.0, height=35.0)
        self.deleteButton.place(x=695.0, y=103.0, width=40.0, height=35.0)
        self.backButton.place(x=100.0, y=420.0, width=100.0, height=30.0)
        self.submitButton.place(x=615.0, y=420.0, width=100.0, height=30.0)

        self.Member1_HSingle.place(x=490.0, y=250.0, width=60.0, height=15.0)
        self.Member1_HWidow.place(x=560.0, y=250.0, width=60.0, height=15.0)
        self.Member1_HMarried.place(x=630.0, y=250.0, width=60.0, height=15.0)
        self.Member1_HSeparated.place(x=490.0, y=268.0, width=80.0, height=15.0)
        self.Member1_HWithPartner.place(x=570.0, y=268.0, width=160.0, height=15.0)

        self.Member1_HPost_Graduate.place(x=480.0, y=315.0, width=120.0, height=15.0)
        self.Member1_HCollege.place(x=600.0, y=315.0, width=80.0, height=15.0)
        self.Member1_HHigh_School.place(x=484.0, y=333.0, width=100.0, height=15.0)
        self.Member1_HElementary_School.place(x=599.0, y=333.0, width=100.0, height=15.0)
        self.Member1_HVocational.place(x=479.0, y=350.0, width=100.0, height=15.0)
        self.Member1_HNone.place(x=603.0, y=350.0, width=60.0, height=15.0)

        self.combobox.place(x=70.0, y=153.0, width=672.0, height=30.0)
        self.combobox.config(state="readonly")


#SHOW THE WIDGETS
    def back_page(self):
        #HIDE THE WIDGETS PAGE 2
        for image_id in self.entryImage2:
            self.itemconfigure(image_id, state="hidden")
        for text_id in self.textImage2:
            self.itemconfigure(text_id, state="hidden")
        for bg_id in self.backgroundImage2:
            self.itemconfigure(bg_id, state="hidden")

        self.Member1_HName.place_forget()
        self.Member1_HAge.place_forget()
        self.Member1_HRelation.place_forget()
        self.Member1_HOccupation.place_forget()
        self.Member1_HMonthlyincome.place_forget()

        self.Member1_HSingle.place_forget()
        self.Member1_HWidow.place_forget()
        self.Member1_HMarried.place_forget()
        self.Member1_HSeparated.place_forget()
        self.Member1_HWithPartner.place_forget()

        self.Member1_HPost_Graduate.place_forget()
        self.Member1_HHigh_School.place_forget()
        self.Member1_HVocational.place_forget()
        self.Member1_HElementary_School.place_forget()
        self.Member1_HCollege.place_forget()
        self.Member1_HNone.place_forget()

        self.Member2_HName.place_forget()
        self.Member2_HAge.place_forget()
        self.Member2_HRelation.place_forget()
        self.Member2_HOccupation.place_forget()
        self.Member2_HMonthlyincome.place_forget()

        self.Member2_HSingle.place_forget()
        self.Member2_HWidow.place_forget()
        self.Member2_HMarried.place_forget()
        self.Member2_HSeparated.place_forget()
        self.Member2_HWithPartner.place_forget()

        self.Member2_HPost_Graduate.place_forget()
        self.Member2_HHigh_School.place_forget()
        self.Member2_HVocational.place_forget()
        self.Member2_HElementary_School.place_forget()
        self.Member2_HCollege.place_forget()
        self.Member2_HNone.place_forget()

        self.addButton.place_forget()
        self.deleteButton.place_forget()
        self.backButton.place_forget()
        self.submitButton.place_forget()

        self.combobox.place_forget()

        for image_id in self.entryImage:
            self.itemconfigure(image_id, state="normal")
        for text_id in self.textImage:
            self.itemconfigure(text_id, state="normal")
        for bg_id in self.backgroundImage:
            self.itemconfigure(bg_id, state="normal")
            
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
        self.N0ne.place(x=674.0, y=348.0, width=60.0, height=15.0)

        self.homeButton.place(x=7.0, y=3.0, width=30.0, height=29.0)
        self.nextButton.place(x=645.0, y=451.0, width=125.0, height=26.515151977539062)

    def checkCombobox(self, current_list, previous_list):
        if current_list == previous_list:
            return False
        else:
            return True


    def commit_data(self):
        
        if not self.checkCombobox(self.householdMember, ["Member 1", "Member 2"]):
            messagebox.showerror("Error", "Please add a household member first before submitting.")
            return
        else:
            pass

        try:
            applicantFields = [
            self.FullName.get(),
            self.PermanentAddress.get(),
            self.CivilStatus.get(),
            self.Birthdate.get(),
            self.Age.get(),
            self.Sex.get(),
            self.Nationality.get(),
            self.Religion.get(),
            self.EducationalAttainment.get(),
            self.Occupation.get(),
            self.MonthlyIncome.get(),
            self.Membership.get(),
            self.OtherSourceOfIncome.get(),
            self.MonthlyExpenditure.get(),
            self.GrossMonthlyIncome.get(),
            self.NetMonthlyIncome.get(),
            self.ReferenceNo.get(),
            self.Date.get(),
            self.ApplicantStatus.get()
            ]
            # Insert applicant and reference details
            if all(applicantFields):
                self.database.insert_applicant_and_reference_details(
                    self.FullName.get(),
                    self.PermanentAddress.get(),
                    self.CivilStatus.get(),
                    self.Birthdate.get(),
                    self.Age.get(),
                    self.Sex.get(),
                    self.Nationality.get(),
                    self.Religion.get(),
                    self.EducationalAttainment.get(),
                    self.Occupation.get(),
                    self.MonthlyIncome.get(),
                    self.Membership.get(),
                    self.OtherSourceOfIncome.get(),
                    self.MonthlyExpenditure.get(),
                    self.GrossMonthlyIncome.get(),
                    self.NetMonthlyIncome.get(),
                    self.ReferenceNo.get(),
                    self.Date.get(),
                    self.ApplicantStatus.get()
                )
            # TODO Put an If Else statement hereee
            self.InsertHousehold1()
            self.InsertHousehold2()


        except mysql.Error as err:  
            print(f"An error occurred: {err}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:    
            self.database.close_connection()
            self.switch_frame('applicanthomepage')


    def InsertApplicant(self):
        try:
            applicantFields = [
            self.FullName.get(),
            self.PermanentAddress.get(),
            self.CivilStatus.get(),
            self.Birthdate.get(),
            self.Age.get(),
            self.Sex.get(),
            self.Nationality.get(),
            self.Religion.get(),
            self.EducationalAttainment.get(),
            self.Occupation.get(),
            self.MonthlyIncome.get(),
            self.Membership.get(),
            self.OtherSourceOfIncome.get(),
            self.MonthlyExpenditure.get(),
            self.GrossMonthlyIncome.get(),
            self.NetMonthlyIncome.get(),
            self.ReferenceNo.get(),
            self.Date.get(),
            self.ApplicantStatus.get()
            ]
            # Insert applicant and reference details
            if all(applicantFields):
                self.database.insert_applicant_and_reference_details(
                    self.FullName.get(),
                    self.PermanentAddress.get(),
                    self.CivilStatus.get(),
                    self.Birthdate.get(),
                    self.Age.get(),
                    self.Sex.get(),
                    self.Nationality.get(),
                    self.Religion.get(),
                    self.EducationalAttainment.get(),
                    self.Occupation.get(),
                    self.MonthlyIncome.get(),
                    self.Membership.get(),
                    self.OtherSourceOfIncome.get(),
                    self.MonthlyExpenditure.get(),
                    self.GrossMonthlyIncome.get(),
                    self.NetMonthlyIncome.get(),
                    self.ReferenceNo.get(),
                    self.Date.get(),
                    self.ApplicantStatus.get()
                )
        except mysql.Error as err:  
            print(f"An error occurred: {err}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.switch_frame('applicanthomepage')

    def InsertHousehold1(self):

        self.HMember1Fields = [
            self.Member1_HName.get(), 
            self.Member1_HAge.get(), 
            self.Member1_HCivilStatus.get(), 
            self.Member1_HRelation.get(), 
            self.Member1_HEducationalAttainment.get(), 
            self.Member1_HOccupation.get(), 
            self.Member1_HMonthlyincome.get()
            ]
            
        try:
            # Insert household details
            if all(self.HMember1Fields):
                self.database.insert_household_details(
                    self.Member1_HName.get(),  # Hname
                    self.Member1_HAge.get(),  # Hage
                    self.Member1_HCivilStatus.get(),  # HCivilStatus
                    self.Member1_HRelation.get(),  # Hrelation
                    self.Member1_HEducationalAttainment.get(),  # HHighestEducationalAttainment
                    self.Member1_HOccupation.get(),  # Hoccupation
                    self.Member1_HMonthlyincome.get()  # Hmonthlyincome
                    )
            else:
                print("No Household Member 1 inputted.")
                
        except mysql.Error as err:
            print(f"An error occurred: {err}")



    def InsertHousehold2(self):

        self.HMember2Fields = [
            self.Member2_HName.get(), 
            self.Member2_HAge.get(), 
            self.Member2_HCivilStatus.get(), 
            self.Member2_HRelation.get(), 
            self.Member2_HEducationalAttainment.get(), 
            self.Member2_HOccupation.get(), 
            self.Member2_HMonthlyincome.get()
            ]
        
        try:
            if all(self.HMember2Fields):
                self.database.insert_household_details(
                    self.Member2_HName.get(),  # Hname
                    self.Member2_HAge.get(),  # Hage
                    self.Member2_HCivilStatus.get(),  # HCivilStatus
                    self.Member2_HRelation.get(),  # Hrelation
                    self.Member2_HEducationalAttainment.get(),  # HHighestEducationalAttainment
                    self.Member2_HOccupation.get(),  # Hoccupation
                    self.Member2_HMonthlyincome.get()  # Hmonthlyincome
                    )   
                self.database.close_connection()
                
            else:
                print("No Household Member 2 inputted.")

        except mysql.Error as err:
            print(f"An error occurred: {err}")





    def get_reference_id(self):
        # Call get_last_reference_id from DatabaseHandler instance
        reference_id = self.database.get_last_reference_id()
        self.ReferenceNo.delete(0, 'end')  # Clear previous content if any
        self.ReferenceNo.insert(0, reference_id)
        print(f"Fetched Reference ID: {reference_id}")
        return reference_id
    

    def backtoHome(self):
        print("Back to Home")
        if self.switch_frame:
            print("Switching to Home")
            self.switch_frame('applicanthomepage')
        else:
            print("Switch frame not none")


        
       

    
