# import tkinter as tk
# from tkinter import messagebox

# def open_main():
#     root.destroy()
#     import main 

# def login():
#     username = entry_username.get()
#     password = entry_password.get()

#     try:
#         with open("employees.txt", "r") as file:
#             for line in file:
#                 parts = line.strip().split(",")
#                 if len(parts) == 3:  # Ensure all values exist
#                     user, passw, role = parts
#                     if user == username and passw == password:
#                         root.destroy()
#                         if role == "Account Manager":
#                             import account_manager_dashboard
#                         elif role == "Cashier":
#                             import cashier_dashboard
#                         elif role == "Update Customer":
#                             import update_customer
#                         elif role == "loan officer":
#                             import loan_officer_dashboard   
#                         else:
#                             messagebox.showerror("Error", "Invalid role assigned!")
#                         return
#             messagebox.showerror("Login Failed", "Invalid username or password!")
#     except FileNotFoundError:
#         messagebox.showerror("Error", "employees.txt not found!")

# # GUI Setup
# root = tk.Tk()
# root.title("Employee Login")
# root.geometry("500x500")
# root.configure(bg="#f8f9fa")

# tk.Label(root, text="Employee Login", font=("Arial", 16, "bold"), bg="#f8f9fa").pack(pady=10)
# tk.Label(root, text="Username:", bg="#f8f9fa").pack()
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# tk.Label(root, text="Password:", bg="#f8f9fa").pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# tk.Button(root, text="Login", bg="#0077b6", fg="white",font=("Arial", 14), width=20, height=2, bd=3, command=login).pack(pady=10)
# # Logout Button
# tk.Button(root, text="Logout", command=open_main, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

# root.mainloop()
# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import hashlib

# # Function to hash the entered password
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def open_main():
#     root.destroy()
#     import main 

# def login():
#     username = entry_username.get()
#     password = entry_password.get()
#     hashed_password = hash_password(password)  # Convert entered password to hash

#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(host="localhost", user="root", password="", database="bank_db")
#         cursor = conn.cursor()

#         # Check if username and hashed password match
#         query = "SELECT role FROM employees WHERE username = %s AND password = %s"
#         cursor.execute(query, (username, hashed_password))
#         result = cursor.fetchone()

#         cursor.close()
#         conn.close()

#         if result:
#             role = result[0]  # Get role from query result
#             root.destroy()
            
#             # Redirect to appropriate dashboard
#             if role == "Account Manager":
#                 import account_manager_dashboard
#             elif role == "Cashier":
#                 import cashier_dashboard
#             elif role == "Update Customer":
#                 import update_customer
#             elif role == "Loan Officer":
#                 import loan_officer_dashboard
#             else:
#                 messagebox.showerror("Error", "Invalid role assigned!")
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password!")

#     except mysql.connector.Error as e:
#         messagebox.showerror("Database Error", str(e))

# # GUI Setup
# root = tk.Tk()
# root.title("Employee Login")
# root.geometry("500x500")
# root.configure(bg="#f8f9fa")

# tk.Label(root, text="Employee Login", font=("Arial", 16, "bold"), bg="#f8f9fa").pack(pady=10)
# tk.Label(root, text="Username:", bg="#f8f9fa").pack()
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# tk.Label(root, text="Password:", bg="#f8f9fa").pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# tk.Button(root, text="Login", bg="#0077b6", fg="white", font=("Arial", 14), width=20, height=2, bd=3, command=login).pack(pady=10)
# tk.Button(root, text="Logout", command=open_main, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

# root.mainloop()

# import mysql.connector
# import tkinter as tk
# from tkinter import messagebox
# from db_connection import connect_db
# import hashlib

# def hash_password(password):
#     """Hashes the password using SHA-256 for security."""
#     return hashlib.sha256(password.encode()).hexdigest()

# def add_employee():
#     name = entry_name.get()
#     role = role_var.get()
#     username = entry_username.get()
#     password = entry_password.get()

#     if name and role and username and password:
#         hashed_password = hash_password(password)  # Hash the password before storing

#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             try:
#                 query = "INSERT INTO employees (username, password, role) VALUES (%s, %s, %s)"
#                 cursor.execute(query, (username, hashed_password, role))
#                 conn.commit()
#                 messagebox.showinfo("Success", "✅ Employee Added Successfully!")
                
#                 # Clear fields
#                 entry_name.delete(0, tk.END)
#                 entry_username.delete(0, tk.END)
#                 entry_password.delete(0, tk.END)

#             except mysql.connector.Error as e:
#                 messagebox.showerror("Error", f"❌ MySQL Error: {e}")
            
#             cursor.close()
#             conn.close()
#         else:
#             messagebox.showerror("Error", "❌ Database Connection Failed!")
#     else:
#         messagebox.showerror("Error", "❌ All Fields Are Required!")

# # ✅ GUI for Admin Dashboard
# root = tk.Tk()
# root.title("Admin Dashboard")
# root.geometry("400x400")
# root.configure(bg="#f8f9fa")

# tk.Label(root, text="Add Employee", font=("Arial", 18, "bold"), bg="#f8f9fa").pack(pady=10)
# tk.Label(root, text="Name:", bg="#f8f9fa").pack()
# entry_name = tk.Entry(root)
# entry_name.pack(pady=5)

# tk.Label(root, text="Role:", bg="#f8f9fa").pack()
# role_var = tk.StringVar()
# role_dropdown = tk.OptionMenu(root, role_var, "Admin", "Account Manager", "Cashier", "Update Customer", "Loan Officer")
# role_dropdown.pack(pady=5)

# tk.Label(root, text="Username:", bg="#f8f9fa").pack()
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# tk.Label(root, text="Password:", bg="#f8f9fa").pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# tk.Button(root, text="Add Employee", bg="#0077b6", fg="white", command=add_employee).pack(pady=10)

# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="W7301@jqir#",  # Replace with your actual MySQL password
            database="BankerDB"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to handle login
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM employees WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
        
        if result:
            role = result[0]
            messagebox.showinfo("Success", f"Welcome {username}!")

            root.destroy()
            if role == "Account Manager":
                import account_manager_dashboard
            elif role == "Cashier":
                import cashier_dashboard
            elif role == "Update Customer":
                import update_customer
            elif role == "Loan Officer":
                import loan_officer_dashboard
            else:
                messagebox.showerror("Error", "Invalid role assigned!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        conn.close()

# GUI Setup
root = tk.Tk()
root.title("Employee Login")
root.geometry("400x300")
root.configure(bg="#f8f9fa")

tk.Label(root, text="Employee Login", font=("Arial", 16, "bold"), bg="#f8f9fa").pack(pady=10)

tk.Label(root, text="Username:", bg="#f8f9fa").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", bg="#f8f9fa").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", bg="#0077b6", fg="white", font=("Arial", 14), command=login).pack(pady=10)

root.mainloop()