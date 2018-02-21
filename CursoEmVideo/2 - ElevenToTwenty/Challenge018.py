"""Sine, Cosine, and Tangent"""

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
