import tkinter as tk
from mysql_connection import DatabaseConnection

root = tk.Tk()
root.title("PCSO Application")

# Instantiate the DatabaseConnection class
db_connection = DatabaseConnection()

def submit():
    # Collect data from GUI inputs
    ref_no = ref_entries["Ref No"].get()
    applicant_status = ref_entries["Applicant Status"].get()
    date = ref_entries["Date"].get()
    full_name = app_entries["Full Name"].get()
    address = app_entries["Address"].get()
    civil_status = app_entries["Civil Status"].get()
    birthdate = app_entries["Birthdate"].get()
    sex = app_entries["Sex"].get()
    nationality = app_entries["Nationality"].get()
    religion = app_entries["Religion"].get()
    occupation = app_entries["Occupation"].get()
    hhold_fam_name = hhold_entries["Family Name"].get()
    hhold_fam_age = hhold_entries["Family Age"].get()
    hhold_fam_civil_status = hhold_entries["Family Civil Status"].get()
    hhold_fam_rs_with_patient = hhold_entries["Relationship with Patient"].get()
    hhold_fam_highest_educ_attain = hhold_entries["Highest Education Attainment"].get()
    hhold_fam_occupation = hhold_entries["Family Occupation"].get()
    hhold_fam_monthly_income = hhold_entries["Family Monthly Income"].get()

    # Insert reference information into the database
    db_connection.insert(
        ref_no, date, applicant_status
    )

    # Insert applicant information into the database
    db_connection.insert(
        full_name, address, civil_status, birthdate, sex, nationality, religion, occupation
    )

    # Insert household family information into the database
    db_connection.insert(
        hhold_fam_name, hhold_fam_age, hhold_fam_civil_status, hhold_fam_rs_with_patient,
        hhold_fam_highest_educ_attain, hhold_fam_occupation, hhold_fam_monthly_income
    )


title_label = tk.Label(root, text="PCSO Application", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Reference Information
ref_labels = ["Ref No", "Applicant Status", "Date"]  
ref_entries = {}

for i, label_text in enumerate(ref_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky=tk.E)
    
    entry = tk.Entry(root, width=50)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    
    ref_entries[label_text] = entry

# Applicant Information
app_labels = ["Full Name", "Address", "Civil Status", "Birthdate", "Sex", "Nationality", "Religion", "Occupation"]
app_entries = {}

for i, label_text in enumerate(app_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + 1, column=2, padx=10, pady=5, sticky=tk.E)
    
    entry = tk.Entry(root, width=50)
    entry.grid(row=i + 1, column=3, padx=10, pady=5)
    
    app_entries[label_text] = entry

# Household Family Information
hhold_labels = ["Family Name", "Family Age", "Family Civil Status", "Relationship with Patient", "Highest Education Attainment", "Family Occupation", "Family Monthly Income"]
hhold_entries = {}

for i, label_text in enumerate(hhold_labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i + len(app_labels) + 2, column=0, padx=10, pady=5, sticky=tk.E)
    
    entry = tk.Entry(root, width=50)
    entry.grid(row=i + len(app_labels) + 2, column=1, padx=10, pady=5)
    
    hhold_entries[label_text] = entry

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=len(app_labels) + len(hhold_labels) + 3, column=0, columnspan=4, pady=10)

root.mainloop()
