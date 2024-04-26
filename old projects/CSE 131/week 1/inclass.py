from datetime import datetime
import json
current_year = datetime.now().year


def problem_1():
    firstname = input("what is your first name? ")
    lastname = input("what is your last name? ")
    gender = input("what is your gender? (m/f) ")
    if gender == "m":
        title = "mr. "
    else:
        title ="mrs. "
    return (f"{title} {firstname} {lastname}")


def problem_2():
    year_b = int(input("what year were you born?"))
    age = current_year - year_b
    return age

data_dictionary = {
    "numbers": [24, 34, 76, 54, 99, 11, 32, 59, 78, 32],
    "names": ['bob', 'betty', 'james', 'jane', 'billy'],
    "phone numbers" : [2088675309, 4358675309, 8018675309]

}

def write_data_to_file(file_name, data):
    """this function writes the data in the data parameter to a file_name file"""
    try:
        with open(file_name, "wt") as file_handle:
            json_data = json.dumps(data) #3
            file_handle.write(json_data)
    except FileNotFoundError:
        print(f'unable to open the file {file_name}')

def read_data_from_file(file_name):
    """read data from file_name file and return the dictionary"""
    try:
        with open(file_name, "rt") as file_handle:
            json_data = file_handle.read()
            dictionary_data = json.loads(json_data)
        return dictionary_data
    except FileNotFoundError:
        print(f'could not open the file: {file_name}')
        return {}

def sum_of_numbers(data):
    numbers = data
    total = 0
    for number in numbers:
        total += number
    return total

    




def main():
    print (f"{problem_1()}\nyou will turn {problem_2()} years old this year")
    # validate dictionary
    print(data_dictionary['numbers'])
    print(data_dictionary['names'])
    print(data_dictionary['phone numbers'])

    file_name = 'jsonexample.json'
    write_data_to_file(file_name, data_dictionary)

    data = read_data_from_file(file_name)
    print(data['numbers'])
    print(data['names'])
    print(data['phone numbers'])

    total = sum_of_numbers(data['numbers'])
    print(f"the sum of your numbers is {total}")
main()