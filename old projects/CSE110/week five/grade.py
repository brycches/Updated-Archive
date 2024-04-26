import math
from turtle import goto



grade = float(input('what is your grade percentage? '))

if grade >= 90:
    # print('you have an A')
    letter = 'A'
    fail = 'f'
elif grade >=80:
    # print('you have a B')
    fail = 'f'
    letter = 'B'
elif grade >=70:
    # print('you have a C')
    fail = 'f'
    letter = 'C'
elif grade >=60:
    # print('you have a D')
    fail = 't'
    letter = 'D'
elif grade >=1:
    # print('you have an F')
    fail = 't'
    letter = 'F'
else:
    print('please enter a valid grade percentage')
    letter = 'j'
    fail = 'n'


plus = grade % 10 

if plus >=7 and letter != 'A' and letter != 'F' :
    letter = (f'{letter}+')
    
elif plus <3 and letter != 'F':
    letter = (f'{letter}-')


if 'A' in letter or 'F' in letter:
    print (f'you have an {letter}')
elif 'B' in letter or 'C' in letter or 'D' in letter:
    print (f'you have a {letter}')
else:
    print('')



if fail == 'f':
    print ('your grade is enough to pass the class')
elif grade >=1 and fail == 't':
    print('your grade is not enough to pass')
else:
    print('')







