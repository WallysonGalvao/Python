"""First and Last Name of a Person"""

print("Challenge 027")
print("Make a program that reads a person's full name,")
print("then displays the first and last name separately.")
print("Ex: Ana Maria de Souza")
print("First name: Ana")
print("Last name: Souza")

fullName = str(input("Type your full name: ")).strip()
separatelyName = fullName.split()


print("Very nice to meet you!")
print("Your first name is {}".format(separatelyName[0]))
print("Your last name is {}".format(separatelyName[len(separatelyName) - 1]))
