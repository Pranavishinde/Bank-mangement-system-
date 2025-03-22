# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# # Function to retrieve the balance from the accounts file
# def get_balance(account_number):
#     try:
#         with open('accounts.txt', 'r') as file:
#             for line in file:
#                 values = line.strip().split(",")  # Split each line by commas
#                 if len(values) == 5:  # Ensure there are exactly 5 values
#                     acc_no, name, phone, acc_type, balance = values  # Unpack the values
#                     if acc_no == account_number:  # Check if account number matches
#                         return float(balance)  # Return balance as float
#         return None  # If account not found
#     except Exception as e:
#         print(f"Error reading file: {e}")
#         return None

# # Function for Deposit
# def deposit():
#     account_number = entry_account_number.get()  # Get account number from input
#     amount = float(entry_amount.get())  # Get deposit amount from input
#     balance = get_balance(account_number)  # Get current balance
#     if balance is not None:
#         new_balance = balance + amount  # Calculate new balance
#         messagebox.showinfo("Success", f"Deposited {amount}. New balance: {new_balance}")
#     else:
#         messagebox.showerror("Error", "Account not found.")

# # Function for Withdraw
# def withdraw():
#     account_number = entry_account_number.get()  # Get account number from input
#     amount = float(entry_amount.get())  # Get withdrawal amount from input
#     balance = get_balance(account_number)  # Get current balance
#     if balance is not None:
#         if balance >= amount:  # Check if balance is sufficient
#             new_balance = balance - amount  # Calculate new balance
#             messagebox.showinfo("Success", f"Withdrawn {amount}. New balance: {new_balance}")
#         else:
#             messagebox.showerror("Error", "Insufficient balance.")
#     else:
#         messagebox.showerror("Error", "Account not found.")

# # Create the main window
# root = tk.Tk()
# root.title("Cashier Dashboard")
# root.geometry("500x400")  # Set window size
# root.config(bg="#f0f0f0")  # Set background color

# # Add a header label
# header_label = tk.Label(root, text="Cashier Dashboard", font=("Arial", 24, "bold"), bg="#3b5998", fg="white")
# header_label.pack(fill="x", pady=10)

# # Account number input
# label_account_number = tk.Label(root, text="Account Number:", font=("Arial", 12), bg="#f0f0f0")
# label_account_number.pack(pady=(10, 5))
# entry_account_number = ttk.Entry(root, font=("Arial", 12))
# entry_account_number.pack(pady=5)

# # Amount input
# label_amount = tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f0f0f0")
# label_amount.pack(pady=(10, 5))
# entry_amount = ttk.Entry(root, font=("Arial", 12))
# entry_amount.pack(pady=5)

# # Deposit button with custom style
# deposit_button = ttk.Button(root, text="Deposit", command=deposit, style="TButton")
# deposit_button.pack(pady=10, fill="x")

# # Withdraw button with custom style
# withdraw_button = ttk.Button(root, text="Withdraw", command=withdraw, style="TButton")
# withdraw_button.pack(pady=10, fill="x")

# # Styling for buttons
# style = ttk.Style()
# style.configure("TButton",
#                 font=("Arial", 12),
#                 padding=10,
#                 relief="flat",
#                 background="#4CAF50",
#                 foreground="white")
# style.map("TButton",
#           background=[('active', '#45a049')],
#           foreground=[('active', 'white')])

# # Run the application
# root.mainloop()
# 
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="W7301@jqir#",
    database="BankerDB"
)
cursor = db.cursor()

def get_balance(account_number):
    """Fetch the balance of an account from MySQL."""
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    result = cursor.fetchone()
    return float(result[0]) if result else None

def update_balance(account_number, new_balance):
    """Update the account balance in MySQL."""
    cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (new_balance, account_number))
    db.commit()

def deposit_money():
    """Handles depositing money into an account."""
    account_number = account_entry.get().strip()
    amount = amount_entry.get().strip()

    if not account_number or not amount:
        messagebox.showerror("Error", "Account number and amount are required!")
        return

    # Validate amount
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid deposit amount.")
        return

    # Check if account exists
    balance = get_balance(account_number)
    if balance is None:
        messagebox.showerror("Error", "Account not found!")
        return

    # Update balance
    new_balance = balance + amount
    update_balance(account_number, new_balance)

    messagebox.showinfo("Success", f"₹{amount} Deposited Successfully!\nNew Balance: ₹{new_balance}")

    # Clear input fields
    amount_entry.delete(0, tk.END)

def withdraw_money():
    """Handles withdrawing money from an account."""
    account_number = account_entry.get().strip()
    amount = amount_entry.get().strip()

    if not account_number or not amount:
        messagebox.showerror("Error", "Account number and amount are required!")
        return

    # Validate amount
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid withdrawal amount.")
        return

    # Check if account exists
    balance = get_balance(account_number)
    if balance is None:
        messagebox.showerror("Error", "Account not found!")
        return

    # Check if sufficient balance is available
    if amount > balance:
        messagebox.showerror("Error", "Insufficient balance!")
        return

    # Update balance
    new_balance = balance - amount
    update_balance(account_number, new_balance)

    messagebox.showinfo("Success", f"₹{amount} Withdrawn Successfully!\nNew Balance: ₹{new_balance}")

    # Clear input fields
    amount_entry.delete(0, tk.END)

def check_balance():
    """Displays the balance of the entered account."""
    account_number = account_entry.get().strip()

    if not account_number:
        messagebox.showerror("Error", "Please enter an account number!")
        return

    # Fetch balance
    balance = get_balance(account_number)
    if balance is None:
        messagebox.showerror("Error", "Account not found!")
        return

    messagebox.showinfo("Balance Info", f"Current Balance: ₹{balance}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Banker - Cashier Dashboard")
root.geometry("450x400")
root.configure(bg="#1E3D59")

# Header
header = tk.Label(root, text="Cashier Dashboard", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59")
header.pack(pady=20)

# Account Number Entry
tk.Label(root, text="Account Number", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
account_entry = tk.Entry(root, width=40, font=("Arial", 12))
account_entry.pack(pady=5)

# Amount Entry
tk.Label(root, text="Amount (₹)", fg="white", bg="#1E3D59", font=("Arial", 12)).pack()
amount_entry = tk.Entry(root, width=40, font=("Arial", 12))
amount_entry.pack(pady=5)

# Buttons for Deposit, Withdraw, and Check Balance
tk.Button(root, text="Deposit Money", command=deposit_money, bg="#28A745", fg="white", 
          font=("Arial", 14), width=20, height=2, bd=3).pack(pady=10)

tk.Button(root, text="Withdraw Money", command=withdraw_money, bg="#DC3545", fg="white", 
          font=("Arial", 14), width=20, height=2, bd=3).pack(pady=10)

tk.Button(root, text="Check Balance", command=check_balance, bg="#007BFF", fg="white", 
          font=("Arial", 14), width=20, height=2, bd=3).pack(pady=10)

root.mainloop()

# Close DB Connection when GUI is closed
db.close()
