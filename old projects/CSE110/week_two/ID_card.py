first = input('What is your first name: ').capitalize()
last = input('what is your last name: ').upper()
email = input('what is your email address: ').lower()
phone = input ('what is your phone number: ')
job = input('what is your job title: ').capitalize()
ID = input('what is your ID number: ')

print('your ID card is\n')
print("----------------------------------------")
print(f"{last}, {first}")
print(f"{job}")
print(f"ID: {ID}\n")
print(f"{email}")
print(f"{phone}")
print("----------------------------------------")

# or you could just do 
"""
print (f"\n""
your ID card is
----------------------------------------
{last}, {first}
{job}
ID: {ID}

{email}
{phone}
----------------------------------------
"\n"")
"""
# example: 
"""First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------
"""