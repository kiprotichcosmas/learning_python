# Python number guessing game

import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("Welcome to the Guess Game!")
print(f"Select a number between {lowest_number} and {highest_number}.")
while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("That number is out of range.")
            print(f"Select a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print(f"Your guess is too low.")
        elif guess > answer:
            print(f"Your guess is too high.")
        else:
            print(f"Your guess is correct. The answer is {answer}.")
            print(f"Your guesses are {guesses} ")
            is_running = False
    else:
        print("Please enter a number.")
        print(f"Please enter a number between {lowest_number} and {highest_number}.")

