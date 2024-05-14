from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\CODER\IM_PROJECT\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("643x350")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=311,
    width=643,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas.create_rectangle(
    64.0,
    3.0,
    460.0,
    50.0,
    fill="#FFFFFF",
    outline=""
)

# Load the image
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_width = image_image_1.width()
canvas_width = 643

# Center the image
image_x = canvas_width / 2
image_1 = canvas.create_image(
    image_x,
    30.0,
    image=image_image_1
)

canvas_width = 460.0
canvas_height = 50.0

canvas.create_text(
    canvas_width / 2,
    canvas_height / 2,
    anchor="center",
    text="Household Details",
    fill="#000000",
    font=("InknutAntiqua Regular", 17 * -1)
)

# First Name
canvas.create_text(
    40.0,
    80.0,
    anchor="nw",
    text="Firstname",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_1 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(x=40.0, y=100.0, width=130.0, height=20.0)

# Last Name
canvas.create_text(
    200.0,
    80.0,
    anchor="nw",
    text="Lastname",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_2 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(x=200.0, y=100.0, width=130.0, height=20.0)

# Middle Name
canvas.create_text(
    360.0,
    80.0,
    anchor="nw",
    text="Middlename",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_3 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(x=360.0, y=100.0, width=130.0, height=20.0)

# Address
canvas.create_text(
    40.0,
    130.0,
    anchor="nw",
    text="Address",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_4 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(x=40.0, y=150.0, width=290.0, height=20.0)

# Relationship
canvas.create_text(
    360.0,
    130.0,
    anchor="nw",
    text="Relationship",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_3 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
) 
entry_3.place(x=360.0, y=150.0, width=130.0, height=20.0)

# Contact Number
canvas.create_text(
    40.0,
    180.0,
    anchor="nw",
    text="Contact Number",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_5 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(x=40.0, y=200.0, width=130.0, height=20.0)

# Civil Status
canvas.create_text(
    200.0,
    180.0,
    anchor="nw",
    text="Civil Status",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_6 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(x=200.0, y=200.0, width=130.0, height=20.0)

# Birthdate
canvas.create_text(
    360.0,
    180.0,
    anchor="nw",
    text="Birthdate (mm/dd/yyyy)",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_7 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(x=360.0, y=200.0, width=130.0, height=20.0)

# Sex
canvas.create_text(
    40.0,
    230.0,
    anchor="nw",
    text="Sex",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_8 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(x=40.0, y=250.0, width=130.0, height=20.0)

# Nationality
canvas.create_text(
    200.0,
    230.0,
    anchor="nw",
    text="Nationality",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_9 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(x=200.0, y=250.0, width=130.0, height=20.0)

# Religion
canvas.create_text(
    360.0,
    230.0,
    anchor="nw",
    text="Religion",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_10 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(x=360.0, y=250.0, width=130.0, height=20.0)

# Education
canvas.create_text(
    40.0,
    280.0,
    anchor="nw",
    text="Highest Educational Attainment",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_11 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(x=40.0, y=300.0, width=200.0, height=20.0)

# Residence
canvas.create_text(
    260.0,
    280.0,
    anchor="nw",
    text="Residence",
    fill="#000000",
    font=("InknutAntiqua Regular", 8 * -1)
)
entry_12 = Entry(
    bd=0,
    bg="#FFF4F4",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(x=260.0, y=300.0, width=100.0, height=20.0)



# Button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(x=520.0, y=300.0, width=84.0, height=20.0)

window.resizable(False, False)
window.mainloop()
