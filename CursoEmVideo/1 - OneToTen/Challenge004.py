""""Dissecting a Variable"""

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
