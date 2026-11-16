
# LAB EXPERIMENT 2
# Python Programming Exercises


# LAB EXERCISE 5: Number Guessing Game

import random

num = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == num:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry! Wrong guess.")
    print("The correct number was:", num)


# LAB EXERCISE 6 (A): Prime Number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")


# LAB EXERCISE 6 (B): Factorial

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# LAB EXERCISE 7: Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")
