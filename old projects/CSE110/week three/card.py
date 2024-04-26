"""
this program does somthing card related
"""
#get details for the order
amount = int(input('how many buisness cards do you need? '))
characterf = int(input('how many characters are on the front? '))
characterb = int(input('how many characters are on the back? '))

#calculate the order of cost

card_stock = .15
card_ink = .003
mark_up = .30

cost = card_stock * mark_up #base cost
cost += card_ink * mark_up * (characterf + characterb) #printing cost
cost *= amount #order cost * order amount
cost += cost * mark_up #markup order cost

print(f"order total: ${cost: .3g}")