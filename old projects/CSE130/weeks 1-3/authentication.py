# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
# Get a username and a password from a user, and match it against a list of authenticated users.
# If what they entered matches the list, authenticating them, and if not having them try again. 
# 4. What was the hardest part? Be as specific as possible.
# figuring out how exactly to split the json object into two variables. another big problem was
# figuring out why my first hard coded test through an error but none of the others. it had to do
# with my password_check variable, but i figured it out. Also adding maticulous coments took some time.
# Was the syntax of Python the hardest part? If so, what part?
# yes and no, i did not realize you had to put '' around the key to the json list. which took a bit to
# figure out even after looking up syntax as the quotes are sometimes easy to miss.
# Was there some aspect of the problem that was particularly difficult to solve?
# finding the error in the first hard coded problem was difficult, fixing it wsa not really difficult.
# but after you get so many lines of code, I needed a way to figure out what wrong with the first one.
# my try catch was just returning the print statement of unable to access the file, but none of the 
# other ones were. so i didn't think it was the file's fault, it had to be somthing with my code. I
# after reading over my code and not seeing any problems I was just confused, so i removed the try catch
# from the loop, to see if VScode could figure it out, and they pointed me to the if statement
# for the password authenticator, which said password_check was not defined. I relized that i only defined
# it if the username was in the list, meaning with an incorrect username it would just crash. I fixed
# this by defining it outside of the if statements but inside of the loop to being equal to 1 + the number
# of items in the list, meaning it would never be true without a correct username. I then encountered
# tons of errors because of how i had set it up, and had to define it as 0 outside the loop so that the
# adder would work.
# Was there an especially difficult bug? If so, how did you resolve it?
# yes, password_check  needed to be defined, and i added the redundancy so no matter how long the
# json list was it wouldn't return a false positive.
# Was there some difficulty with the instructions or any part of the problem definition?
# no, it was a bit vague on the whole the json code needs to be from a different file and not just
# coded into the beginning of the python file as a dictionary, but it worked either way.
# 5. How long did it take for you to complete the assignment?
# about 3 to 4 hours, probably closer to 4




import json

# This is my code, it has been commented out in order for my hard coded test cases to run in under 1 minute
# if you would like to run it without it being commented out, remove the tripple """ at the beginning and end

"""
# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0


while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
    
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user
    given_username = input('Username: ')
    given_password = input('Password: ')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')

# Telling the user they have been authorized.
print('You are authorized to use this system.')
"""





# hard coding the test cases so i dont have to type everything in 1 minute. Some edits were made
# to the original code such that the you are authorized message would not display if the while loop
# was broken by the break commands that were added to prevent infinte loops in the hard coded examples




# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
# Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'John Cheese'
    print(f'Username: {given_username}')
    given_password = 'None shall pass'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')



# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'Black Knight'
    print(f'Username: {given_username}')
    given_password = 'Tis but a scratch.'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')




# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'John Cheese'
    print(f'Username: {given_username}')
    given_password = 'Tis but a scratch.'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')





# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'King Arthur'
    print(f'Username: {given_username}')
    given_password = 'Bring out your dead!'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')



# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'Black Knight'
    print(f'Username: {given_username}')
    given_password = 'None shall pass'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')





# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'King Arthur'
    print(f'Username: {given_username}')
    given_password = 'Run away!'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')






# Before getting any input from the user authentications should always be False.
authentication = False
auth_username = False
auth_password = False
# Password check needs to be defined
password_check = 0
while authentication == False:
  # Error catching the opening of a file, printing unable to open file if unsuccessful
  try:
    # Opening the file in the read state
    file = open("lab02.json", "r")
    # Storing all the text read from the file into a string variable
    text = file.read()
    # loading all that text into a json object named data
    data = json.loads(text)
    # Closing the file
    file.close()
  
  
    # Storing the two different parts of the object into seperate variables based on the keys in the data.
    usernames = data['username']
    passwords = data['password']
    # Finding the number of items in the list
    for number in usernames:
    # password_check will not be defined unless a correct username is entered, throwing an error.
    # thus it needs to be an integer outside the number of items in the data lists
      password_check += 1
    # This code ensures password_check is defined and outside the bounds of the number of usernames
    password_check = password_check + 1
    # Getting the Username and Password from the user (hard coded for the demo video)
    given_username = 'French Soldier'
    print(f'Username: {given_username}')
    given_password = 'I fart in your general direction'
    print(f'Password: {given_password}')
    # Checking if the entered username is an authorized username by looping through the list
    for user_number, username in enumerate(usernames):
      # Finding if the username is an authorized one
      if given_username == username:
        # If it is authorized it will change the username to authenticated.
        auth_username = True
        # It will store the number in the list that came back as authorized to make sure the password
        # is for the same username
        password_check = user_number

    # Checking if the entered password is an authorized password by looping through the list
    for password_number, password in enumerate(passwords):
      # Finding if the entered password is both an authorized password and if it is the 
      # correct password for the username that was given.
      if given_password == password and password_check == password_number:
        # If it is authorized it will change the password to authorized
        auth_password = True
    # Checking if both username and password are authorized together
    if auth_username == True and auth_password == True:
      # Exiting the loop and authenticating the user
      authentication = True
    # If it does not authorize it will display a message telling them they are not 
    # authorized and restart the loop
    else:
      print('You are not authorized to use this system.')
      # I added a break here for the hard coded test cases so as to not create infinite loops and move 
      # to the next use case
      break
  # If the file doesn't open or an error gets thrown, it will tell the user
  except:
    print('unable to open file lab02.json. ')
    # It will also not try to loop back to the beginning if the file was unable to be read
    break
  # Telling the user they have been authorized.
  print('You are authorized to use this system.')




# a reference for the coder to see what is inside the json file without having to jump back and forth

"""
data = {
    "username": [
    "King Arthur",
    "Lancelot",
    "Sir Robin, the Not-Quite-So-Brave",
    "Black Knight",
    "Sir Bedivere",
    "Roger the Shrubber",
    "Brother Maynard",
    "Bridgekeeper",
    "French Soldier",
    "Knight of Ni",
    "Dead Collector",
    "Dennis",
    "King of Swamp Castle"
  ],
  "password": [
    "Run away!",
    "She turned me into a newt!",
    "That's enough singing for now",
    "None shall pass",
    "How do you know so much about swallows?",
    "Oh, what sad times are these when passing ruffians can say Ni at will to old ladies.",
    "Armaments, chapter two, verses nine through twenty-one",
    "What... is the air-speed velocity of an unladen swallow?",
    "I fart in your general direction",
    "You must cut down the mightiest tree in the forest... WITH... A HERRING!",
    "Bring out your dead!",
    "Help, I'm being oppressed",
    "Let's not bicker and argue over who killed who"
  ]
}
"""