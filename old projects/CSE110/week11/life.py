
expectancy1 = 99999999
expectancy2 = 0
desired = 0
average = 0
z=0
expectancy6 = 9999999
expectancy7 = 0
expectancy4 = 9999999
expectancy5 = 0
averaged = 0
x=0
w=0
t=0
average1 = 0
place = ''

while True:
    expectancy1 = 99999999
    expectancy2 = 0
    average = 0
    z=0
    expectancy6 = 9999999
    expectancy7 = 0
    expectancy4 = 9999999
    expectancy5 = 0
    averaged = 0
    x=0
    w=0
    t=0
    while desired == 0:
        try:  
            desired = int(input('what year are you interested in? '))
            break
        except:
            print('please enter a valid year')
            continue
        break
    while place == '':
        try:  
            place = str(input('what country are you interested in learning about? '))
            break
        except:
            print('please enter a valid place')
            continue
        


    with open("CSE110/week11/life-expectancy.csv") as life_expectancy:
        for i, line in enumerate(life_expectancy):
            parts = line.split(',')
            percent = parts[3]
            percent = float(percent)
            if percent < expectancy1:
                expectancy1 = percent
                place1 = parts[0]
                year1 = parts[2]
            if percent > expectancy2:
                expectancy2 = percent
                place2 = parts[0]
                year2 = parts[2]
            year3 = int(parts[2])

            if year3 == desired:
                average = average + percent
                z = z+1
            try: averaged = average/z
            except: pass
            if year3 == desired:
                x=1
                if percent < expectancy4: 
                    expectancy4 = percent
                    place4 = parts[0]
                    year4 = parts[2]
                if percent > expectancy5:
                    expectancy5 = percent
                    place5 = parts[0]
                    year5 = parts[2]
                    x=1

            placed = parts[0].strip().lower()        
            if placed == place.lower():
                average1 = average1 + percent
                w = w+1
            try: average2 = average1/w
            except: pass
            if placed == place.lower():
                t=1
                if percent < expectancy6: 
                    expectancy6 = percent
                    place6 = parts[0]
                    year6 = parts[2]
                if percent > expectancy7:
                    expectancy7 = percent
                    place7 = parts[0]
                    year7 = parts[2]
                    t=1
    # if x == 1 and t == 1:
                
            


        
        try:
            print (f'In the year {desired}, the country with the lowest life expectancy is {place4.capitalize()} with a life expectance of {expectancy4} years old')
            print (f'In the year {desired}, the country with the highest life expectancy is {place5.capitalize()} with a life expectance of {expectancy5} years old,')
            print(f'In the year {desired} the average lifespan was {averaged}')
            
        except:
            print('to show your results, please enter a valid year ex. 2001')
            desired = 0
            continue
        try:
            print (f'in the year {year6}, {place} had the lowest life expectancy of {expectancy6} years old')
            print (f'the the year {year7}, {place} had it\'s highest life expectancy of {expectancy7} years old,')
            print(f'In the country of {place} the average lifespan was {average2}')
        
            
        except:
            print('to show your results, please enter a valid place ex. Spain')
            place = ''
            continue

        print (f'The country with the overall lowest life expectancy is {place1.capitalize()} with a life expectance of {expectancy1} years old, as recorded in the year {year1}')
        print (f'The country with the overall highest life expectancy is {place2.capitalize()} with a life expectance of {expectancy2} years old, as recorded in the year {year2}')
        while True:
            again = input('would you like to learn about another year and place? [yes or no] ')
            if 'yes' in again.lower():
                desired = 0
                break
            if 'no' in again.lower():
                desired = 1
                break
            else:
                print('sorry, i didn\'t understand that, please try again')
                continue
        if desired == 0:
            continue
        if desired == 1:
            break
    # else:
    #     print('please enter a valid year or place')
    #     desired = 0
    #     place = ''
    #     continue