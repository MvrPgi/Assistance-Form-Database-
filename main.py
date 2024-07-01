from UI.applicantadmin import ApplicantAdmin
from UI.adminlogin import AdminLogin
from UI.adminBench import AdminBench
from UI.login import Login
from UI.register import Register
from UI.signup import Signup

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
       
        self.title("Main App")
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.geometry("820x500")
        self.resizable(False, False)
        

        self.configure(bg="#FFFFFF")
        self.open_admin_bench_button = tk.Button(self, text="Open Admin Bench", command=self.open_admin_bench)
        self.open_admin_bench_button.pack(pady=20)
        self.open_register_button = tk.Button(self, text="Open Register", command=self.open_register)
        self.open_register_button.pack(pady=20)
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)
        self.adminLogin_button = tk.Button(self, text="Admin Login", command=self.adminLogin)
        self.adminLogin_button.pack(pady=20)
        self.applicant_admin_button = tk.Button(self, text="Applicant Admin", command=self.open_applicant_admin)
        self.applicant_admin_button.pack(pady=20)
        self.signup_button = tk.Button(self, text="Signup", command=self.signup)
        self.signup_button.pack(pady=20)
        
        # self.HomePage = ApplicantAdmin(master=self.main_frame)
        # self.HomePage.pack(fill=tk.BOTH, expand=True)

        


    def open_admin_bench(self):
        self.withdraw()
        admin_bench_window = AdminBench()
        admin_bench_window.mainloop()



    def adminLogin(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = AdminLogin(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)

    def open_applicant_admin(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = ApplicantAdmin(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)
    
    def login(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = Login(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)



    def open_register(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = Register(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)

    def signup(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = Signup(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)
    
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()
