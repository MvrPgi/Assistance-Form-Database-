import tkinter as tk
from UI.applicantadmin import ApplicantAdmin
from UI.adminBench import AdminBench
from UI.applicantHomepage import ApplicantHomepage
from UI.login import Login
from UI.register import Register
from UI.signup import Signup
from UI.adminlogin import AdminLogin
from UI.adminHomepage import AdminHomepage
from UI.HouseHoldTable import AdminBenchHousehold
from UI.ApplicantTable import ApplicantTable
from UI.referenceTable import AdminBenchReference



import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PCSOIA PORTAL")
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
        if self.current_frame is not None:
            # Clear Entry widgets
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0, tk.END)
            self.current_frame.destroy()
            self.current_frame = None
        else:
            print("No current frame to destroy.")

    def switch_frame(self, frame_name):
        print(f"Switching to frame: {frame_name}")
        self.clear_frame()

        if frame_name == 'applicantadmin':
            self.current_frame = ApplicantAdmin(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'adminhomepage':
            self.current_frame = AdminHomepage(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'adminbench':
            self.withdraw()  # Hide the main window
            admin_bench_window = AdminBench(master=self)
            admin_bench_window.mainloop()
        elif frame_name == 'household':
            self.withdraw()  # Hide the main window
            admin_bench_window = AdminBenchHousehold(master=self)
            admin_bench_window.mainloop()
        elif frame_name == 'applicant':
            self.withdraw()  # Hide the main window
            admin_bench_window = ApplicantTable(master=self)
            admin_bench_window.mainloop()
        elif frame_name == 'reference':
            self.withdraw()
            admin_bench_window = AdminBenchReference(master=self)
            admin_bench_window.mainloop()
        elif frame_name =='applicanthomepage':
            self.current_frame = ApplicantHomepage(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'register':
            self.current_frame = Register(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'login':
            self.current_frame = Login(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'adminlogin':
            self.current_frame = AdminLogin(master=self.main_frame, switch_frame=self.switch_frame)
        elif frame_name == 'signup':
            self.current_frame = Signup(master=self.main_frame, switch_frame=self.switch_frame)
        else:
            print(f"Frame '{frame_name}' not recognized.")
            return

        if self.current_frame is not None:
            self.current_frame.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    app = App()
    app.mainloop()



