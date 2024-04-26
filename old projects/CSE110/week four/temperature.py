import math

print('this chalculator will convert from Fahrenheit to celsius or celsius to Fahrenheit\nIf you are using celsius to begin with skip the Fahrenheit box')
temperaturef = float(input('what is the temperature in farenheit? '))

temperaturec = float(input('what is the temperature in celsius? '))

degreec = (temperaturef - 32) * (5 / 9)

degreef = (temperaturec * (9 / 5)) + 32

print(f'{temperaturef} degrees Fahrenheit is equal to {degreec} degrees celsius. \n{temperaturec} degrees celsius is equal to {degreef} degrees Fahrenheit.')



