"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

"""
A loop to make sure we recieve an integer as our input from the user
"""
while True:
    try:
        age = int(input('what is your age?'))
        break
    except:
        print('please enter a valid age')
        continue
"""
math to do the calculations for the max heart rate and your target 
rates for strengthening your heart
"""
max_heart = 220 - age

high = max_heart * .85
low = max_heart * .65

print(f'At {age} years old when you exercise to strengthen your heart, \nyou should be keeping your heart between {low} and {high} beats per minute')