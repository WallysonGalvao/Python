"""Car Rent"""

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
