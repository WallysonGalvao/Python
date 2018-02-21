"""Temperature Converter"""

# Challenge 014
# Write a program that convert a temperature typed in ºC and convert for ºF.
print("Challenge 014")
print("Write a program that convert a temperature typed in ºC and convert for ºF.")
temperatureCelsius = float(input("Enter the temperature in °C: "))
temperatureFahrenheit = ((9 * temperatureCelsius) / 5) + 32
print("The temperature of {}ºC corresponds {}ºF!".format(temperatureCelsius, temperatureFahrenheit))
