# 1. Name: 
#    -Bryce Chesley-
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
"""
This program is meant to be a short game where the user guesses a random number, and the
program tells them if they have guessed too high or low.
""" 
# 4. What was the hardest part? Be as specific as possible.
"""
This program was mostly review, however I did have to shake off the cobwebs of how arrays
worked. so I would have to say that the hardest part was definitely remembering the different
commands that deal with arrays, such as len(), .append() and how to make the array
variable an array not a string. Bug fixing was also a bit challenging, but once I realized
that I had used the wrong < and > symbols throughout it solved itself pretty quick.

Another challenging thing at least for me as I am not used to doing it, is adding comments
to the code, explaining what everything does. This wasn't particularly difficult,
however it did take me much more time to add the comments than not adding them. 
Another dificulty was capturing a screen recording, as I had no idea how you wanted
this done, and to find a screen recording software that could capture my face was 
difficult. then i remembered zoom had a recording function, and using this I was able
to record the video of my code working.
"""
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-
#   probably around 1 hour, an hour and a half maximum.  

import random

# Game introduction.
print('This is the "guess a number" game.\nYou try to guess a random number in the smallest number of attempts.')
# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = 2 # Any integer will work here.
while True:
    try:
        value_max = int(input('Enter a positive integer greater than one '))
        if value_max<1:
            print('your value must be greater than 1')
            continue
        else:
            break
    except:
        print('please enter a whole number')
        continue

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f'please guess a number between 1 and {value_max}')
# Initialize the sentinal and the array of guesses.
array = [] # This is the array we will store the guesses in, it should start blank.
guessed = 0 # This must be an integer that cannot be within the range of our guessing game.
# Play the guessing game.
while guessed != value_random:
    try:
            # Prompt the user for a number.
        guessed = int(input(''))
            # Store the number in an array so it can be displayed later.
        array.append(guessed)
            # Make a decision: was the guess too high, too low, or just right.
        if guessed>value_random:
            print(' too high')
            continue
        elif guessed<value_random:
            print(' too low')
            continue
        else:
            break
    # Error handling for if the user doesn't enter a number.
    except:
        print('please enter a whole number')
        continue

# Give the user a report: How many guesses and what the guesses where.
print(f'You were able to find the number in {len(array)} guesses.')
print(f'The numbers you guessed were: {array}')










