"""
Enter price: 24.72
Enter discount %: 15
Price with discount: 21.01
Reduction: 3.71
"""

price = float(input("Enter price: "))
discount_percent = float(input("Enter discount %: "))

price_with_discount = price * (1 - discount_percent / 100)
reduction = price - price_with_discount

print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")
