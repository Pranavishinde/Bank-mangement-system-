# import tkinter as tk
# from tkinter import messagebox

# # File storing account details
# ACCOUNT_FILE = "accounts.txt"

# def fetch_details():
#     """Fetches customer details from accounts.txt based on account number."""
#     account_number = account_var.get().strip()

#     try:
#         with open(ACCOUNT_FILE, "r") as file:
#             lines = file.readlines()
        
#         for line in lines:
#             data = line.strip().split(", ")
#             if data[0] == account_number:
#                 full_name_var.set(data[1])   # Full Name
#                 dob_var.set(data[2])         # Date of Birth
#                 phone_var.set(data[3])       # Phone Number
#                 account_type_var.set(data[4]) # Account Type
#                 return
        
#         messagebox.showerror("Error", "Account number not found!")
    
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Account file not found!")

# def update_account():
#     """Updates customer details in accounts.txt (except amount)."""
#     account_number = account_var.get().strip()

#     try:
#         with open(ACCOUNT_FILE, "r") as file:
#             lines = file.readlines()
        
#         updated_lines = []
#         found = False
#         for line in lines:
#             data = line.strip().split(", ")
#             if data[0] == account_number:
#                 # Keep account number & amount unchanged, update other details
#                 updated_line = f"{account_number}, {full_name_var.get()}, {dob_var.get()}, {phone_var.get()}, {account_type_var.get()}, {data[5]}\n"
#                 updated_lines.append(updated_line)
#                 found = True
#             else:
#                 updated_lines.append(line)
        
#         if not found:
#             messagebox.showerror("Error", "Account number not found!")
#             return
        
#         with open(ACCOUNT_FILE, "w") as file:
#             file.writelines(updated_lines)

#         messagebox.showinfo("Success", "Customer details updated successfully!")
    
#     except FileNotFoundError:
#         messagebox.showerror("Error", "Account file not found!")

# def clear_fields():
#     """Clears all input fields except Account Number."""
#     full_name_var.set("")
#     dob_var.set("")
#     phone_var.set("")
#     account_type_var.set("")

# # GUI Setup
# root = tk.Tk()
# root.title("Update Customer Information")
# root.geometry("600x400")
# root.configure(bg="#0A3D62")  # Dark navy blue background

# # Labels and Entry Fields
# tk.Label(root, text="Enter Account Number:", bg="#0A3D62", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
# account_var = tk.StringVar()
# tk.Entry(root, textvariable=account_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

# tk.Button(root, text="Fetch Details", command=fetch_details, font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10)

# # Variables for storing input
# full_name_var = tk.StringVar()
# dob_var = tk.StringVar()
# phone_var = tk.StringVar()
# account_type_var = tk.StringVar()

# # Labels and Entry Fields for Customer Details (without Amount)
# labels = ["Full Name:", "Date of Birth:", "Phone Number:", "Account Type:"]
# variables = [full_name_var, dob_var, phone_var, account_type_var]

# for i, label in enumerate(labels):
#     tk.Label(root, text=label, bg="#0A3D62", fg="white", font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)
#     tk.Entry(root, textvariable=variables[i], font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)

# # Buttons
# tk.Button(root, text="Update", command=update_account, font=("Arial", 12), bg="green", fg="white").grid(row=8, column=0, padx=10, pady=10)
# tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), bg="gray", fg="white").grid(row=8, column=1, padx=10, pady=10)
# tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12), bg="red", fg="white").grid(row=8, column=2, padx=10, pady=10)

# # Run the GUI
# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="W7301@jqir#",
    database="BankerDB"
)
cursor = db.cursor()

def fetch_details():
    """Fetches customer details from MySQL based on account number."""
    account_number = account_var.get().strip()

    if not account_number:
        messagebox.showerror("Error", "Please enter an account number!")
        return

    # Query to get account details
    cursor.execute("SELECT name, dob, phone, account_type FROM accounts WHERE account_number = %s", (account_number,))
    result = cursor.fetchone()

    if result:
        full_name_var.set(result[0])   # Full Name
        dob_var.set(result[1])         # Date of Birth
        phone_var.set(result[2])       # Phone Number
        account_type_var.set(result[3]) # Account Type
    else:
        messagebox.showerror("Error", "Account number not found!")

def update_account():
    """Updates customer details in MySQL (except balance)."""
    account_number = account_var.get().strip()

    if not account_number:
        messagebox.showerror("Error", "Please enter an account number!")
        return

    updated_name = full_name_var.get().strip()
    updated_dob = dob_var.get().strip()
    updated_phone = phone_var.get().strip()
    updated_account_type = account_type_var.get().strip()

    if not (updated_name and updated_dob and updated_phone and updated_account_type):
        messagebox.showerror("Error", "All fields must be filled!")
        return

    # Update query
    cursor.execute("""
        UPDATE accounts SET name = %s, dob = %s, phone = %s, account_type = %s 
        WHERE account_number = %s
    """, (updated_name, updated_dob, updated_phone, updated_account_type, account_number))

    db.commit()
    messagebox.showinfo("Success", "Customer details updated successfully!")

def clear_fields():
    """Clears all input fields except Account Number."""
    full_name_var.set("")
    dob_var.set("")
    phone_var.set("")
    account_type_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Update Customer Information")
root.geometry("600x400")
root.configure(bg="#0A3D62")  # Dark navy blue background

# Labels and Entry Fields
tk.Label(root, text="Enter Account Number:", bg="#0A3D62", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
account_var = tk.StringVar()
tk.Entry(root, textvariable=account_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Fetch Details", command=fetch_details, font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10)

# Variables for storing input
full_name_var = tk.StringVar()
dob_var = tk.StringVar()
phone_var = tk.StringVar()
account_type_var = tk.StringVar()

# Labels and Entry Fields for Customer Details (without Balance)
labels = ["Full Name:", "Date of Birth:", "Phone Number:", "Account Type:"]
variables = [full_name_var, dob_var, phone_var, account_type_var]

for i, label in enumerate(labels):
    tk.Label(root, text=label, bg="#0A3D62", fg="white", font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=variables[i], font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Update", command=update_account, font=("Arial", 12), bg="green", fg="white").grid(row=8, column=0, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), bg="gray", fg="white").grid(row=8, column=1, padx=10, pady=10)
tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12), bg="red", fg="white").grid(row=8, column=2, padx=10, pady=10)

# Run the GUI
root.mainloop()

# Close MySQL Connection when GUI is closed
db.close()
