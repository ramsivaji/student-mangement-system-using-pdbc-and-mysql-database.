# student-mangement-system-using-pdbc-and-mysql-database.
Student Management System (Tkinter + MySQL)  A desktop-based CRUD application built using Python, Tkinter, and MySQL. This project allows users to Insert, Update, Delete, and View student records through a simple graphical user interface.
Features

📝 Add new student records

✏️ Update existing student details

❌ Delete student records

📋 Display all students

🖥️ User-friendly GUI using Tkinter

🗄️ Persistent storage using MySQL

🛡️ Proper error handling with message boxes

🛠️ Technologies Used

Python 3

Tkinter (GUI)

MySQL

mysql-connector-python

🧱 Database Structure
Database Name
p8

Table: Studentes
CREATE TABLE Studentes (
    roll_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    p_number VARCHAR(10) UNIQUE,
    gender VARCHAR(10),
    fees DECIMAL(10,2)
);

📂 Project Structure
Student-Management-System/
│
├── main.py        # Tkinter + MySQL CRUD application
├── README.md      # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
https://github.com/ramsivaji/student-mangement-system-using-pdbc-and-mysql-database./edit/main/

cd student-management-system

2️⃣ Install Required Package
pip install mysql-connector-python

3️⃣ Setup MySQL Database

Start MySQL server

Create database and table using the SQL provided above

Update database credentials in main.py if needed

4️⃣ Run the Application
python main.py

🖼️ Application UI Overview

Input Fields: Roll No, Name, Phone Number, Gender, Fees

Buttons:

Insert

Update

Delete

Display

Exit

Text Area: Displays all student records

🧠 How It Works

Tkinter handles the user interface

Python connects Tkinter actions to MySQL queries

CRUD operations are performed using parameterized SQL queries

MySQL stores and manages student data

🧪 Error Handling

Empty field validation

Duplicate phone number handling

Invalid roll number warnings

Database exceptions shown via message boxes

📌******** Future Enhancements ***************

📊 Treeview table instead of text area

🔽 Gender dropdown (Combobox)

🔐 Login authentication

🧹 Clear form after operations

📦 Convert application to .exe

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.


This project is for learning and educational purposes.

👤 Author

Rama Sivaji
Python Developer (Beginner)
📧 Contact: ramsivaji0@gmail.com

⭐ If you like this project

Please ⭐ star the repository — it motivates me to build more projects!
