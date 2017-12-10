from random import shuffle
# Challenge 021
# The same teacher of previous challenge wants to solve the order of presentation of the students' work.
# Make a program that reads the name of four students and shows the order drawn.
print("Challenge 021")
print("The same teacher of previous challenge wants to solve the order of presentation of the students' work.")
print("Make a program that reads the name of four students and shows the order drawn.")
firstStudent = str(input("First student: "))
secondStudent = str(input("Second student: "))
thirdStudent = str(input("Third student: "))
fourthStudent = str(input("Fourth student: "))
students = [firstStudent, secondStudent, thirdStudent, fourthStudent]
shuffle(students)
print("The order of presentation will be: {}".format(students))
