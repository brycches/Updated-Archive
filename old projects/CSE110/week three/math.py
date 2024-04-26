import math
#getting thier age
age = input ('\nwhat is your age? ')
#doing math with thier age
age1 = int(age)
#printing age and age after next birthday
print (f'you are {age1} years old')

age2 = age1+1
print (f'after your next birthday you will be {age2} years old\n')
#asking how many cartons of eggs they have
cartons = int(input('how many cartons of eggs do you have? '))
#printing how many eggs and cartons they have
eggs = cartons*12
print (f'\nif you have {cartons} cartons, then you must have {eggs} eggs.\n')
#asking how many cookies thye have and how many people they are getting split between
cookies = int(input("how many cookies do you have? "))
people = int(input('how many people are you splitting the cookies between? '))
#using math to find the number of cookies per person
per_person = cookies/people
#printing number of straight divided cookies
print (f'\neach person will recieve {per_person} cookies')
#finding whole number and remainder cookies
remainder = cookies%people
whole_cookies = math.floor(per_person)
#printing whole cookies per person with the remainder
print (f'or, you will have {whole_cookies} whole cookies per person with a remainder of {remainder} cookies')