def demo(a, b=""):# <-- Parameters? (it dont have to have parameters), function signiture
    """
    explain what this does in a single line

    long explination if needed...

    parameters:
    a (string): this is the first positional argument.
    b (string): this is the second positional argument.

    """
    print(a, b)


demo('hello', 'world') #<-- Arguments? (it dont have to have an argument)

#positional arguments
demo('Hello', 'World')


def family(surname, *names):
    for name in names:
        print(f'{name} {surname}')

# [] list <-- array
# () tuple <-- (immutable)
family('Chesley', 'Hayley', 'Bryce', 'Ashlyn', 'Jaydon', 'Avery',)


def person(surname, **names):
    print(f"{names['fname']} {names['mname']} {surname}") #<-- type of quotation marks matter

person('Chesley', fname='Bryce', mname='Aaron')


"""
first day ^ second day v
"""

"""
from datetime import datetime as d1
import datetime as d2
import datetime
today = datetime.now()

print(type(today))
print(type(d1))
print(type(d2))

today = d1.now()
print(today)

print(f"{type(datetime)}")

today = datetime.now()
"""
from datetime import datetime

timestamp = datetime.now()

try:
    file = open('logs.txt', "a")
    file.write(f'{timestamp}\n')
    file.close()
except OSError:
    print('we were unable to append logs.txt')