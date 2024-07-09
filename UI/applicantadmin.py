import tkinter as tk
from tkinter import PhotoImage
from resources.FileTracker.tracker import resource_path

class ApplicantAdmin(tk.Canvas):
    def __init__(self, master=None, switch_frame=None):
        super().__init__(master, height=500, width=820, bg="#FFFFFF", highlightthickness=0)

        self.switch_frame = switch_frame  # Reference to the switch_frame method of the main app


        self.GradiantBg = PhotoImage(file=resource_path("resources/applicantadmin/landingPagebg.png"))
        #self.welcomText = PhotoImage(file=resource_path("resources/applicantadmin/WelcomeText.png"))
        self.pcsioText = PhotoImage(file=resource_path("resources/applicantadmin/pcsio_text.png"))
        self.loginBg = PhotoImage(file=resource_path("resources/applicantadmin/loginBG.png"))
        self.Logo = PhotoImage(file=resource_path("resources/applicantadmin/Logo.png"))
        self.applicantButton = PhotoImage(file=resource_path("resources/applicantadmin/applicantButton.png"))
        self.adminButton = PhotoImage(file=resource_path("resources/applicantadmin/adminButton.png"))
        self.applicangButtonBG = PhotoImage(file=resource_path("resources/applicantadmin/blueBG.png"))
        self.adminButtonBG = PhotoImage(file=resource_path("resources/applicantadmin/redBG.png"))
        self.destinationText = PhotoImage(file=resource_path("resources/applicantadmin/destination_text.png"))


        self.create_image(410.0, 250.0, image=self.GradiantBg)
        #self.create_image(300.0, 250, image=self.welcomText)
        self.create_image(300.0, 250.0, image=self.pcsioText)
        self.create_image(600.0, 250.0, image=self.loginBg)
        self.create_image(610.0, 180.0, image=self.Logo)
        self.create_image(600.0, 305.0, image=self.adminButtonBG)
        self.create_image(600.0, 265.0, image=self.applicangButtonBG)

        #self.create_text(500.0, 210.0, anchor="nw", text="Please click you destination", fill="#000000", font=("Nokora", 17 * -1))
        self.create_image(603.0, 220.0, image=self.destinationText)

        self.ApplicantButton = tk.Button(self, image=self.applicantButton, borderwidth=0, highlightthickness=0, command=self.gotoLogin, relief="flat")
        self.ApplicantButton.place(x=475.0, y=257.0, width=250.0, height=25.0)

        self.AdminButton = tk.Button(self, image=self.adminButton, borderwidth=0, highlightthickness=0, command=self.gotoAdminLogin, relief="flat")
        self.AdminButton.place(x=475.0, y=298.0, width=250.0, height=25.0)


  



    def gotoAdminLogin(self):
        if self.switch_frame:
            self.switch_frame('adminlogin')

    def gotoLogin(self):
        if self.switch_frame:
            self.switch_frame('login')
