import tkinter as tk
from UI.applicantadmin import ApplicantAdmin
from UI.adminBench import AdminBench
from UI.login import Login
from UI.register import Register
from UI.signup import Signup
from UI.adminlogin import AdminLogin

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main App")
        self.geometry("820x500")
        self.resizable(False, False)

        # Initialize main frame
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Start with the ApplicantAdmin frame
        self.current_frame = None
        self.switch_frame('applicantadmin')


    def clear_frame(self):
        print("Clearing frame...")
        # Clear the main_frame and destroy current frame
        if self.current_frame is not None:
            print(f"Destroying current frame: {self.current_frame.__class__.__name__}")
            self.current_frame.destroy()
        else:
            print("No current frame to destroy.")

    def switch_frame(self, frame_name):
        print(f"Switching to frame: {frame_name}")
        self.clear_frame()

        if frame_name == 'applicantadmin':
            self.current_frame = ApplicantAdmin(master=self.main_frame, switch_frame=self.switch_frame)
            self.current_frame.pack(fill=tk.BOTH, expand=True)
        elif frame_name == 'adminbench':
            self.withdraw()  # Hide the main window
            admin_bench_window = AdminBench(master=self)
            admin_bench_window.mainloop()
        elif frame_name == 'register':
            self.current_frame = Register(master=self.main_frame, switch_frame=self.switch_frame)
            self.current_frame.pack(fill=tk.BOTH, expand=True)
        elif frame_name == 'login':
            self.current_frame = Login(master=self.main_frame, switch_frame=self.switch_frame)
            self.current_frame.pack(fill=tk.BOTH, expand=True)
        elif frame_name == 'adminlogin':
            self.current_frame = AdminLogin(master=self.main_frame, switch_frame=self.switch_frame)
            self.current_frame.pack(fill=tk.BOTH, expand=True)
        elif frame_name == 'signup':
            self.current_frame = Signup(master=self.main_frame, switch_frame=self.switch_frame)
            self.current_frame.pack(fill=tk.BOTH, expand=True)
        else:
            print(f"Frame '{frame_name}' not recognized.")
            return

if __name__ == "__main__":
    app = App()
    app.mainloop()