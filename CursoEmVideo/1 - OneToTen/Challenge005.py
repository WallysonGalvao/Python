""""Predecessor and successor"""

# Challenge 005
# Make a program that read an integer and shows on the screen its successor and its predecessor.
print("Challenge 005")
print("Make a program that read an integer and shows on the screen its successor and its predecessor.")
userValue = int(input("Write a number: "))
successor = userValue + 1
predecessor = userValue - 1
print("Analysing the value {}, it's predecessor is {} and it's successor is {}"
      .format(userValue, predecessor, successor))
