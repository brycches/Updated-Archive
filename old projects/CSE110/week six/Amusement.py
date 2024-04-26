rider2h = 0
rider2a = 0
double = False
rider1h = float(input('what is the height of the first rider? '))
rider1a = float(input('what is the age of the first rider? '))
second = input('is there a second rider? [yes/no] ')

if 'yes' in second.lower():
    rider2h = float(input('what is the height of the second rider? '))
    rider2a = float(input('what is the age of the second rider. '))


if rider1a >= 12 and rider1a <= 17:
    golden1 = input('is rider 1 a golden ticket holder? [yes/no] ')
    if 'yes' in golden1.lower():
        rider1a = 18

if rider2a >= 12 and rider2a <= 17:
    golden2 = input('is rider 2 a golden ticket holder? [yes/no] ')
    if 'yes' in golden2.lower():
        rider2a = 18


if rider1a >= 14 and rider2a >= 16:
    double = True
elif rider2a >= 14 and rider1a >= 16:
    double = True


if rider1a >= 18 or rider2a >= 18:
    double = True
elif rider1a >= 12 and rider1h >= 52 and rider2a >= 12 and rider1h >=52:
    double = True


if rider1h < 36 and 'no'in second.lower():
    print('you can not ride.')

if rider1a >= 18 and rider1h > 62 and 'no' in second.lower():
    print('you may ride. ')

if rider1a < 18 and 'no' in second.lower() or rider1h < 62 and 'no' in second.lower():
    print('you may not ride. ')
    print (f'{second}')

if 'yes' in second.lower() and double == True:
    print ('you may ride. ')

if 'yes' in second.lower() and double == False:
    print('you may not ride ')













