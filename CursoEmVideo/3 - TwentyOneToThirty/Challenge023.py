"""Separating Digits from a Number"""
print("Challenge 023")
print("Make a program that read a number from 0 to 9999")
print("and show in the screen each one of digits separated.")
print("Ex: ")
print("Type a number: 1834")
print("Unit: 4; Tens: 3; Hundreds: 8; Thousands: 1")

number = int(input('Type a number: '))
unit = number // 1 % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print('Analyzing the number...')
print('Unit {}'.format(unit))
print('Tens {}'.format(tens))
print('Hundreds {}'.format(hundreds))
print('Thousands {}'.format(thousands))
