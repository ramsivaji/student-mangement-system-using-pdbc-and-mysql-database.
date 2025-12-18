import mysql.connector
import tkinter as tk
from tkinter import messagebox

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="p8"
)

if conn.is_connected():
    print("Connected to MySQL successfully\n")

cursor = conn.cursor()

# ---------------- FUNCTIONS ------------------------------- ----------------

def insert():
    try:
        name1 = e_name.get()
        p_no = e_phone.get()
        gen = e_gender.get()
        fees1 = e_fees.get()

        if name1 == "" or p_no == "" or gen == "" or fees1 == "":
            messagebox.showerror("Error", "All fields are required")
            return

        sql = "INSERT INTO Studentes (name, p_number, gender, fees) VALUES (%s, %s, %s, %s)"
        values = (name1, p_no, gen, fees1)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo("Success", "Data inserted successfully")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def update():
    try:
        rno = e_roll.get()
        name1 = e_name.get()
        p_no = e_phone.get()
        gen = e_gender.get()
        fees1 = e_fees.get()

        if rno == "":
            messagebox.showerror("Error", "Roll number is required")
            return

        sql = """
            UPDATE Studentes
            SET name=%s,
                p_number=%s,
                gender=%s,
                fees=%s
            WHERE roll_no=%s
        """

        values = (name1, p_no, gen, fees1, rno)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "No record found")
        else:
            messagebox.showinfo("Success", "Data updated successfully")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def delete():
    try:
        rno = e_roll.get()

        if rno == "":
            messagebox.showerror("Error", "Roll number is required")
            return

        sql = "DELETE FROM Studentes WHERE roll_no=%s"
        values = (rno,)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "No record found")
        else:
            messagebox.showinfo("Success", "Data deleted successfully")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def dis():
    try:
        cursor.execute("SELECT * FROM Studentes")
        rows = cursor.fetchall()

        text.delete(1.0, tk.END)
        for row in rows:
            text.insert(tk.END, f"{row}\n")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def display():
    pass   # kept only because you had this function


# ---------------- TKINTER UI ----------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Student Management System")
root.geometry("460x540")

tk.Label(root, text="Student Management System",
         font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Roll No").grid(row=0, column=0, sticky="w")
e_roll = tk.Entry(frame)
e_roll.grid(row=0, column=1)

tk.Label(frame, text="Name").grid(row=1, column=0, sticky="w")
e_name = tk.Entry(frame)
e_name.grid(row=1, column=1)

tk.Label(frame, text="Phone Number").grid(row=2, column=0, sticky="w")
e_phone = tk.Entry(frame)
e_phone.grid(row=2, column=1)

tk.Label(frame, text="Gender").grid(row=3, column=0, sticky="w")
e_gender = tk.Entry(frame)
e_gender.grid(row=3, column=1)

tk.Label(frame, text="Fees").grid(row=4, column=0, sticky="w")
e_fees = tk.Entry(frame)
e_fees.grid(row=4, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Insert", width=10, command=insert).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Display", width=10, command=dis).grid(row=0, column=3, padx=5)

text = tk.Text(root, height=20, width=100)
text.pack(pady=10)

def exit_app():
    cursor.close()
    conn.close()
    root.destroy()

tk.Button(root, text="Exit", width=10, command=exit_app).pack(pady=5)

root.mainloop()
