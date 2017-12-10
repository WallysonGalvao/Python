"""Looking For A String Within Another"""

print("Challenge 025")
print("Create a program that reads a person's name and says if it has 'SILVA' in the name")

fullName = str(input('Whats is your full name ?')).strip()

print("Your name has 'SILVA': {}".format('SILVA' in fullName.upper()))
