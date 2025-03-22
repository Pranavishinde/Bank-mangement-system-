
# import tkinter as tk
# from tkinter import messagebox
# import re
# import os

# FILE_PATH = "accounts.txt"

# def generate_unique_account_number():
#     """Generates a unique account number following the format: BankCode + BranchCode + Year + UniqueNumber."""
#     base_format = "21052025"  # Bank Code (21) + Branch Code (05) + Year (2025)

#     last_number = 0  # Default if no valid numbers are found

#     if os.path.exists(FILE_PATH):
#         with open(FILE_PATH, "r") as file:
#             lines = file.readlines()

#             # Process the file in reverse to find the last valid account number
#             for line in reversed(lines):
#                 line = line.strip().split(",")[0]  # Extract the first value (account number)
                
#                 if line.startswith(base_format) and len(line) == len(base_format) + 5:
#                     try:
#                         last_number = int(line[-5:])  # Extract last 5 digits as integer
#                         break  # Stop at the first valid account number
#                     except ValueError:
#                         continue  # Skip invalid lines and keep searching

#     new_unique_number = last_number + 1
#     formatted_unique_number = str(new_unique_number).zfill(5)
#     new_account_number = f"{base_format}{formatted_unique_number}"

#     return new_account_number

# def create_account():
#     """Handles account creation, validation, and saving to file."""
#     account_number = generate_unique_account_number()
    
#     # Get the values from input fields
#     name = name_entry.get().strip()
#     dob = dob_entry.get().strip()
#     phone = phone_entry.get().strip()
#     acc_type = acc_type_var.get()
#     deposit = deposit_entry.get().strip()

#     # Validation checks
#     if not name or not dob or not phone or not deposit:
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     # Validate phone number (10 digits)
#     if not re.match(r'^\d{10}$', phone):
#         messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
#         return

#     # Validate deposit (should be a positive number)
#     try:
#         deposit = float(deposit)
#         if deposit <= 0:
#             raise ValueError
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid deposit amount.")
#         return

#     # Save the account details to the file
#     with open(FILE_PATH, "a") as file:
#         file.write(f"{account_number}, {name}, {dob}, {phone}, {acc_type}, {deposit}\n")

#     messagebox.showinfo("Success", f"Account Created Successfully!\nAccount Number: {account_number}")
    
#     # Update the label with the generated account number
#     account_number_label.config(text=f"Account Number: {account_number}")

#     # Clear input fields
#     name_entry.delete(0, tk.END)
#     dob_entry.delete(0, tk.END)
#     phone_entry.delete(0, tk.END)
#     deposit_entry.delete(0, tk.END)

# # Tkinter GUI Setup
# root = tk.Tk()
# root.title("Banker - Create Account")
# root.geometry("450x500")
# root.configure(bg="#1E3D59")

# # Header
# header = tk.Label(root, text="Create Your Bank Account", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59")
# header.pack(pady=20)

# # Entry fields for user information
# fields = [("Full Name", "name_entry"), ("Date of Birth (DD/MM/YYYY)", "dob_entry"),
#           ("Phone Number", "phone_entry"), ("Initial Deposit (₹)", "deposit_entry")]

# for label, var_name in fields:
#     tk.Label(root, text=label, fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
#     globals()[var_name] = tk.Entry(root, width=40, font=("Arial", 12))
#     globals()[var_name].pack(pady=5)

# # Account Type Dropdown
# tk.Label(root, text="Account Type", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
# acc_type_var = tk.StringVar(value="Savings")
# acc_type_menu = tk.OptionMenu(root, acc_type_var, "Savings", "Current", "Fixed Deposit")
# acc_type_menu.pack(pady=5)

# # Account Number Label
# account_number_label = tk.Label(root, text="Account Number will be generated", fg="white", bg="#1E3D59", font=("Arial", 12))
# account_number_label.pack(pady=10)

# # Submit Button
# tk.Button(root, text="Create Account", command=create_account, bg="#28A745", fg="white",
#           font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

# root.mainloop()
# import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="W7301@jqir#",
    database="BankerDB"
)
cursor = db.cursor()

def generate_unique_account_number():
    """Generates a unique account number based on the last stored number."""
    base_format = "21052025"  # Bank Code (21) + Branch Code (05) + Year (2025)

    cursor.execute("SELECT account_number FROM accounts ORDER BY account_number DESC LIMIT 1")
    result = cursor.fetchone()

    if result:
        last_number = int(result[0][-5:])
    else:
        last_number = 0  # If no accounts exist yet

    new_unique_number = last_number + 1
    formatted_unique_number = str(new_unique_number).zfill(5)
    return f"{base_format}{formatted_unique_number}"

def create_account():
    """Handles account creation, validation, and saving to MySQL."""
    account_number = generate_unique_account_number()
    
    # Get user input
    name = name_entry.get().strip()
    dob = dob_entry.get().strip()
    phone = phone_entry.get().strip()
    acc_type = acc_type_var.get()
    deposit = deposit_entry.get().strip()

    # Validation checks
    if not name or not dob or not phone or not deposit:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate DOB (DD-MM-YYYY or DD/MM/YYYY)
    if not re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', dob):
        messagebox.showerror("Error", "Please enter Date of Birth in DD-MM-YYYY or DD/MM/YYYY format.")
        return

    # Validate phone number (10 digits)
    if not re.match(r'^\d{10}$', phone):
        messagebox.showerror("Error", "Please enter a valid 10-digit phone number.")
        return

    # Validate deposit (should be a positive number)
    try:
        deposit = float(deposit)
        if deposit <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid deposit amount.")
        return

    # Insert into MySQL database
    try:
        cursor.execute("INSERT INTO accounts (account_number, name, dob, phone, account_type, balance) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (account_number, name, dob, phone, acc_type, deposit))
        db.commit()
        messagebox.showinfo("Success", f"Account Created Successfully!\nAccount Number: {account_number}")

        # Update label with the generated account number
        account_number_label.config(text=f"Account Number: {account_number}")

        # Clear input fields
        name_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        deposit_entry.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Banker - Create Account")
root.geometry("450x500")
root.configure(bg="#1E3D59")

# Header
header = tk.Label(root, text="Create Your Bank Account", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59")
header.pack(pady=20)

# Entry fields for user information
fields = [("Full Name", "name_entry"), ("Date of Birth (DD-MM-YYYY)", "dob_entry"),
          ("Phone Number", "phone_entry"), ("Initial Deposit (₹)", "deposit_entry")]

for label, var_name in fields:
    tk.Label(root, text=label, fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
    globals()[var_name] = tk.Entry(root, width=40, font=("Arial", 12))
    globals()[var_name].pack(pady=5)

# Account Type Dropdown
tk.Label(root, text="Account Type", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
acc_type_var = tk.StringVar(value="Savings")
acc_type_menu = tk.OptionMenu(root, acc_type_var, "Savings", "Current", "Fixed Deposit")
acc_type_menu.pack(pady=5)

# Account Number Label
account_number_label = tk.Label(root, text="Account Number will be generated", fg="white", bg="#1E3D59", font=("Arial", 12))
account_number_label.pack(pady=10)

# Submit Button
tk.Button(root, text="Create Account", command=create_account, bg="#28A745", fg="white",
          font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

root.mainloop()

# Close DB Connection when GUI is closed
db.close()
