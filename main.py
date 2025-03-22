import tkinter as tk
from tkinter import messagebox

def open_admin():
    root.destroy()
    import admin_login  # Redirects to Admin Login Page

def open_employee():
    root.destroy()
    import employee_login  # Redirects to Employee Login Page

# GUI Setup
root = tk.Tk()
root.title("Banker - Bank Management System")
root.geometry("400x300")
root.configure(bg="#f8f9fa")

tk.Label(root, text="Welcome to Banker", font=("Arial", 18, "bold"), fg="#0077b6", bg="#f8f9fa").pack(pady=20)
tk.Label(root, text="Secure & Reliable Banking System", font=("Arial", 12), bg="#f8f9fa").pack()

tk.Button(root, text="Admin Login", bg="#0077b6", fg="white", width=20, command=open_admin).pack(pady=10)
tk.Button(root, text="Employee Login", bg="#0077b6", fg="white", width=20, command=open_employee).pack(pady=5)

root.mainloop()
