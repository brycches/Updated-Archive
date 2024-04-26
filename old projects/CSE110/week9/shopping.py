
remove = 0
shopping_list = []
shopping_price = []
option1=0
new_item_price = 0
total = 0


while option1 != 6:
    try:
        option1 = int(input("""
please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Edit Price
6. Quit
please enter the number asociated with your choice: """))
        print()
    except:
        print('please enter a number 1 through 6')
        continue

    if option1 == 1:
        new_item = input('what item would you like to add to your shopping list? ')
        shopping_list.append(new_item)
        while True:
            try:
                new_item_price = float(input(f'What is the price of {new_item}? $'))
                break
            except:
                print('please enter a valid price')
                continue
        shopping_price.append(new_item_price)
        print (f'{new_item} has been added to your shopping list')
        continue
    
    elif option1 == 2:
        print('you would like to view your shopping list. your list is: ')
        for i, item in enumerate(shopping_list):
            print(f'{i+1}. {item} price: ${shopping_price[i]:.2f}')
            continue
    
    elif option1 == 3:
        print('your current shopping list is: ')
        for i, item in enumerate(shopping_list):
            print(f'{i+1}. {item} price: ${shopping_price[i]:.2f}')
        while True:
            try:
                remove = int(input('which item number would you like to remove?'))
                if remove > (len(shopping_list)):
                    print(x)
                break
            except:
                print('Error. Please try again and enter the item number on your shopping list.')
                continue
        remove = remove-1
        del shopping_list[remove]
        del shopping_price[remove]
        print('your item has been removed.')
        




        continue
    elif option1 == 4:
        print ('your subtotal comes to: ')
        for price in shopping_price:
            total = price + total
        print(f'your subtotal comes to: ${total:.2f}')
        tax = total * 1.06
        print(f'after tax your total comes to: ${tax:.2f}')
        tax = 0
        total = 0
        continue
    elif option1 == 5:
        while True:
            print('your current shopping list is: ')
            for i, item in enumerate(shopping_list):
                print(f'{i+1}. {item} price: ${shopping_price[i]:.2f}')
            try:
                which = int(input('which item number\'s price would you like to update? (ex. \'1\' ) '))
            except: 
                print('please enter a valid item number')
                continue
            if which > len(shopping_list):
                print('please enter a valid number')
                continue
            try:
                amount = float(input(f'what is the new price for {shopping_list[which-1]} $'))
            except:
                print('please enter a number')
                continue
            shopping_price[which-1] = amount
            break
        print(f'{shopping_list[which-1]} now has a price of ${shopping_price[which-1]:.2f}')
        continue
        continue
    elif option1 == 6:
        print('goodbye')
        break






