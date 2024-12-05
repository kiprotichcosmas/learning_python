import random
#print(help(random))

low = 1
high = 6
options = ("rock", "paper", "scissor")
cards = ["1","2","3","4","5","6","7","8","9",]
number = random.randint(low, high)
#number = random.random()

option = random.choice(options)

random.shuffle(cards)

print(cards)
print(number)
print(option)