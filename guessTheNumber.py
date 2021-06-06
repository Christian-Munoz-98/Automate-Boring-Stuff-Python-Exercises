#This is a Guess the number game.
import random
secret_Number = random.randint(1,100)
print('I am thinking of a number between 1 and 100')

#Ask the player to guess 6 times.
for guesses_taken in range(1,11):
    print('Take a guess')
    guess = int(input())

    if guess < secret_Number:
        print('Your guess is too low')
    elif guess > secret_Number:
        print('Your guess is too high')
    else:
        break #This condition is the correct guess!

if guess == secret_Number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses')
else:
    print('Nope. The number i was thinking of was' + str(secret_Number))