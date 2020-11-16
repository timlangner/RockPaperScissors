from random import randint

# create a list of play options
options = ['Rock', 'Paper', 'Scissors']

# assign a random play to the computer
computer = options[randint(0, 2)]

# set player to false
player = False

# while player is false
while not player:
    # set player to True
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', computer, 'covers', player)
        else:
            print('You win!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You lose!', computer, 'cut', player)
        else:
            print('You win!', player, 'covers', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose...', computer, 'smashes', player)
        else:
            print('You win!', player, 'cut', computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # ask for rematch
    rematch = input('Want to try it again? (Y/N)')
    if rematch.lower() == 'y':
        # set player to False so the while loop continues
        player = False
        # reassign an option to the computer
        computer = options[randint(0, 2)]
    else:
        print('Alright, was fun buddy!')
