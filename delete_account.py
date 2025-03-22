# import tkinter as tk
# from tkinter import messagebox

# # Function to delete an account based on the account number
# def delete_account():
#     account_number = account_number_entry.get()

#     # Check if the account number is provided
#     if not account_number:
#         messagebox.showerror("Error", "Please enter an account number.")
#         return

#     # Read all accounts from the file
#     with open("accounts.txt", "r") as file:
#         accounts = file.readlines()

#     # Remove the account with the entered account number
#     with open("accounts.txt", "w") as file:
#         account_found = False
#         for account in accounts:
#             if account.split(",")[0] != account_number:
#                 file.write(account)
#             else:
#                 account_found = True
        
#         if account_found:
#             messagebox.showinfo("Success", f"Account {account_number} deleted successfully.")
#         else:
#             messagebox.showerror("Error", "Account not found!")

# # GUI setup for Delete Account
# root = tk.Tk()
# root.title("Banker - Delete Account")
# root.geometry("450x300")
# root.configure(bg="#1E3D59")

# # Header
# header = tk.Label(root, text="Delete Bank Account", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59")
# header.pack(pady=20)

# # Account Number Input
# tk.Label(root, text="Enter Account Number to Delete", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
# account_number_entry = tk.Entry(root, width=40, font=("Arial", 12))
# account_number_entry.pack(pady=5)

# # Delete Account Button
# tk.Button(root, text="Delete Account", command=delete_account, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

# # Logout Button
# tk.Button(root, text="Logout", command=root.quit, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

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

def delete_account():
    """Deletes an account from MySQL based on account number."""
    account_number = account_number_entry.get().strip()

    if not account_number:
        messagebox.showerror("Error", "Please enter an account number.")
        return

    # Check if account exists
    cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
    result = cursor.fetchone()

    if not result:
        messagebox.showerror("Error", "Account not found!")
        return

    # Confirm before deleting
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete account {account_number}?")
    if not confirm:
        return

    # Delete account
    cursor.execute("DELETE FROM accounts WHERE account_number = %s", (account_number,))
    db.commit()

    messagebox.showinfo("Success", f"Account {account_number} deleted successfully.")

# GUI setup for Delete Account
root = tk.Tk()
root.title("Banker - Delete Account")
root.geometry("450x300")
root.configure(bg="#1E3D59")

# Header
header = tk.Label(root, text="Delete Bank Account", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59")
header.pack(pady=20)

# Account Number Input
tk.Label(root, text="Enter Account Number to Delete", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
account_number_entry = tk.Entry(root, width=40, font=("Arial", 12))
account_number_entry.pack(pady=5)

# Delete Account Button
tk.Button(root, text="Delete Account", command=delete_account, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

# Logout Button
tk.Button(root, text="Logout", command=root.quit, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

root.mainloop()

# Close MySQL Connection when GUI is closed
db.close()
