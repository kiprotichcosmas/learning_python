capitals = {
    "Kenya": "Nairobi",
    "United States": "Washington, D.C.",
    "United Kingdom": "London",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "South Africa": "Pretoria"
}

#print(capitals.get("Canada"))

# if capitals.get("Uganda"):
#     print("The Capita exists")
# else:
#     print("The Capita doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"Canada": "Toronto"})

# print(capitals)

# keys = capitals.keys()
# print(keys)
#or
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)
# #or
#
# for value in values:
#     print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")