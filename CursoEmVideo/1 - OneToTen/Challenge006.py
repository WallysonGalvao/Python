""""Double, Triple, Square Root"""


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
