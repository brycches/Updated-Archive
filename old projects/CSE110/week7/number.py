import random

attempts = 0
number = random.randint(1, 100)


while True:
    guess = int(input('guess a number between 1 and 100: \n'))
    if guess < number:
        print('Higher')
        attempts = attempts +1
        continue
    elif guess > number:
        print('Lower')
        attempts = attempts +1
        continue
    else:
        print(f'you guessed the magic number correctly! it took you {attempts} guesses.')
        again = input('would you like to play again? [yes, no] ')
        if 'yes' in again.lower():
            number = random.randint(1, 100)
            continue
        else:
            break

    

