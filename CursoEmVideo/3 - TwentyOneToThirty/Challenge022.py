"""Analyzing Texts"""
print("Challenge 022")
print("Create a program that reads a person's full name and shows: ")
print("> The name with all letters uppercase and lowercase.")
print("> How many letters in all (without considering spaces).")
print("> How many letters have the first name.")

yourName = str(input('Type your name: ')).strip()
firstName = yourName.split()[0]

print('Analyzing yout name...')
print('Your name in uppercase is {}'.format(yourName.upper()))
print('Your name in lowercase is {}'.format(yourName.lower()))
print('Your name have {} letters'.format(len(yourName) - yourName.count(' ')))
print('Your first name is {} and he have {} letters'.format(
    firstName, yourName.find(' ')))
