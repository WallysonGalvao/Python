# Challenge 001
# Create a program that write "Hello, World!" on the screen.
print("Challenge 001")
print("Create a program that write \"Hello, World!\" in screen.")
print("Hello, World")

# Challenge 002
# Make a program that reads the name a person and show a welcome message.
print("Challenge 002")
print("Make a program that read the name a person and show a welcome message.")
userName = input("Write your name: ")
print("It's a pleasure meet you, {}!".format(userName))

# Challenge 003
# Create a program that reads two numbers and shows the sum between them.
print("Challenge 003")
print("Create a program that reads two numbers and shows the sum between them.")
number1 = int(input("Write a first number: "))
number2 = int(input("Write a second number: "))
resultOfSum = number1 + number2
print("The sum between {} and {} is equals of {}".format(number1, number2, resultOfSum))

# Challenge 004
# Make a program that reads something from the keyboard and shows on the screen its primitive type and
# all possible information about it.
print("Challenge 004")
print("Make a program that reads something from the keyboard and shows on the screen its primitive type and")
print("all possible information about it.")
userInput = input("Write something: ")
print("The primitive type of this value is ", type(userInput))
print("Only have spaces ?", userInput.isspace())
print("It's a number? ", userInput.isnumeric())
print("It's alphabetic ?", userInput.isalpha())
print("It's alphanumeric ?", userInput.isalnum())
print("It's in uppercase ?", userInput.isupper())
print("It's in lowercase ?", userInput.islower())
print("Is capitalized ?", userInput.istitle())

# Challenge 005
# Make a program that read an integer and shows on the screen its successor and its predecessor.
print("Challenge 005")
print("Make a program that read an integer and shows on the screen its successor and its predecessor.")
userValue = int(input("Write a number: "))
successor = userValue + 1
predecessor = userValue - 1
print("Analysing the value {}, it's predecessor is {} and it's successor is {}"
      .format(userValue, predecessor, successor))

# Challenge 006
# Create an algorithm that read a number and shows its double, triple, and square root.
print("Challenge 006")
print("Create an algorithm that read a number and shows its double, triple, and square root.")
userValue = int(input("Write an number: "))
double = userValue * 2
triple = userValue * 3
# squareRoot = userValue ** (1/2)
squareRoot = pow(userValue, (1 / 2))
print("The double of {} worth {}".format(userValue, double))
print("The triple of {} worth {}".format(userValue, triple))
print("The square root of {} is equals of {:.2f}".format(userValue, squareRoot))

# Challenge 007
# Develop a program that reads a student's two grades, computes and shows your average.
print("Challenge 007")
print("Develop a program that reads a student's two grades, computes and shows your average.")
firstGrade = float(input("First grade of student: "))
secondGrade = float(input("Second grade of student: "))
average = (firstGrade + secondGrade) / 2
print("The average between {:.1f} and {:.1f} is equals of {:.1f}".format(firstGrade, secondGrade, average))

# Challenge 008
# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
print("Challenge 008")
print("Write a program that reads a value in meters and displays it converted to centimeters and millimeters.")
distanceInMeters = float(input("A distance in meters: "))
centimeters = distanceInMeters * 100
millimeters = distanceInMeters * 1000
print("The average of {}m corresponds to {}cm and {}mm".format(distanceInMeters, centimeters, millimeters))

# Challenge 009
# Make a program that read any integer and shows on the screen its table.
print("Challenge 009")
print("Make a program that read any integer and shows on the screen its table.")
number = int(input("Type it a number to see its table: "))
multipliedByOne = number * 1
multipliedByTwo = number * 2
multipliedByThree = number * 3
multipliedByFour = number * 4
multipliedByFive = number * 5
multipliedBySix = number * 6
multipliedBySeven = number * 7
multipliedByEight = number * 8
multipliedByNine = number * 9
multipliedByTen = number * 10
print("=============")
print("{} x {:2} = {}".format(number, 1, multipliedByOne))
print("{} x {:2} = {}".format(number, 2, multipliedByTwo))
print("{} x {:2} = {}".format(number, 3, multipliedByThree))
print("{} x {:2} = {}".format(number, 4, multipliedByFour))
print("{} x {:2} = {}".format(number, 5, multipliedByFive))
print("{} x {:2} = {}".format(number, 6, multipliedBySix))
print("{} x {:2} = {}".format(number, 7, multipliedBySeven))
print("{} x {:2} = {}".format(number, 8, multipliedByEight))
print("{} x {:2} = {}".format(number, 9, multipliedByNine))
print("{} x {:2} = {}".format(number, 10, multipliedByTen))
print("=============")

# Challenge 010
# Create a program that read how much money a person has in the wallet and shows how much money they can buy.
print("Challenge 010")
print("Create a program that read how much money a person has in the wallet and shows how much money they can buy.")
money = float(input("How much money do you have in the wallet ? $"))
reais = money * 3.28
print("With ${:.2f} dollars you can buy R${:.2f} reais".format(money, reais))

# Challenge 011
# Make a program that read the width and height of a wall in meters, calculate its area and the amount of paint needed
# to paint it, know that each liter of paint, paints an area of 2sqm.
# sqm = m²
print("Challenge 011")
print("Make a program that read the width and height of a wall in meters, calculate its area and the amount of paint")
print("needed to paint it, know that each liter of paint, paints an area of 2sqm.")
wallWidth = float(input("Wall Width: "))
wallHeight = float(input("Wall Height: "))
squareMeters = wallHeight * wallWidth
literOfPaint = squareMeters / 2
print("Its wall has the dimension of {}x{} and its area is {}m²".format(wallWidth, wallHeight, squareMeters))
print("For paint this wall you'll need of {} liters of paint".format(literOfPaint))

# Challenge 012
# Make an algorithm that read the price of a product and shows its new price, with a 5% discount.
print("Challenge 012")
print("Make an algorithm that read the price of a product and shows its new price, with a 5% discount.")
priceOfProduct = float(input("What is the product's price ? $"))
discount = priceOfProduct * 5 / 100
newPrice = priceOfProduct - discount
print("The product that costs ${:.2f}, in promotion with discount of 5% will cost ${:.2f}"
      .format(priceOfProduct, newPrice))

# Challenge 013
# Make an algorithm that read the employee's salary and show its new salary, with 15% of increase.
print("Challenge 013")
print("Make an algorithm that read the employee's salary and show its new salary, with 15% of increase.")
salaryOfEmployee = float(input("What is the employee's salary ? $"))
newSalary = salaryOfEmployee + (salaryOfEmployee * 15 / 100)
print("An employee earning ${}, with a 15% raise, is getting ${}".format(salaryOfEmployee, newSalary))

# Challenge 014
# Write a program that convert a temperature typed in ºC and convert for ºF.
print("Challenge 014")
print("Write a program that convert a temperature typed in ºC and convert for ºF.")
temperatureCelsius = float(input("Enter the temperature in °C: "))
temperatureFahrenheit = ((9 * temperatureCelsius) / 5) + 32
print("The temperature of {}ºC corresponds {}ºF!".format(temperatureCelsius, temperatureFahrenheit))

# Challenge 015
# Write a program that asks the number of miles traveled by a rental car and the number of days it was rented
# Calculate the price to pay, knowing that the car costs $ 60 per day and $ 0.15 per kilometer wheeled.
print("Challenge 015")
print("Write a program that asks the number of miles traveled by a rental car and the number of days it was rented ")
print("Calculate the price to pay, knowing that the car costs $ 60 per day and $ 0.15 per kilometer wheeled.")
daysRented = int(input("How many rented days ? "))
KmWheeled = float(input("How many KM's rolled ? "))
totalToPay = (daysRented * 60) + (KmWheeled * 0.15)
print("The total to pay is ${:.2f}".format(totalToPay))

# Challenge 016
# Create a program that read a any number and show on the screen its integer portion.
print("Challenge 016")
print("Create a program that read a any number and show on the screen its integer portion.")
value = float(input("Enter a value: "))
portion = round(value)
print("The value typed was {} and its integer portion is {}".format(value, portion))

from math import hypot
# Challenge 017
# Make a program that measures the length of the opposite leg and the adjunct leg of the triangle,
# calculate and show the length of the hypotenuse.
print("Challenge 017")
print("Make a program that measures the length of the opposite leg and the adjunct leg of the triangle, ")
print("calculate and show the length of the hypotenuse. ")
oppositeLeg = float(input("Length of opposite leg: "))
adjacentLeg = float(input("Adjacent leg length: "))
hypotenuse = hypot(oppositeLeg, adjacentLeg)
print("The hypotenuse will measure {:.2f}".format(hypotenuse))

from math import sin, cos, tan, radians
# Challenge 018
# Make a program that reads any angle and shows on the screen the sine, cosine, and tangent value of that angle.
print("Challenge 018")
print("Make a program that reads any angle and shows on the screen the sine, cosine, and tangent value of that angle.")
angle = float(input("Enter the angle you want: "))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print("The angle of {} has the sine of {:.2f} ".format(angle, sine))
print("The angle of {} has the cosine of {:.2f} ".format(angle, cosine))
print("The angle of {} has the tangent of {:.2f} ".format(angle, tangent))

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