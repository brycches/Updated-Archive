inp = ''
storage = []

while inp != 'quit':
    inp = input('Please enter the items of the shopping list (type: quit to finish): ')
    if inp == 'quit':
        break
    else:
        storage.append(inp)
        continue


print('the shopping list is:')
for items in storage:
    print(f'{items}')

print('the items on your list with thier index numbers is: ')
for i, items in enumerate(storage):
    print(f'{i}. {items}')

change = int(input('what number would you like to change? '))
new = input('what would you like to change it to? ')

storage[change] = new

for items in storage:
    print(items)
