number_items = int(input("Number of items:"))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))
item_price = 0
total_price = 0
for i in range(number_items):
    item_price = (int(input("Enter price of item: $")))
    total_price += item_price
if total_price > 100:
    print("Total price is $", total_price - (total_price * 0.1))
else:
    print("Total price is $", total_price)



#Solution
"""
CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for j in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print("Total price for ", number, " items is $", total, sep='')

# with string formatting for currency output
print("Total price for {} items is ${:.2f}".format(number, total))