# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      It is a program meant to see whether a player of the game monopoly
#      can put a hotel on pensylvania avenue
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?

""" The hardest part for me was figuring out how to do the "end" bubbles from the flow chart.
I had code that worked within 45 minutes. It gives all the outputs
correctly but since it used a while loop and break commands I knew I would be marked down.
As clearly the break command for a while loop is considered swearing in this class
and was the only way tought to us in previous classes to skip code to the end.
I spent 2 hours researching how to skip code without swearing, and another hour
getting it to work right. So I used a function with empty return statements to skip my code. 
Functions, not beinga part of this class and not taught in the prerequisite classes, 
took me a while to figure out. But now my code doesnt have break statements so thats great.
"""
# 5. How long did it take for you to complete the assignment?
#      over 4 hours



# first iteration of code, which I then turned into a function for the test cases.
# if you want to run it using the user's input this still works, or you can remove
# the commented input lines from the function
"""
while True:


    CG = input("do you own all the properties in pensylvania avenue's color group? [y/n]: ")

    if CG.lower() == "n":
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        break

    PA = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))

    if PA == 5:
        print("You cannot purchase a hotel if the property already has one.")
        break

    NC = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))

    if NC == 5:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses. ")
        break


    PC = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))

    if PC == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses. ")
        break

    houses_needed = 12 - PC - NC - PA

    cash_needed = (houses_needed * 200) + 200

    PC_needed = 4 - PC
    NC_needed = 4 - NC
    PA_needed = 4 - PA

    hotels = int(input("How many hotels are there to purchase? "))

    if hotels == 0:
        print("There are not enough hotels available for purchase at this time.")
        break

    houses = int(input("How many houses are there to purchase? "))

    if houses < houses_needed:
        print("There are not enough houses available for purchase at this time. ")
        break

    cash = int(input("How much cash do you have to spend? "))

    if cash < cash_needed:
        print("You do not have sufficient funds to purchase a hotel at this time. ")
        break

    print(f\"""This will cost ${cash_needed}.
Purchase 1 hotel and {houses_needed} house(s).
Put 1 hotel on Pennsylvania and return any houses to the bank.\""")
    if PC_needed >= 1:
         print(f"Put {PC_needed} house(s) on Pacific.")
    if NC_needed >= 1:
         print(f"Put {NC_needed} house(s) on North Carolina.")
    
    break
"""

              
    


def monopoly(CG, PA, NC, PC, hotels, houses, cash):
     # CG = input("do you own all the properties in pensylvania avenue's color group? [y/n]: ")

    # Check if the color group is owned
    if CG.lower() == "n":
        print("You cannot purchase a hotel until you own all the properties of a given color group.")
        return

    # PA = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    # Check if Pennsylvania Avenue already has a hotel
    if PA == 5:
        print("You cannot purchase a hotel if the property already has one.")
        return

    # NC = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    # Check if North Carolina Avenue has a hotel
    if NC == 5:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses. ")
        return


    # PC = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel): "))
    # Check if Pacific Avenue has a hotel
    if PC == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses. ")
        return

    # Calculating information to be used later in the function
    houses_needed = 12 - PC - NC - PA

    cash_needed = (houses_needed * 200) + 200

    PC_needed = 4 - PC
    NC_needed = 4 - NC
    PA_needed = 4 - PA

    # hotels = int(input("How many hotels are there to purchase? "))
    # Check if there are enough hotels available for purchase
    if hotels == 0:
        print("There are not enough hotels available for purchase at this time.")
        return

    # houses = int(input("How many houses are there to purchase? "))
    # Check if there are enough houses available for purchase
    if houses < houses_needed:
        print("There are not enough houses available for purchase at this time. ")
        return

    # cash = int(input("How much cash do you have to spend? "))
    # Check if there is sufficient cash to purchase a hotel
    if cash < cash_needed:
        print("You do not have sufficient funds to purchase a hotel at this time. ")
        return

    print(f"""This will cost ${cash_needed}.
Purchase 1 hotel and {houses_needed} house(s).
Put 1 hotel on Pennsylvania and return any houses to the bank.""")
    if PC_needed >= 1:
        print(f"Put {PC_needed} house(s) on Pacific.")
    if NC_needed >= 1:
        print(f"Put {NC_needed} house(s) on North Carolina.")        



# Function calls with values from each test case
print("\nTest case 1\n")
monopoly ("n", 0, 0, 0, 10, 10, 1000)
print("\nTest case 2\n")
monopoly ("y", 0, 0, 0, 10, 15, 100)
print("\nTest case 3\n")
monopoly ("y", 0, 0, 0, 10, 10, 9000)
print("\nTest case 4\n")
monopoly ("y", 4, 4, 5, 0, 0, 0)
print("\nTest case 5\n")
monopoly ("y", 4, 5, 4, 0, 0, 0)
print("\nTest case 6\n")
monopoly ("y", 5, 4, 4, 10, 10, 1000)
print("\nTest case 7\n")
monopoly ("y", 0, 0, 0, 3, 12, 3000)
print("\nTest case 8\n")
monopoly ("y", 3, 3, 3, 1, 3, 5000)
