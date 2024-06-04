
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\Coder\IM_PROJECT\resources\APP_1")

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    429.0,
    46.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    577.0,
    132.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    677.0,
    131.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    586.036865234375,
    130.3037109375,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    570.0,
    116.0,
    image=image_image_5
)

canvas.create_text(
    385.0,
    205.0,
    anchor="nw",
    text="First Name",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    410.0,
    195.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=54.0,
    y=187.0,
    width=712.0,
    height=15.0
)

canvas.create_text(
    87.0,
    203.0,
    anchor="nw",
    text="Surname",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    691.0,
    204.0,  
    anchor="nw",
    text="Middle Name",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    50.0,
    173.0,
    anchor="nw",
    text="Full Name of the Patient:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    409.0,
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
    x=49.0,
    y=229.0,
    width=720.0,
    height=15.0
)

canvas.create_text(
    62.0,
    245.0,
    anchor="nw",
    text="No.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    101.0,
    245.0,
    anchor="nw",
    text="Street.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    149.0,
    245.0,
    anchor="nw",
    text="Barangay",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    288.0,
    245.0,
    anchor="nw",
    text="Municipality/City",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    518.0,
    245.0,
    anchor="nw",
    text="Province",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    696.0,
    245.0,
    anchor="nw",
    text="Region",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    49.0,
    215.0,
    anchor="nw",
    text="Permanent Address:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    409.0,
    237.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=53.0,
    y=229.0,
    width=712.0,
    height=15.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    125.5,
    314.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=54.0,
    y=306.0,
    width=143.0,
    height=15.0
)

canvas.create_text(
    62.0,
    245.0,
    anchor="nw",
    text="No.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    101.0,
    245.0,
    anchor="nw",
    text="Street.",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    149.0,
    245.0,
    anchor="nw",
    text="Barangay",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    288.0,
    245.0,
    anchor="nw",
    text="Municipality/City",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    518.0,
    245.0,
    anchor="nw",
    text="Province",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    696.0,
    245.0,
    anchor="nw",
    text="Region",
    fill="#000000",
    font=("Mada Regular", 6 * -1)
)

canvas.create_text(
    49.0,
    215.0,
    anchor="nw",
    text="Permanent Address:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

canvas.create_text(
    49.0,
    294.0,
    anchor="nw",
    text="Birthdate:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    127.5,
    349.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=56.0,
    y=341.0,
    width=143.0,
    height=15.0
)

canvas.create_text(
    51.0,
    329.0,
    anchor="nw",
    text="Nationality:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    104.0,
    435.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=50.0,
    y=427.0,
    width=108.0,
    height=15.0
)

canvas.create_text(
    49.0,
    415.0,
    anchor="nw",
    text="Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    241.0,
    434.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=191.0,
    y=426.0,
    width=100.0,
    height=15.0
)

canvas.create_text(
    186.0,
    414.0,
    anchor="nw",
    text="Other Source of Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    297.5,
    348.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=226.0,
    y=340.0,
    width=143.0,
    height=15.0
)

canvas.create_text(
    221.0,
    328.0,
    anchor="nw",
    text="Religion:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    420.5,
    391.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=349.0,
    y=383.0,
    width=143.0,
    height=15.0
)

canvas.create_text(
    345.0,
    370.0,
    anchor="nw",
    text="Occupation:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    283.5,
    314.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=228.0,
    y=306.0,
    width=111.0,
    height=15.0
)

canvas.create_text(
    223.0,
    294.0,
    anchor="nw",
    text="Age:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    122.0,
    157.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    410.00000324418534,
    77.0,
    image=image_image_7
)

canvas.create_text(
    289.0,
    109.0,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    397.5,
    131.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=292.0,
    y=123.0,
    width=211.0,
    height=15.0
)

canvas.create_text(
    50.0,
    109.0,
    anchor="nw",
    text="Reference No:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    158.5,
    131.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFF6E3",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=50.0,
    y=123.0,
    width=217.0,
    height=15.0
)

canvas.create_text(
    50.0,
    109.0,
    anchor="nw",
    text="Reference No:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    158.5,
    131.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=54.0,
    y=123.0,
    width=209.0,
    height=15.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    297.0,
    76.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    517.836669921875,
    76.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    407.4183349609375,
    76.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    74.0,
    268.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    79.0,
    284.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    146.0,
    285.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    56.0,
    283.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    115.0,
    284.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    210.0,
    285.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    274.0,
    284.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    185.0,
    284.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    246.0,
    284.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    413.0,
    313.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    399.0,
    300.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    478.0,
    312.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    395.0,
    312.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    456.0,
    312.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    371.0,
    285.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    304.0,
    284.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    471.0,
    288.0,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    446.0,
    287.0,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    606.0,
    291.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    248.0,
    390.0,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    145.0,
    389.0,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    57.0,
    388.0,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    169.0,
    390.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    215.0,
    389.0,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    97.0,
    389.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    235.0,
    405.0,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    145.0,
    404.0,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    57.0,
    403.0,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    179.0,
    405.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    215.0,
    404.0,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    89.0,
    404.0,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    121.0,
    373.0,
    image=image_image_42
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    400.0,
    432.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=350.0,
    y=424.0,
    width=100.0,
    height=15.0
)

canvas.create_text(
    345.0,
    412.0,
    anchor="nw",
    text="Monthly Expenditures:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    556.0,
    431.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=506.0,
    y=423.0,
    width=100.0,
    height=15.0
)

canvas.create_text(
    501.0,
    411.0,
    anchor="nw",
    text="Gross Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    710.0,
    430.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#FFE5AB",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=660.0,
    y=422.0,
    width=100.0,
    height=15.0
)

canvas.create_text(
    655.0,
    410.0,
    anchor="nw",
    text="Net Monthly Income:",
    fill="#000000",
    font=("Mada Regular", 10 * -1)
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    721.0,
    391.0,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    614.0,
    389.0,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    556.0,
    390.0,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    651.0,
    390.0,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    689.0,
    390.0,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    583.0,
    391.0,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=relative_to_assets("image_49.png"))
image_49 = canvas.create_image(
    578.0,
    375.0,
    image=image_image_49
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    300.0,
    78.0,
    image=image_image_50
)

image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    411.0,
    78.0,
    image=image_image_51
)

image_image_52 = PhotoImage(
    file=relative_to_assets("image_52.png"))
image_52 = canvas.create_image(
    521.0,
    78.0,
    image=image_image_52
)

canvas.create_text(
    253.0,
    94.0,
    anchor="nw",
    text="Applicant Information",
    fill="#000000",
    font=("Mada Bold", 8 * -1)
)

canvas.create_text(
    361.0,
    94.0,
    anchor="nw",
    text="Household Information",
    fill="#000000",
    font=("Mada Regular", 8 * -1)
)

canvas.create_text(
    495.0,
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
    x=664.0,
    y=459.0,
    width=105.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
