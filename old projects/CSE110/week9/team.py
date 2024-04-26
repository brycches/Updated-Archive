
number = int(7)
output =[]
total = int(0)
thing = int(0)
it = int(0)
yes = 0
numbers = []
no = 0
closest = 99999999999999999999999999999999
while number != 0:

    number = float(input('enter a number, enter 0 to end. '))
    if number == 0:
        break
    else:
        output.append(number)


output.sort(reverse=False)
print (f'your numbers in numerical order are')
for variable in output:
    print (variable)
for stuff in output:
    total += stuff
    if stuff > yes:
        yes = stuff
    

print (f'the total of your numbers is {total}')

for things in output:
    thing = thing + things
    it += 1
    if things < closest and things > 0:
        closest = things
    
print (f'the average is {thing/it}')
print (f'the largest number is {yes}')
print (f'the smallest number greater than zero is {closest}')



