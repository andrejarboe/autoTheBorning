import random

#Ask for their name
print('Hello what is your name?')
name = input()

print('Well, ' +name+ ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)
print('Take a guess...')

for guessTaken in range(1, 7):
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # tis sis for a correct guess

if guess == secretNumber:
    print('Good Job, ' +name+ '!!!')
    print('You guessed my number in ' +str(guessTaken)+ ' guesses.')
else:
    print('Nope. The number I was thinking of was ' +str(secretNumber)+ '...')
    print('You used all ' +str(guessTaken)+ ' of yor guesses.')
    print('************GAME OVER*************')

input("")