"""
getting ->
The price of a child's meal (floating point)

The price of an adult's meal (floating point)

The number of children (integer)

The number of adults (integer)

The sales tax rate (floating point)
"""

pricec = float(input("What is the price of a child's meal? $"))

pricea = float(input("what is the price of an adult's meal? $"))

children = float(input("how many children are there? "))

adults = float(input("how many adults are there? "))

tax = float(input("what is the sales tax rate? (for 6% write 6) "))

lunch = input("is it lunch time? (y/n):")

if lunch == "n" : 

    #finding subtotal
    subtotal = (pricec * children)+(pricea * adults)
    #printing subtotal
    print(f'your subtotal is ${subtotal:.3g}')
    #finding total by multiplying the subtotal by 100% +the sales tax
    total = subtotal * (1+(tax/100))
    #printing the total
    print(f'your total is ${total:.3g}')
    #asking for how much they pay
    payment = float(input("what is your payment amount? "))
    #calculating thier change
    change = payment-total
    #displaying thier change
    print(f'your change is ${change}')

else: 
    #finding subtotal with lunch special
    subtotal = ((pricec * children)+(pricea * adults))* .9
    #printing subtotal
    print(f'your subtotal with the 10% lunch discount is ${subtotal:.2f}')
    #finding total by multiplying the subtotal by 100% +the sales tax
    total = subtotal + (subtotal * (tax/100))
    #printing the total
    print(f'your total is ${total:.2f}')
    #asking for how much they pay
    payment = float(input("what is your payment amount? "))
    #calculating thier change
    change = payment - total
    #displaying thier change
    print(f'your change is ${change:.2f}')


