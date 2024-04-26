accounts = []
balances = []
account = ''
balance = 0
i = 0
total = 0
update = ''
greatest1 = 0
greatest2 = 0
greatestA = ''
greatestb = ''

while account.lower()!='quit':
    account = input('What is the name of your bank acount? (type quit to quit) ')
    if account.lower() != 'quit':
        try:
            balance = float(input('what is your acount balance? '))
        except:
            print('please enter a number, try again')
            continue
        accounts.append(account)
        balances.append(balance)

while i < len(accounts):
    print(f'{i+1}. {accounts[i]} - balance of ${balances[i]:.2f}')
    total = total + float(f'{balances[i]:.2f}')
    if balances[i] > greatest1:
        greatest1 = balances[i]
        greatestA = accounts[i]
    
    i=i+1

i=0
while update != 'no':
    update = input('would you like to update the amount stored in one of your acounts? ')
    if 'yes' in update.lower():
        try:
            which = int(input('which acount number would you like to update? (ex. \'1\' ) '))
        except: 
            print('please enter a number')
            continue
        if which > len(accounts)+1:
            print('please enter a valid number')
            continue
        amount = float(input(f'what is the new amount for {accounts[which-1]} '))
        balances[which-1] = amount
        while i < len(accounts):
            print(f'{i+1}. {accounts[i]} - balance of ${balances[i]:.2f}')
            total = total + float(f'{balances[i]:.2f}')
            if balances[i] > greatest2:
                greatest2 = balances[i]
                greatestb = accounts[i]
            i=i+1
            
if greatest1 > greatest2:
    print (f'your largest account is {greatestA} with a balance of ${greatest1:.2f}')
elif greatest1 < greatest2:
    print (f'your largest account is {greatestb} with a balance of ${greatest2:.2f}')
elif greatest1 == greatest2:
    print (f'your largest account is {greatestA} with a balance of ${greatest1:.2f}')



average = total/len(balances)


print (f'your total is ${total:.2f}')
print (f'your avarage is ${average:.2f}')





