# Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

name = input("Enter Name : ")
age = int(input("Enter Age : "))

turn_100 = 2123 - age

print("You will be turn 100 at :", turn_100)