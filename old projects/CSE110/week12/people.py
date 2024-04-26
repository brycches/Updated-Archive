people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

oldest_age = 0
oldest_name = ''

for line in people:
    parts = line.split(' ')
    name = parts[0]
    age = int(parts[1])

    if age > oldest_age:
        oldest_age = age
        oldest_name = name

print(f'The oldest person is {oldest_name}: {oldest_age}')