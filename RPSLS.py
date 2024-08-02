# Rock, Paper, Scissors, Lizard, Spock Game

import random
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
computer = random.choice(choices)

while True:
    player = None
    while player not in choices:
        player = input('Enter one of the following: rock, paper, scissors, lizard or spock: ').lower()

    print('-------------------')
    print(f'Player: {player}')
    print(f'Computer: {computer}')
    print('-------------------')

    if player == computer:
        print('Tie!')

    elif player == 'rock':                   # Rock wins scissors and lizard but loses to paper and Spock
        if computer == 'scissors':
            print('You win!!!')
        elif computer == 'lizard':
            print('You win!!!')
        elif computer == 'paper':
            print('You lose!!!')
        elif computer == 'spock':
            print('You lose!!!')

    elif player == 'paper':                  # Paper wins rock and Spock but loses to scissors and lizard
        if computer == 'scissors':
            print('You lose!!!')
        elif computer == 'lizard':
            print('You lose!!!')
        elif computer == 'rock':
            print('You win!!!')
        elif computer == 'spock':
            print('You win!!!')

    elif player == 'scissors':               # Scissors win paper and lizard but lose to rock and Spock
        if computer == 'paper':
            print('You win!!!')
        elif computer == 'lizard':
            print('You win!!!')
        elif computer == 'rock':
            print('You lose!!!')
        elif computer == 'spock':
            print('You lose!!!')

    elif player == 'lizard':                # Lizard wins paper and Spock but loses to scissors and rock
        if computer == 'scissors':
            print('You lose!!!')
        elif computer == 'paper':
            print('You win!!!')
        elif computer == 'rock':
            print('You lose!!!')
        elif computer == 'spock':
            print('You win!!!')

    elif player == 'spock':                 # Spock wins scissors and rock but loses to lizard and paper
        if computer == 'scissors':
            print('You win!!!')
        elif computer == 'paper':
            print('You lose!!!')
        elif computer == 'rock':
            print('You win!!!')
        elif computer == 'lizard':
            print('You lose!!!')
    
    print('-------------------')

    play_again = input('Play again? (yes/no): ').lower()

    if play_again != 'yes':
        print('Byeeeeeeee!')
        break
