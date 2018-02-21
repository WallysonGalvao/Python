"""Calculating Discounts"""

# Challenge 012
# Make an algorithm that read the price of a product and shows its new price, with a 5% discount.
print("Challenge 012")
print("Make an algorithm that read the price of a product and shows its new price, with a 5% discount.")
priceOfProduct = float(input("What is the product's price ? $"))
discount = priceOfProduct * 5 / 100
newPrice = priceOfProduct - discount
print("The product that costs ${:.2f}, in promotion with discount of 5% will cost ${:.2f}"
      .format(priceOfProduct, newPrice))
