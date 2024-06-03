

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\Coder\IM_PROJECT\V3\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("820x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    9.0,
    11.0,
    850.0,
    82.0,
    fill="#3F95E4",
    outline="")

canvas.create_text(
    89.0,
    7.0,
    anchor="nw",
    text="PCSO IMAP\nAPPLICATION",
    fill="#FFFFFF",
    font=("Mada Black", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    42.0,
    28.0,
    image=image_image_1
)

canvas.create_text(
    548.0,
    125.0,
    anchor="nw",
    text="New Applicant",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_text(
    650.0,
    124.0,
    anchor="nw",
    text="Old Applicant",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_rectangle(
    533.036865234375,
    124.3037109375,
    647.0,
    137.3037109375,
    fill="#000000",
    outline="")

canvas.create_text(
    535.0,
    109.0,
    anchor="nw",
    text="Applicant  Status:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_text(
    388.0,
    205.0,
    anchor="nw",
    text="First Name",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    413.0,
    195.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=53.0,
    y=187.0,
    width=720.0,
    height=15.0
)

canvas.create_text(
    91.0,
    202.0,
    anchor="nw",
    text="Surname",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    694.0,
    204.0,
    anchor="nw",
    text="Middle Name",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    53.0,
    173.0,
    anchor="nw",
    text="Full Name of the Patient:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    412.0,
    237.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=52.0,
    y=229.0,
    width=720.0,
    height=15.0
)

canvas.create_text(
    65.0,
    245.0,
    anchor="nw",
    text="No.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    104.0,
    245.0,
    anchor="nw",
    text="Street.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    152.0,
    245.0,
    anchor="nw",
    text="Barangay",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    291.0,
    245.0,
    anchor="nw",
    text="Municipality/City",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    521.0,
    245.0,
    anchor="nw",
    text="Province",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    699.0,
    245.0,
    anchor="nw",
    text="Region",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    52.0,
    215.0,
    anchor="nw",
    text="Permanent Address:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    412.0,
    237.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=52.0,
    y=229.0,
    width=720.0,
    height=15.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    128.5,
    314.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=53.0,
    y=306.0,
    width=151.0,
    height=15.0
)

canvas.create_text(
    65.0,
    245.0,
    anchor="nw",
    text="No.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    104.0,
    245.0,
    anchor="nw",
    text="Street.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    152.0,
    245.0,
    anchor="nw",
    text="Barangay",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    291.0,
    245.0,
    anchor="nw",
    text="Municipality/City",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    521.0,
    245.0,
    anchor="nw",
    text="Province",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    699.0,
    245.0,
    anchor="nw",
    text="Region",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    52.0,
    215.0,
    anchor="nw",
    text="Permanent Address:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_text(
    52.0,
    294.0,
    anchor="nw",
    text="Birthdate:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    130.5,
    349.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=55.0,
    y=341.0,
    width=151.0,
    height=15.0
)

canvas.create_text(
    54.0,
    329.0,
    anchor="nw",
    text="Nationality:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    107.0,
    435.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=53.0,
    y=427.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    52.0,
    415.0,
    anchor="nw",
    text="Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    244.0,
    434.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=190.0,
    y=426.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    189.0,
    414.0,
    anchor="nw",
    text="Other Source of Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    300.5,
    348.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=225.0,
    y=340.0,
    width=151.0,
    height=15.0
)

canvas.create_text(
    224.0,
    328.0,
    anchor="nw",
    text="Religion:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    423.5,
    391.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=348.0,
    y=383.0,
    width=151.0,
    height=15.0
)

canvas.create_text(
    348.0,
    370.0,
    anchor="nw",
    text="Occupation:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    286.5,
    314.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=227.0,
    y=306.0,
    width=119.0,
    height=15.0
)

canvas.create_text(
    226.0,
    294.0,
    anchor="nw",
    text="Age:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_rectangle(
    52.0,
    151.0,
    172.0,
    164.0,
    fill="#84BBEE",
    outline="")

canvas.create_text(
    61.0,
    151.0,
    anchor="nw",
    text="Applicant Information",
    fill="#000000",
    font=("Mada Bold", 10 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    413.00000324418534,
    77.0,
    image=image_image_2
)

canvas.create_text(
    292.0,
    109.0,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_rectangle(
    292.0,
    123.0,
    509.0,
    140.0,
    fill="#000000",
    outline="")

canvas.create_text(
    53.0,
    109.0,
    anchor="nw",
    text="Reference No:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_rectangle(
    53.0,
    123.0,
    270.0,
    140.0,
    fill="#000000",
    outline="")

canvas.create_text(
    53.0,
    109.0,
    anchor="nw",
    text="Reference No:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    161.5,
    131.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=53.0,
    y=123.0,
    width=217.0,
    height=15.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    300.0,
    76.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    520.836669921875,
    76.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    410.4183349609375,
    76.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    77.0,
    268.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    82.0,
    284.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    149.0,
    285.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    59.0,
    283.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    118.0,
    284.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    213.0,
    285.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    277.0,
    284.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    188.0,
    284.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    249.0,
    284.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    416.0,
    313.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    402.0,
    300.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    481.0,
    312.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    398.0,
    312.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    459.0,
    312.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    374.0,
    285.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    307.0,
    284.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    474.0,
    288.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    449.0,
    287.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    609.0,
    291.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    251.0,
    390.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    148.0,
    389.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    60.0,
    388.0,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    172.0,
    390.0,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    218.0,
    389.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    100.0,
    389.0,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    238.0,
    405.0,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    148.0,
    404.0,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    60.0,
    403.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    182.0,
    405.0,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    218.0,
    404.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    92.0,
    404.0,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    124.0,
    373.0,
    image=image_image_37
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    403.0,
    432.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=349.0,
    y=424.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    348.0,
    412.0,
    anchor="nw",
    text="Monthly Expenditures:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    559.0,
    431.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=505.0,
    y=423.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    504.0,
    411.0,
    anchor="nw",
    text="Gross Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    713.0,
    430.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=659.0,
    y=422.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    658.0,
    410.0,
    anchor="nw",
    text="Net Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    724.0,
    391.0,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    617.0,
    389.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    559.0,
    390.0,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    654.0,
    390.0,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    692.0,
    390.0,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    586.0,
    391.0,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    581.0,
    375.0,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    303.0,
    78.0,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    414.0,
    78.0,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    524.0,
    78.0,
    image=image_image_47
)

canvas.create_text(
    256.0,
    94.0,
    anchor="nw",
    text="Applicant Information",
    fill="#000000",
    font=("Mada Regular", 8 * -1)
)

canvas.create_text(
    364.0,
    94.0,
    anchor="nw",
    text="Household Information",
    fill="#000000",
    font=("Mada Regular", 8 * -1)
)

canvas.create_text(
    498.0,
    95.0,
    anchor="nw",
    text="Verification",
    fill="#000000",
    font=("Mada Regular", 8 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=667.0,
    y=459.0,
    width=105.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
