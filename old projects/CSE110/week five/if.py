


number1 = float(input('what is your first number? '))
number2 = float(input('what is your second number? '))

if number1 > number2:
    print(f'your fist number is larger than your second number, {number1}>{number2}')
else:
    if number2 > number1:
        print(f'your second number is larger than your first number, {number2}>{number1}')
    else:
        print(f'your fist number is equal to your second number, {number1}={number2}')



animal1 = input('what is your favorite animal? ')

animal1 = animal1.lower()

if 'falcon' in animal1:
    print('your favorite animal is the same as mine.')
else:
    print('your favrite animal is not the same as mine.')


while True:
    try:
        ans = input('guess my favorite animal ')
    except ValueError:
        print('i didn\'t understand that, try types of meat eating birds. \n')
        continue
    if 'falcon' in ans.lower():
        print('you are correct! ')
        break
    else:
        print('you are incorrect, try types of birds')
