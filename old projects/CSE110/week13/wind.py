tempf = 0
tempt = ''
windspeed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
def fahrenheit():
    tempf = float(input('please enter the current temperature in farenheit. '))
    windf = float(input('please enter the current windspeed in miles per hour. '))
    tempfw = ((35.74 + 0.6215*tempf) - (35.75*(windf**0.16)) + (0.4275*tempf*(windf**0.16)))
    print(f'the current windchill temperature at your given wind speed of {windf} MPH is {tempfw:.2f} degrees farenheit.')
    for windfx in windspeed:
        tempfx = ((35.74 + 0.6215*tempf) - (35.75*(windfx**0.16)) + (0.4275*tempf*(windfx**0.16)))
        print(f'the windchill for {tempf} at {windfx} MPH is {tempfx:.2f} degrees farenheit')
def celcius():
    tempc = float(input('please enter the current temperature in celcius. '))
    windc = float(input('please enter the current windspeed in miles per hour. '))
    tempcf = (tempc * (9/5))+32
    tempcw = ((((35.74 + 0.6215*tempcf) - (35.75*(windc**0.16)) + (0.4275*tempcf*(windc**0.16)))-32)*(5/9))
    print(f'your current windchill temperature is {tempcw:.2f} degrees celcius.')
    for windcx in windspeed:
        tempcx = ((((35.74 + 0.6215*tempcf) - (35.75*(windcx**0.16)) + (0.4275*tempcf*(windcx**0.16)))-32)*(5/9))
        print(f'the windchill for {tempc} degrees celcius with {windcx} MPH wind, windchill is {tempcx:.2f} degrees celcius')
while True:
    tempt = input('will you be using farenheit or celcius? (F/C):\n')

    if tempt.lower() == 'f':
        fahrenheit()
        break
    elif tempt.lower() == 'c':
        celcius()
        break
    else:
        print('please enter F or C for your desired temperature type.')
        continue



