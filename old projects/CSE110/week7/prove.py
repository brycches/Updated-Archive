import random
guesses = 0
guess = 0
number = 0
print('this is a guessing game similar to wordle, you will guess a word and an underscore _ indicates that the letter was not present in the secret word. A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position. An uppercase letter indicates that the letter was present at that exact spot in the secret word.')

secret =str('sphynx')
secretl = len(secret)




while secret != guess:
    guesses = guesses+1
    guess = str(input(f'\nwhat is your guess?\n'))
    guess = guess.lower()
    if len(guess) != secretl:
        print(f'your guess must be {secretl} letters long, try again.')
        continue



    # for c, correct in enumerate(secret):
    #     for i, letters in enumerate(guess):
    #         if letters == correct and i == c:
    #             print(letters.upper(),end="")
    #         elif letters == correct:
    #             print(letters.lower(),end="")
    #             printed = True
    #         elif letters != correct and i == c and printed != True:
    #             print('_',end="")







            





    for i, letters in enumerate(guess):
        # print(f'i = {i}')
        printed = False
    #     # if letters[i] == secret[i]:
    #     #     print(letters.upper(),end = "")
    #     # elif letters[i] in secret:
    #     #     print(letters.lower(),end = "")
    #     # elif letters[i] != secret[i] and letters[i] not in secret:
    #     #     print('_',end="")
        for c, correct in enumerate(secret):
            # print(f'print c ={c}, correct is currently {correct}, letters is currently {letters} ouput in the for loop is\n ')
        # if secret[i] != letters:
        #     print('_',end="")


        # if correct == letters and i == c:
        #     print(letters.upper(),end="")
        #     printed = '1'
        #     break

        # elif correct == letters and i != c:
        #     print(letters.lower(),end="")
        #     printed = '2'
        #     break
            if letters == correct and i==c:
                print(letters.upper(),end="")
                printed = True
                break
            elif letters == correct and i != c:
                print(letters.lower(),end="")
                printed = True
                break
            else:
                printed = False
        #     print( '\nto there')
        # print('ouput that should only happen once is') 
        if printed != True:
            print('_',end="")
        # print('to there')
            
        
    continue

print(f'\nYou guessed it correctly! it took you {guesses} trys')

        



    # test = guess
    # if secret[0] == test[0]:
    #     Print[0] = secret[0].lower()
    # if secret[1] == test[1]:
    #     print(test[1].upper())
    # if secret[2] == test[2]:
    #     print(test[2].upper())
    # if secret[3] == test[3]:
    #     print(test[3].upper())
    # if secret[4] == test[4]:
    #     print(test[4].upper())
    # if secret[5] == test[5]:
    #     print(test[5].upper())
    # if secret[0] == test:
    #     print(secret[0].lower())
    # if secret[1] == test:
    #     print(secret[1].lower())
    # if secret[2] == test:
    #     print(secret[2].lower())
    # if secret[3] == test:
    #     print(secret[3].lower())
    # if secret[4] == test:
    #     print(secret[4].lower())
    # if secret[5] == test:
    #     print(secret[5].lower())
    # if secret[0] != test:
    #     print('_')
    # if secret[1] != test:
    #     print('_')
    # if secret[2] != test:
    #     print('_')
    # if secret[3] != test:
    #     print('_')
    # if secret[4] != test:
    #     print('_')
    # if secret[5] != test:
    #     print('_')