

lives = int(3)
name = input('what is your name? ')
print (f'Hello {name} welcome to the dungeon')
print("""You will be given many choices, and the choices you make have
effects on your continuation inside the game, choose the wrong choice
you will die, restarting the game at the beginning. 
Now, let us play
""")

while True:

    
    choice1 = input('you find yourself in a damp cold stone room.\nfeatureless, except for a wooden door and a small sword hanging from a hook on the wall.\nDo you grab the sword, or open the DOOR? ')
    if 'door' in choice1.lower():
        lives = lives-1
        print('you find yourself face to face with a goblin, and without a sword it makes short work of you. you die.')
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else:
        print('you walk over and grab the sword off the wall, and feel it in your hands. \n1 short sword added to inventory.')
    choice2 = input('now you have a sword, would youn like to open the door? YES or NO? ')
    if 'no' in choice2.lower():
        print('you wait around, until suddenly a goblin bursts into the room!')
    else:
        print('you open the door, and find yourself face to face with a goblin!')
    choice3 = input('flashes of memory cascading through your mind, adrenaline pumping, you think of only three things you could do. \ntry to TALK to it, SWING your sword at it, or DODGE out of the way. which one do you choose? ')
    if 'talk' in choice3.lower():
        print('you try to talk to it, but apearently it doesn\'t speak english, and kills you')
        lives = lives-1
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    elif 'dodge' in choice3.lower():
        print('you dodge out of the way, but in these small\nconfines theres not much room, and the goblin still gets you. you die')
        lives = lives-1
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else:
        print("""you take the initiative and swing your sword, striking down your foe.\nnow looking through the open door you can see a long hallway, with a doorway at \nthe end to the left, and a doorway at the end on the right.
        """)
    choice4 = input('which way do you go? LEFT or RIGHT? ')
    if 'left' in choice4.lower():
        lives = lives-1
        print('you open the door to the left, and imediately three arrows come shooting out,\nand without any protection you are killed.')
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else: 
        print('opening the right door you find what apears to be a guard station,\nwith two very surprised looking goblins looking at you')
    choice5 = input('do you try to TALK to them, try to FIGHT them, or RUN back to the left door? ')
    if 'talk' in choice5.lower():
        print('you try to talk to them, but apearently they don\'t speak english, \nand as you try to talk to them one comes at you with thier sword, and kills you')
        lives = lives-1
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    elif 'run' in choice5.lower():
        lives = lives-1
        print('you open the door to the left, and imediately three arrows come shooting out,\nand without any protection you are killed.')
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else:
        print('taking advantage of thier momentary distraction with two mighty cleaves both goblins fall.\nbut now you can hear sounds coming from behind you. looking around you see a small shield leaning against the wall.')
    choice6 = input('do you take it? [YES or NO] ')
    if 'yes' in choice6.lower():
        shield = 'true'
        print('you grab the shield')
    else:
        print('you leave it there')
        shield = 'false'
    print('now turning back around you head for the door on the left.')
    choice7 = input('Do you open it? [YES or NO] ')
    if 'yes' in choice7.lower() and shield =='false':
        print('you open the door to the left, and imediately three arrows come shooting out,\n and without any protection you are killed.')
        print(f'you have {lives} lives left')
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    elif 'no' in choice7.lower():
        print('you prepare yourself to meet whatever is through the door')
    elif 'yes' in choice7.lower() and shield == 'true':
        print('you open the door, and three arrows come flying at you. raising your shield you deflect them.\nnow peering in you see a large shape, that of a hobgoblin!')
        choice75 = input('do you try to TALK to it, try to FIGHT it, or RUN away? ')
        if 'talk' in choice75.lower():
            print('you try to talk to it, but apearently it doesn\'t speak english, \nand as you try to talk to it it runs at you with its sword, killing you.')
            lives = lives-1
            print(f'you have {lives} lives left')
            if lives <= 0:
                print('you lose')
                break
            else:
                continue
        elif 'fight' in choice75.lower() or 'sword' in choice75.lower():
            print('you swing your sword at the hobgoblin, but it deftly parrys your sword to the side and swings its own sword at you, killing you in one blow.')
            lives = lives-1
            print(f'you have {lives} lives left')
            if lives <= 0:
                print('you lose')
                break
            else:
                continue
        else:
            lives = lives-1
            print('you try to run, but the hobgoblin is faster than you expected, and with one great swing it kills you.')
            print(f'you have {lives} lives left')
            if lives <= 0:
                print('you lose')
                break
            else:
                continue
    print('having prepared yourself, you hear footsteps getting closer and closer.' )
    choice8 = input('do you OPEN the door or WAIT? ')
    if 'wait' in choice8.lower():
        print('you here the sound of a chain, and then the door comes crashing open and before you stands a hobgoblin,\nand seeing you it quicky stabs with its sword, killing you')
        print(f'you have {lives} lives left')
        lives = lives-1
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    elif shield == 'false':
        print('you swing open the door, and three arrows get fired. two of them hit a hobgoblin standing in front of you, the source of the noise\nand the other flys at you, and without a shield you are struck and killed.')
        print(f'you have {lives} lives left')
        lives = lives-1
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else:
        print('you swing open the door, and three arrows get fired. Two of them hit a hobgoblin standing in front of you killing it instantly\nand the other flys at you, and with your shield you protect yourself.\nlooking down this new hallway you can see only one door at the very end.')
    choice9 = input('do you open the door? [YES or NO] ')
    if 'no' in choice9.lower():
        print('you kind of just stand there, and suddenly, three more arrows come flying at you. you try to raise your shield, but you just aren\'t quite fast enough, and die. ')
        print(f'you have {lives} lives left')
        lives = lives-1
        if lives <= 0:
            print('you lose')
            break
        else:
            continue
    else:
        
        print(F'you oepn the door and find yourself outside, free from the aweful dungeon.\nCONGRADULATIONS, YOU WIN! YOUR SCORE IS {lives}.')
        break






























