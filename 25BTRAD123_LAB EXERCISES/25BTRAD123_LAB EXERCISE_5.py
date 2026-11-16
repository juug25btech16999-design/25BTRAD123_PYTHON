
# LAB EXPERIMENT 5
# Python Programming Exercises


# LAB EXERCISE 14: Bank Account System Using OOP

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully!")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.__balance)


# Create bank account
account = BankAccount("Varsha", 5000)

while True:
    print("\n--- BANK ACCOUNT SYSTEM ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")


# LAB EXERCISE 15: Library Management System

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.book_id, self.title, self.author, status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nBook ID | Title | Author | Status")
            print("----------------------------------")

            for book in self.books:
                book.display()

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("This book was not issued!")
                return

        print("Book not found!")


# Main program
library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Try again.")


# LAB EXERCISE 16: Dice Simulator Using Random Module

import random

print("\n--- DICE SIMULATOR ---")

# Get number of dice and rolls
num_dice = int(input("Enter number of dice: "))
num_rolls = int(input("Enter number of rolls: "))

if num_dice <= 0 or num_rolls <= 0:
    print("Please enter positive numbers!")

else:
    frequency = {i: 0 for i in range(1, 7)}

    for roll in range(1, num_rolls + 1):
        results = []

        for dice in range(num_dice):
            number = random.randint(1, 6)
            results.append(number)
            frequency[number] += 1

        print("Roll", roll, ":", results)

    print("\n--- FREQUENCY SUMMARY ---")

    for number in range(1, 7):
        print(number, "appeared", frequency[number], "times")

    print("Total dice rolled:", num_dice * num_rolls)

print("Thank you for playing!")
