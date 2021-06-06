import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('\n%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print("="*20)
    while True: # The player input loop.
        print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('\nType one of r, p, s, or q.')
        print("="*20)

    # Display what the player chose:
    if playerMove == 'r':
        print('\nROCK versus...')
    elif playerMove == 'p':
        print('\nPAPER versus...')
    elif playerMove == 's':
        print('\nSCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('\nIt is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('\nYou win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('\nYou win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('\nYou win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('\nYou lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('\nYou lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('\nYou lose!')
        losses = losses + 1