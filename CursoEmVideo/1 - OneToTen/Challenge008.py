""""Measurement converter"""

# Challenge 008
# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
print("Challenge 008")
print("Write a program that reads a value in meters and displays it converted to centimeters and millimeters.")
distanceInMeters = float(input("A distance in meters: "))
centimeters = distanceInMeters * 100
millimeters = distanceInMeters * 1000
print("The average of {}m corresponds to {}cm and {}mm".format(distanceInMeters, centimeters, millimeters))
