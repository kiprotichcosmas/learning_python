print("Welcome")

print("To my Shopping List:")

foods =[]
prices = []

total = 0

while True:
    food = input("Enter a food to buy (q to quit): ) ")
    if food.lower() != "q":
        price = float(input(f"Enter a price of {food}: $ "))
        foods.append(food)
        prices.append(price)
    else:
        break

#print(f"Total price is {prices}")

print("--------YOUR RECEIPT---------")
for food in foods:
    print(food, end=",")
for price in prices:
    total += price

print()
print(f"Your Total is : {total}")

