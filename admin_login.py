import tkinter as tk
from tkinter import messagebox

def open_main():
    root.destroy()
    import main 

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        root.destroy()
        import admin_dashboard  # Open Admin Dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Create window
root = tk.Tk()
root.title("Admin Login")
root.geometry("400x250")
root.configure(bg="#f8f9fa")

tk.Label(root, text="Admin Login", font=("Arial", 18, "bold"), bg="#f8f9fa").pack(pady=10)
tk.Label(root, text="Username:", bg="#f8f9fa").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", bg="#f8f9fa").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", bg="#0077b6", fg="white", command=login).pack(pady=10)
# Logout Button
tk.Button(root, text="Logout", command=open_main, bg="#FF5733", fg="white", font=("Arial", 14), width=20, height=2, bd=3).pack(pady=20)

root.mainloop()