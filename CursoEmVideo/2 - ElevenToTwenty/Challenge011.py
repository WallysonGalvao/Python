"""Painting wall"""

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
