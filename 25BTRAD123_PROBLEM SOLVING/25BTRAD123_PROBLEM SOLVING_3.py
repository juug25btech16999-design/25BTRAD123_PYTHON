//Attendance Tracker

students = {}
total_classes = 0
def add_student():
name = input("Enter student name: ")
if name in students:
print("Student already exists!")
else:
students[name] = 0
print("Student added successfully!")
def mark_attendance():
global total_classes
total_classes += 1
print("\nMark Attendance (P = Present, A = Absent)")
for name in students:
status = input(name + ": ").upper()
while status not in ["P", "A"]:
print("Enter only P or A")
status = input(name + ": ").upper()
if status == "P":
students[name] += 1
print("Attendance updated successfully!")
def display_attendance():
print("\n----- ATTENDANCE DETAILS -----")
if not students:
print("No students available.")
return
for name, present in students.items():

if total_classes > 0:
percentage = (present / total_classes) * 100
else:
percentage = 0
print(name, "- Present:", present,
"Total Classes:", total_classes,
"Attendance:", round(percentage, 2), "%")
def check_low_attendance():
print("\nStudents Below 75% Attendance:")
found = False
for name, present in students.items():
if total_classes > 0:
percentage = (present / total_classes) * 100
else:
percentage = 0
if percentage < 75:
print(name, "-", round(percentage, 2), "%")
found = True
if not found:
print("No students below 75% attendance.")
while True:
print("\n===== ATTENDANCE TRACKER =====")
print("1. Add Student")
print("2. Mark Attendance")
print("3. Display Attendance")
print("4. Check Low Attendance")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
add_student()
elif choice == "2":
if students:
mark_attendance()
else:
print("Add students first!")
elif choice == "3":
display_attendance()
elif choice == "4":
check_low_attendance()

elif choice == "5":
print("Thank you for using Attendance Tracker!")
break
else:
print("Invalid choice! Try again.”)
