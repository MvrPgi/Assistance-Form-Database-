from UI.register import Register
import tkinter as tk




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Main App")
        self.geometry("820x500")
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")
        

        self.register = Register(self)
        self.register.place(x=0, y=0)




if __name__ == "__main__":
    app = App()
    app.mainloop()
