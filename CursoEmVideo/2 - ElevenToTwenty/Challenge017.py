"""Catatus and Hypotenuse"""

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
