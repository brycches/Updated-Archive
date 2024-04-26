from array import array


letters = ["G", "J", "A", "K", "Z"]  # <- list (for loops)
letters = ("G", "J", "A", "K", "Z")  # <- tupple

letters = [] #while loops


while len(letters) < 5:
    letter = input("please give me a favorite letter of yours: ").upper()
    letters.append(letter)

numbers = []

while len(numbers) < 5:
    num = input("please give me a favorite number of yours: ")
    try:
        num = int(num)
    except:
        print("please enter a whole number!")
        continue
    numbers.append(num)


numbers_a = array("i") # this forces the input to be an intager

while len(numbers_a) < 5:
    num = int(input("please give me a favorite number of yours: "))
    # if len(numbers) % 2 == 0: # <- this stuff will crash it
    #     num = int(num)
    # else:
    #     num = float(num)
    numbers_a.append(num)


# for letter in letters
    # print("letter")

#
# for i in range(len(letters)):
#     print (f" {i+1}) {letters[i]}")

# more effecient V less efficient ^

for i, letter in enumerate(letters):
    print (f" {i + 1}) {letter}")

for i, number in enumerate(numbers):
    print (f" {i +1}) {number}")

print(numbers_a)


with open() as file:
    for line in file:
        print(line)
