
# Put a friendly greeting on screen.
print('\n\nhello world\n\n')

#printing this is cse 130 but 130 is an integer.
print(f'this is CSE {int(130)}\n\n')

numbers = [2,4,6]
for data in numbers:
    print(data)

while True:
    try:
        age = int(input('what is your age?'))
        break
    except:
        print('please enter a number')
        continue

print(f'\n\n{age}\n\n')

# try to count to whatever you need to
"""
#this doesnt work idk why

start = int(input('what number do you want to start with?'))
end = int(input('what number do you want to end with?'))

for values in range[start, end]:
    print(f'{values}')

answer = 'nothing' #anything but stop will work
while answer != 'stop':
    answer = input('do you want to keep going?')

print('the loop has been broken')
"""
gender = (input('what is your gender?')).lower

if gender == 'male':
    is_male = True
else:
    is_male = False

