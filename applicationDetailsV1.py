#SAMPLE GUI APPLICATION FOR PCSO APPLICATION
import tkinter as tk
from tkinter import ttk

def submit():

    full_name = entry_full_name.get()
    address = entry_address.get()
    civil_status = entry_civil_status.get()
    birthdate = entry_birthdate.get()
    sex = entry_sex.get()
    nationality = entry_nationality.get()
    religion = entry_religion.get()
    occupation = entry_occupation.get()
    

    print(f"Full Name: {full_name}")
    print(f"Address: {address}")
    print(f"Civil Status: {civil_status}")
    print(f"Birthdate: {birthdate}")
    print(f"Sex: {sex}")
    print(f"Nationality: {nationality}")
    print(f"Religion: {religion}")
    print(f"Occupation: {occupation}")


root = tk.Tk()
root.title("PCSO Application")

title_label = tk.Label(root, text="PCSO Application", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)


labels = ["Full Name", "Address", "Civil Status", "Birthdate", "Sex", "Nationality", "Religion", "Occupation"]
entries = {}

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky=tk.E)
    
    entry = tk.Entry(root, width=50)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    
    entries[label_text] = entry


entry_full_name = entries["Full Name"]
entry_address = entries["Address"]
entry_civil_status = entries["Civil Status"]
entry_birthdate = entries["Birthdate"]
entry_sex = entries["Sex"]
entry_nationality = entries["Nationality"]
entry_religion = entries["Religion"]
entry_occupation = entries["Occupation"]


submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=len(labels) + 1, columnspan=2, pady=10)


root.mainloop()
