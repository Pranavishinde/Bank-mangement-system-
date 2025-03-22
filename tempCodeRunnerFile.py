import mysql.connector
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