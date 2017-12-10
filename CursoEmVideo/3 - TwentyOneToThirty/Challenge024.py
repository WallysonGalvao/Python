"""Checking The First Letters Of A Text"""
print("Challenge 024")
print("Create a program that read the name of a city and tell if it begin or not with the name 'SANTO'")

city = str(input('What city do you born ?')).strip()
print(city[:5].upper() == 'SANTO')
