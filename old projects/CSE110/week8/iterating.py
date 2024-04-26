
word = 'commitment'

letterf = input('What is your chosen letter? ')

letterf=letterf.lower()
word = word.lower()

for letters in word:
    if letters == letterf:
        print(letters.upper(), end="")
    else:
        print(letters.lower(), end="")
print("\n")
for letters in word:
    if letters == letterf:
        print('_',end="")
    else:
        print(letters,end="")
print("\n")




quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


cont = 'true'
while cont == 'true':
    numberc = int(input('how many characters between when we capitalize? '))
    for i, letters in enumerate(quote):
        if i % numberc == 0:
            print(letters.upper(), end="")
        else:
            print(letters.lower(),end="")
    while True:
        again = input('would you like to try again? ')
        if 'yes' in again.lower():
            cont = 'true'
            break
        elif 'no' in again.lower():
            cont = 'False'
            break
        else:
            print('please enter yes or no.')
            continue
    if cont == 'true':
        continue
    else:
        break


