fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['apple', 'banana', 'orange', 'strawberry']
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(fruits)
# print(vegetables)
# print(meats)

# print(groceries[0])
#
# print(groceries[1][2])
# print(groceries[2][1])

#OR

types_of_food = [("milk", "tomato"),
                 ["mango", "oranges", "banana"],
                 ["chicken", "fish", "turkey"]]
for food in types_of_food:
    for f in food:
        print(f, end=" ")
    print()
    #