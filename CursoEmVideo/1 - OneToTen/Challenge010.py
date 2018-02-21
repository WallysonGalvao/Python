""""Currency converter"""

# Challenge 010
# Create a program that read how much money a person has in the wallet and shows how much money they can buy.
print("Challenge 010")
print("Create a program that read how much money a person has in the wallet and shows how much money they can buy.")
money = float(input("How much money do you have in the wallet ? $"))
reais = money * 3.28
print("With ${:.2f} dollars you can buy R${:.2f} reais".format(money, reais))
