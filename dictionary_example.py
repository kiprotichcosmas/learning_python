#Concession stand program

menu = {
    "Popcorn": 5.00,
    "Nachos": 4.50,
    "Hot Dog": 6.00,
    "Pizza Slice": 7.00,
    "Pretzel": 3.50,
    "Soda (Small)": 3.00,
    "Soda (Medium)": 4.00,
    "Soda (Large)": 5.00,
    "Water Bottle": 2.50,
    "Iced Tea": 3.50
}
cart = []
total = 0

print("----------Menu-----------")
for key, value in menu.items():
    print(f"{key:15}: ${value}")
print("----------Menu-----------")

while True:
    food = input("What would you like to order? (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print("----------Receipt-----------")
print(f"Total: {total}")

#print(f"The new food on the menu are: {cart}")




