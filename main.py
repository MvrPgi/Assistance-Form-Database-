from UI.register import Register
from UI.login import Login
from UI.adminlogin import AdminLogin
from UI.adminBench import AdminBench

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



    def open_register(self):
        # Clear the main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create and pack Register canvas into the main_frame
        register_canvas = Register(master=self.main_frame)
        register_canvas.pack(fill=tk.BOTH, expand=True)


    def open_admin_bench(self):
        self.withdraw()
        admin_bench_window = AdminBench()
        admin_bench_window.mainloop()


        
if __name__ == "__main__":
    app = App()
    app.mainloop()
