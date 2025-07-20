import tkinter as tk
from tkinter import messagebox, ttk
import re  # For email validation

def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()
    gender = gender_var.get()

    # Check for empty fields
    if name == "" or email == "" or age == "" or gender == "Select":
        messagebox.showwarning("Incomplete", "Please fill all fields.")
        return

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}$", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address (e.g., abc@gmail.com).")
        return

    # Validate age (digits only)
    if not age.isdigit():
        messagebox.showerror("Invalid Age", "Age must be a number.")
        return

    # Success
    messagebox.showinfo("Success", f"Registered!\n\nName: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}")
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("Select")

# App window
root = tk.Tk()
root.title("User Registration")
root.geometry("400x400")
root.configure(bg="#fdfdfd")

# Main frame
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Registration Form", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#333").pack(pady=10)

# Name
tk.Label(frame, text="Name", bg="#ffffff", anchor="w").pack(fill="x")
entry_name = tk.Entry(frame, width=30, font=("Helvetica", 11))
entry_name.pack(pady=5)

# Email
tk.Label(frame, text="Email", bg="#ffffff", anchor="w").pack(fill="x")
entry_email = tk.Entry(frame, width=30, font=("Helvetica", 11))
entry_email.pack(pady=5)

# Age
tk.Label(frame, text="Age", bg="#ffffff", anchor="w").pack(fill="x")
entry_age = tk.Entry(frame, width=30, font=("Helvetica", 11))
entry_age.pack(pady=5)

# Gender Dropdown
tk.Label(frame, text="Gender", bg="#ffffff", anchor="w").pack(fill="x")
gender_var = tk.StringVar(value="Select")
gender_dropdown = ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female", "Other"], state="readonly")
gender_dropdown.pack(pady=5)

# Buttons
tk.Button(frame, text="Submit", command=submit_form, bg="#4CAF50", fg="white", font=("Helvetica", 11), width=12).pack(pady=(15, 5))
tk.Button(frame, text="Clear", command=clear_form, font=("Helvetica", 11), width=12).pack()

# Footer
tk.Label(root, text="© 2025 Python GUI", font=("Helvetica", 9), bg="#fdfdfd", fg="#888").pack(side="bottom", pady=5)

root.mainloop()