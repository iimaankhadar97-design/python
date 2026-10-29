import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ================= MySQL Connection =====================
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",     # <-- Change this
        password="your_password", # <-- Change this
        database="hospital_db"
    )

# ================= Function to Add Patient ==============
def add_patient():
    if not all([name_entry.get(), age_entry.get(), gender_var.get(), address_entry.get(), phone_entry.get()]):
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "INSERT INTO patients (name, age, gender, address, phone) VALUES (%s, %s, %s, %s, %s)"
        val = (
            name_entry.get(),
            int(age_entry.get()),
            gender_var.get(),
            address_entry.get(),
            phone_entry.get()
        )
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_entries()
        fetch_patients()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ================= Function to Fetch Patients ===========
def fetch_patients():
    for row in patient_table.get_children():
        patient_table.delete(row)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        patient_table.insert("", "end", values=row)

# ================= Function to Clear Fields =============
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# ===================== GUI ==============================
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("900x600")
root.config(bg="#f0f0f0")

# ========== Patient Form ==========
form_frame = tk.LabelFrame(root, text="Add New Patient", padx=20, pady=10, bg="#f0f0f0")
form_frame.pack(pady=20, padx=10, fill="x")

tk.Label(form_frame, text="Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Age:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(form_frame, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Gender:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
gender_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="#f0f0f0").grid(row=2, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="#f0f0f0").grid(row=2, column=1)

tk.Label(form_frame, text="Address:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(form_frame, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Phone:", bg="#f0f0f0").grid(row=4, column=0, sticky="w")
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(form_frame, text="Add Patient", command=add_patient, bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

# ========== Patient List Table ==========
table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

cols = ("ID", "Name", "Age", "Gender", "Address", "Phone")
patient_table = ttk.Treeview(table_frame, columns=cols, show="headings")
for col in cols:
    patient_table.heading(col, text=col)
    patient_table.column(col, anchor="center")

patient_table.pack(fill="both", expand=True)

# Load patient data at start
fetch_patients()

root.mainloop()
