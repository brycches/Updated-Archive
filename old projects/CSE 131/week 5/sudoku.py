# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      play a legal game of sudoku
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was a bit rough for me, mostly in the length of time it took to make.
#      There was a lot of error handling that had to happen, and I couldn't figure out how
#      to properly look in my main function without using continue. there was a lot of trouble
#      with my possible manipulations function, as it involved imbedded for loops, and loops that
#      kept going past the desired range giving me errors like 4j doesn't exist. it was also
#      challenging to save the board back to the json, as I was storing it throughout my program as
#      a dictionary for easier referencing.
# 5. How long did it take for you to complete the assignment?
#      9 hours

import json
board = {}

def get_file_name():
    done = False
    while done != True:
        try:
            filename = input("What is the name of your file? ")
            with open(filename, mode="r") as json_file:
                data = json.load(json_file)
            done = True
            return filename
        except FileNotFoundError:
            print("File not found, please check your file name. ")
            return 'error'

def get_desired_location():
    try:
        while True:
            location = input("Enter a location (e.g., 3b), or 'q' to quit: ").lower()
            try:
                int(location[1])
                first = location[0]
                second = location[1]
                location = second + first
            except:
                pass
            if location == 'q':
                return 'error'
            if location in board:
                return location
            else:
                print("Your inputed location is not a valid location. Please enter a valid location (e.g., 3b).")
    except:
        return 'error'


def get_desired_manipulation():
    try:
        manipulation = input("what is your desired manipulation to the chosen grid square? (or type s for all possible manipulations) ")
        if manipulation.lower() == 's':
            return manipulation.lower()
        else:
            manipulation = int(manipulation)
            if manipulation < 1:
                raise ValueError()
            if manipulation > 9:
                raise ValueError()
            
            assert 0 <= manipulation <= 9
            return manipulation

    except AssertionError:
        print("assertion error")
        return 'error'
    except:
        print('\nThere was an error with your desired manipulation. Make sure you are inputing a whole number from 1 to 9. ')
        return 'error'



def create_board_from_file(filename):
    done = False
    while done != True:
        try:
            with open(filename, mode="r") as json_file:
                data = json.load(json_file)
            for i, row in enumerate(data["board"]):
                for j, value in enumerate(row):
                    # Create the key in the format "1a", "1b", "1c", ...
                    key = f"{i+1}{chr(97+j)}"
                    board[key] = value
            done = True
            return board


        except:
            print("\nThere was an error, please check your file name. ")

def save_board(filename):
    try:
        save = input('Would you like to save? y/n ')
        if save.lower() == 'y':
            board_list = []
            for row in range(1, 10):
                board_row = [board[f"{row}{col}"] for col in "abcdefghi"]
                board_list.append(board_row)
            data = {"board": board_list}
            with open(filename, mode="w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Board saved to {filename}")
            return
        else:
            print("You didn't save your board")
            return
    except Exception as e:
        print(f"An error occurred while saving the board: {e}")
        return




def manipulation(board, desired_manipulation, desired_location,):

    possible = possible_manipulations(desired_manipulation, desired_location, board)
    original_board = board
    if desired_manipulation == 's':
        display_board(possible, 3)
        board = original_board
    elif possible == True:
        new_board = update_board(desired_location, desired_manipulation)
        new = 1
        display_board(new_board, new)
    elif possible == False:
        return 'error'
    else:
        return 'error'
    return board
    
    

def possible_manipulations(desired_manipulation, desired_location, current_board):
    Squares = {
        1: ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c'],
        2: ['4a', '4b', '4c', '5a', '5b', '5c', '6a', '6b', '6c'],
        3: ['7a', '7b', '7c', '8a', '8b', '8c', '9a', '9b', '9c'],
        4: ['1d', '1e', '1f', '2d', '2e', '2f', '3d', '3e', '3f'],
        5: ['4d', '4e', '4f', '5d', '5e', '5f', '6d', '6e', '6f'],
        6: ['7d', '7e', '7f', '8d', '8e', '8f', '9d', '9e', '9f'],
        7: ['1g', '1h', '1i', '2g', '2h', '2i', '3g', '3h', '3i'],
        8: ['4g', '4h', '4i', '5g', '5h', '5i', '6g', '6h', '6i'],
        9: ['7g', '7h', '7i', '8g', '8h', '8i', '9g', '9h', '9i'],
    }

    row, column = int(desired_location[0]), desired_location[1]

    used_numbers = set()

    for i in range(1, 9):
        used_row = str((row + i - 1) % 9 + 1)
        if used_row != str(row):
            used_numbers.add(current_board[f"{used_row}{column}"])
        used_column = chr(ord(column) + i - 1)
        if 'a' <= used_column <= 'i':
            used_numbers.add(current_board[f"{row}{used_column}"])

    for square in Squares:
        if desired_location in Squares[square]:
            for item in Squares[square]:
                used_numbers.add(current_board[item])

    if desired_manipulation == "s":
        possible_numbers = set(range(1, 9)) - used_numbers
        return sorted(possible_numbers)
    elif int(desired_manipulation) in used_numbers:
        print("That number is already in use in your column, row or square.")
        return False
    else:
        print("That number can be placed in the desired location.")
        return True



def update_board(desired_location, desired_manipulation):

    if board[desired_location] == 0:
        board[desired_location] = desired_manipulation
        return board
    else:
        try:
            update = input('Do you want to overwrite the number that is already in that position? (y/n): ')
            if update.lower() == 'y':
                board[desired_location] = desired_manipulation
                return board
            elif update.lower() == 'n':
                return board
            else:
                print('Invalid input. Please enter "y" to overwrite or "n" to cancel.')
                return board
        except:
            print('An error occurred while updating the board. Please try again.')
            return board


def display_board(board, new):
    if new == 1:
        print("This is your new board:")
        print_board(board)
    elif new == 0:
        print("Your current board looks like this:")
        print_board(board)
    elif new == 3:
        print("The possible manipulations are:")
        print(board)
    else:
        return 'error'

def print_board(board):
    horizontal_line = "+----+----+----+----+----+----+"
    vertical_line = "|"
    for row in range(1, 10):
        if row in [4, 7]:
            print(horizontal_line)
        for col in "abcdefghi":
            value = board[f"{row}{col}"]
            if col in "cfi":
                vertical_line += f" {value} |"
            else:
                vertical_line += f" {value} "
        print(vertical_line)
        vertical_line = "|"


def main():
    file_name = get_file_name()
    if file_name == 'error':
        print('Exiting the game.')
        return
    board = create_board_from_file(file_name)
    display_board(board, 0)
    while True:
        original_board = board
        desired_location = get_desired_location()
        if desired_location == 'error':
            cont = input('Are you sure you would like to quit? y/n ')
            if cont.lower() == 'y':
                save_board(file_name)
                print('Exiting the game.')
                return
            board = original_board
            continue
        desired_manipulation = get_desired_manipulation()
        if desired_manipulation == 'error':
            cont = input('would you like to quit or continue playing? (type q to quit) ')
            if cont.lower() == 'q':
                print('Exiting the game.')
                return
            board = original_board
            continue
            
        result = manipulation(board, desired_manipulation, desired_location)
        if result == 'error':
            cont = input('would you like to quit or continue playing? (type q to quit) ')
            if cont.lower() == 'q':
                print('Exiting the game.')
                return
            board = original_board
            continue
        else:
            board = result



if __name__ == "__main__":
    main()