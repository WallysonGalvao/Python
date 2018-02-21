"""Sorting an Item in the List"""

import random
# Challenge 019
# A teacher wants to draw one of his four students to erase the blackboard.
# Make a program that will help him by reading their name and writing the name of the chosen one.
print("Challenge 019")
print("A teacher wants to draw one of his four students to erase the blackboard.")
print("Make a program that will help him by reading their name and writing the name of the chosen one.")
firstStudent = input("First student: ")
secondStudent = input("Second student: ")
thirdStudent = input("Third student: ")
fourthStudent = input("Fourth student: ")
students = [firstStudent, secondStudent, thirdStudent, fourthStudent]
selectedStudent = random.choice(students)
print("The student chosen was {} ".format(selectedStudent))
