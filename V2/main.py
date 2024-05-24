from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import mysql.connector as mysql
from mysql_connection import DatabaseConnection

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="practice"
    )

class Applicant_Details_GUI:

    def __init__(self):
        self.applicant_details = DatabaseConnection()  # Create an instance of the Applicant_Details class

    # Commit data function
    def commit_data(self):
        data = {
            "Application_Status": entry_17.get(),
            "Full_Name": entry_16.get(),
            "Address": entry_15.get(),
            "Civil_Status": entry_14.get(),
            "Birth_Date": entry_13.get(),
            "Age": entry_12.get(),
            "Nationality": entry_11.get(),
            "Religion": entry_10.get(),
            "Sex": entry_9.get(),
            "Highest_Educ_Attainment": entry_8.get(),
            "Membership": entry_7.get(),
            "Occupation": entry_6.get(),
            "Monthly_Income": entry_5.get(),
            "OtherSourceOfIncome": entry_4.get(),
            "Monthly_Expenditures": entry_3.get(),
            "GrossMonthlyIncome": entry_2.get(),
            "NetMonthlyIncome": entry_1.get(),
        }

        try:
            # Create an instance of the Applicant_Details class
            applicant_details = DatabaseConnection()
            applicant_details.insert(**data)
        except mysql.Error as err:
          print(f"Error: {err}")

# Define paths and constants
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"

# Window dimensions
WINDOW_WIDTH = 1066
WINDOW_HEIGHT = 441

# Colors
BACKGROUND_COLOR = "#FFFFFF"
ENTRY_BACKGROUND = "#FFF4F4"
ENTRY_FOREGROUND = "#000716"

# Font settings
FONT_FAMILY = "InknutAntiqua Regular"
FONT_SIZE = 13

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_entry(canvas, x, y, width, height, image_path):
    entry_image = PhotoImage(file=relative_to_assets(image_path))
    canvas.create_image(x + width / 2, y + height / 2, image=entry_image)
    entry = Entry(
        bd=0,
        bg=ENTRY_BACKGROUND,
        fg=ENTRY_FOREGROUND,
        highlightthickness=0
    )
    entry.place(x=x, y=y, width=width, height=height)
    return entry

def create_text(canvas, x, y, text):
    canvas.create_text(
        x, y,
        anchor="nw",
        text=text,
        fill="#000000",
        font=(FONT_FAMILY, FONT_SIZE * -1)
    )
def quit():
    window.quit()

# Main Window Setup
window = Tk()
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.title("My Application Window")
window.configure(bg=BACKGROUND_COLOR)

canvas = Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=WINDOW_HEIGHT,
    width=WINDOW_WIDTH,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Entry Fields
entries_info = [
    (749, 230, 271, 16, "entry_1.png", "Net Monthly Income"),
    (749, 200, 271, 16, "entry_2.png", "Gross Monthly Income"),
    (749, 172, 271, 16, "entry_3.png", "Monthly Expenditures"),
    (749, 144, 271, 16, "entry_4.png", "Other Sources Of Income"),
    (749, 114, 271, 16, "entry_5.png", "Monthly Income"),
    (749, 86, 271, 16, "entry_6.png", "Occupation"),
    (232, 372, 271, 16, "entry_7.png", "Membership"),
    (232, 344, 271, 16, "entry_8.png", "Educational Attainment"),
    (232, 258, 271, 16, "entry_9.png", "Sex"),
    (232, 316, 271, 16, "entry_10.png", "Religion"),
    (232, 286, 271, 16, "entry_11.png", "Nationality"),
    (232, 230, 271, 16, "entry_12.png", "Age"),
    (232, 200, 271, 16, "entry_13.png", "Birthdate"),
    (232, 172, 271, 16, "entry_14.png", "Civil Status"),
    (232, 144, 271, 16, "entry_15.png", "Address"),
    (232, 114, 271, 16, "entry_16.png", "Full Name"),
    (232, 86, 271, 16, "entry_17.png", "Application Status"),
]

entry_widgets = []

for x, y, width, height, img, label in entries_info:
    entry_widgets.append(create_entry(canvas, x, y, width, height, img))
    create_text(canvas, x - 170, y - 4, label)

entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17 = entry_widgets

# Buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Applicant_Details_GUI().commit_data,  # Call the commit_data method of Applicant_Details_GUI instance
    relief="flat"
)
button_1.place(x=958, y=380, width=62, height=34)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,
    relief="flat"
)
button_2.place(x=892, y=380, width=62, height=34)

# Header Text
canvas.create_text(
    193, 11,
    anchor="nw",
    text="INDIVIDUAL MEDICAL ASSISTANCE PROGRAM (IMAP)",
    fill="#000000",
    font=(FONT_FAMILY, 16 * -1)
)

window.resizable(False, False)
window.mainloop()
