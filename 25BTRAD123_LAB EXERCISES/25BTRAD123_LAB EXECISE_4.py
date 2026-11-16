
# LAB EXPERIMENT 4
# Python Programming Exercises


# LAB EXERCISE 11: Log File Reader Program

from io import StringIO

# Sample log data
log_data = """INFO: Application started
ERROR: Database connection failed
WARNING: Low memory
INFO: User logged in
ERROR: File not found
INFO: Application running
WARNING: Disk space is low
"""

# Read log data
file = StringIO(log_data)
logs = file.readlines()

# Initialize counters
error = 0
warning = 0
info = 0

# Search and count keywords
for line in logs:
    if "ERROR" in line:
        error += 1
    elif "WARNING" in line:
        warning += 1
    elif "INFO" in line:
        info += 1

# Display summary
if len(logs) == 0:
    print("The log file is empty.")
else:
    print("Log File Summary")
    print("----------------")
    print("ERROR:", error)
    print("WARNING:", warning)
    print("INFO:", info)

file.close()


# LAB EXERCISE 12: Student Data Manager Using Files

FILE_NAME = "student_records.txt"


# Function to add student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid marks! Enter a number.")
        return

    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{sid},{name},{marks}\n")

        print("Student added successfully!")

    except OSError as e:
        print("File error:", e)


# Function to display students
def display_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("----------------")

            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("No student records found.")


# Function to search student
def search_student():
    sid = input("Enter Student ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for record in file:
                data = record.strip().split(",")

                if data[0] == sid:
                    print("\nStudent Found!")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Marks:", data[2])
                    return

        print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# Function to update student
def update_student():
    sid = input("Enter Student ID to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        found = False
        new_records = []

        for record in records:
            data = record.strip().split(",")

            if data[0] == sid:
                name = input("Enter New Name: ")

                try:
                    marks = float(input("Enter New Marks: "))

                    if marks < 0 or marks > 100:
                        print("Invalid marks. Update cancelled.")
                        return

                except ValueError:
                    print("Invalid marks. Update cancelled.")
                    return

                new_records.append(f"{sid},{name},{marks}\n")
                found = True

            else:
                new_records.append(record)

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(new_records)

            print("Student updated successfully!")

        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# Main menu
while True:
    print("\n--- Student Data Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")


# LAB EXERCISE 13: CSV-Based Payroll Management System

import csv
from io import StringIO

# Sample CSV employee data
data = """ID,Name,Basic,Allowance
101,Rahul,20000,5000
102,Varsha,25000,6000
103,Amit,30000,7000
"""

# Read CSV data
file = StringIO(data)
reader = csv.DictReader(file)

print("\nPAYROLL MANAGEMENT SYSTEM")
print("-------------------------")

total_salary = 0

for employee in reader:
    emp_id = employee["ID"]
    name = employee["Name"]
    basic = float(employee["Basic"])
    allowance = float(employee["Allowance"])

    # Calculate gross salary
    gross = basic + allowance

    # Calculate deductions
    pf = basic * 0.12
    tax = gross * 0.05

    deductions = pf + tax

    # Calculate net salary
    net = gross - deductions

    total_salary += net

    print("\nEmployee ID:", emp_id)
    print("Employee Name:", name)
    print("Basic Salary:", basic)
    print("Allowance:", allowance)
    print("Gross Salary:", gross)
    print("PF Deduction:", pf)
    print("Tax Deduction:", tax)
    print("Total Deduction:", deductions)
    print("Net Salary:", net)

print("\n-------------------------")
print("Total Salary Paid:", total_salary)

file.close()
