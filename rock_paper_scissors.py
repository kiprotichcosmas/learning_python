import random
options = ['rock', 'paper', 'scissors']
running = True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input('Enter your choice: ')

    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")


    if player == computer:
        print("It's a tie!")
    elif player == 'rock' and computer == 'scissors':
        print("You win!")
    elif player == 'paper' and computer == 'rock':
        print("You win!")
    elif player == 'scissors' and computer == 'paper':
        print("You win")
    else:
        print("You lose")
    if not input("Play again? (y/n): ").lower() == 'y':
        running = False


print("Thank you for playing!")