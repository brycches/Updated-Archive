while True:
    number = int(input('please enter a positive number. '))
    if number >= 0:
        break
    print('that is not a positive number, please try again.\n')


while True:
    candy = input('can i have a candy please? ')
    if 'yes' in candy.lower():
        break
