# import tkinter as tk
# from tkinter import messagebox

# def add_employee():
#     name = entry_name.get()
#     role = role_var.get()
#     username = entry_username.get()
#     password = entry_password.get()

#     if name and role and username and password:
#         with open("employees.txt", "a") as file:
#             file.write(f"{username},{password},{role}\n")
#         messagebox.showinfo("Success", "Employee Added Successfully!")
#         entry_name.delete(0, tk.END)
#         entry_username.delete(0, tk.END)
#         entry_password.delete(0, tk.END)
#     else:
#         messagebox.showerror("Error", "All Fields Are Required!")

# # Create window
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
# role_dropdown = tk.OptionMenu(root, role_var, "Account Manager", "Cashier", "Update Customer","Account Delete")
# role_dropdown.pack(pady=5)

# tk.Label(root, text="Username:", bg="#f8f9fa").pack()
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# tk.Label(root, text="Password:", bg="#f8f9fa").pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# tk.Button(root, text="Add Employee", bg="#0077b6", fg="white", command=add_employee).pack(pady=10)

# root.mainloop() 
# import mysql.connector
# import tkinter as tk
# from tkinter import messagebox
# from db_connection import connect_db

# def add_employee():
#     name = entry_name.get()
#     role = role_var.get()
#     username = entry_username.get()
#     password = entry_password.get()

#     if name and role and username and password:
#         conn = connect_db()
#         if conn:
#             cursor = conn.cursor()
#             try:
#                 query = "INSERT INTO employees (username, password, role) VALUES (%s, %s, %s)"
#                 cursor.execute(query, (username, password, role))
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
# role_dropdown = tk.OptionMenu(root, role_var, "Admin", "Account Manager", "Cashier", "Update Customer", "Account Delete")
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

# Function to add an employee
def add_employee():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    role = role_var.get()

    if not username or not password or role == "Select Role":
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()

        # 🔹 Check if username already exists
        cursor.execute("SELECT * FROM employees WHERE username=%s", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists!")
            conn.close()
            return

        # 🔹 Insert employee into MySQL (password stored as plain text)
        cursor.execute("INSERT INTO employees (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
        conn.commit()
        messagebox.showinfo("Success", f"Employee {username} added successfully!")
        
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        role_var.set("Select Role")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        conn.close()

# GUI Setup
admin_root = tk.Tk()
admin_root.title("Admin - Add Employee")
admin_root.geometry("400x400")
admin_root.configure(bg="#f0f0f0")

tk.Label(admin_root, text="Add Employee", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(admin_root, text="Username:", bg="#f0f0f0").pack()
entry_username = tk.Entry(admin_root)
entry_username.pack(pady=5)

tk.Label(admin_root, text="Password:", bg="#f0f0f0").pack()
entry_password = tk.Entry(admin_root)
entry_password.pack(pady=5)

tk.Label(admin_root, text="Role:", bg="#f0f0f0").pack()
role_var = tk.StringVar(value="Select Role")
role_menu = tk.OptionMenu(admin_root, role_var, "Account Manager", "Cashier", "Update Customer", "Loan Officer")
role_menu.pack(pady=5)

tk.Button(admin_root, text="Add Employee", bg="#28A745", fg="white", font=("Arial", 14), command=add_employee).pack(pady=20)

admin_root.mainloop()