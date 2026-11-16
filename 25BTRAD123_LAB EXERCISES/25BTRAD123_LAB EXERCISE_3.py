
# LAB EXPERIMENT 3
# Python Programming Exercises


# LAB EXERCISE 8: Contact Book Using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact Found:")
            print(contact)
            return

    print("Contact not found!")


def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated successfully!")
            return

    print("Contact not found!")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found!")


def display_contacts():
    if not contacts:
        print("No contacts available!")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(contact)


while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice! Try again.")


# LAB EXERCISE 9: Student Grading System

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks: "))

    students[name] = marks

print("\n--- STUDENT RESULTS ---")

for name, marks in students.items():

    if marks < 0 or marks > 100:
        grade = "Invalid Marks"
    elif marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "Fail"

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("------------------")


# LAB EXERCISE 10: Frequency Counter Using Dictionaries

students = {}

subjects = input("Enter student subject preferences: ")

responses = subjects.lower().split()

for subject in responses:
    if subject in students:
        students[subject] += 1
    else:
        students[subject] = 1

print("\n--- SUBJECT FREQUENCY ---")

for subject, count in students.items():
    print(subject, ":", count)
