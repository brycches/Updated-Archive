# 1. Name:
#      Bryce Chesley
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was probably just shaking off the cobwebs and
#      sitting down to code the program. getting the motivation and losing the brain 
#      fog enough to actually make it work
# 5. How long did it take for you to complete the assignment?
#      around 5 hours

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '
board = []
# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    try:
        with open(filename, "rt") as file_handle:
            json_data = file_handle.read()

            saved_board = json.loads(json_data)

        if saved_board != blank_board:

            return saved_board['board']
        else:
            return blank_board['board']
    except FileNotFoundError:
        print(f'could not open the file: {filename}')
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    save = input("would you like to save the game before you leave? y/n ")
    if save == 'y':
        to_save_board = {'board': board}
        try:
            with open(filename, "wt") as file_handle:
                json_data = json.dumps(to_save_board) #3
                file_handle.write(json_data)
                return
        except FileNotFoundError:
            print(f'unable to open the file {filename}')
            return
    else:
        to_save_board = blank_board
        try:
            with open(filename, "wt") as file_handle:
                json_data = json.dumps(to_save_board) #3
                file_handle.write(json_data)
                return
        except FileNotFoundError:
            print(f'unable to open the file {filename}')
            return
        # Put file writing code here.

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f"""
 {board[0]} | {board[1]} | {board[2]} 
---+---+---
 {board[3]} | {board[4]} | {board[5]} 
---+---+---
 {board[6]} | {board[7]} | {board[8]} 

""")
    # Put display code here.

def is_x_turn(board):
    '''Determine whose turn it is.'''
    square_X = 0
    square_O = 0
    for square in board:
        if square == X:
            square_X += 1
        elif square == O:
            square_O += 1
    if square_O == square_X:
        return False
    else:
        return True
        # Put code here determining if it is X's turn.

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    desired_square = input(f"which numbered space would you like to move? ")
    if desired_square == 'q':
        return False
    else:
        desired_square = int(desired_square)

    if board[desired_square-1]== BLANK:
        if is_x_turn(board):
            board[desired_square-1]= X
        else:
            board[desired_square-1]= O
        return True
    else:
        print("someone has already moved in that square")
        return True

    
    # Put game play code here. Return False when the user has indicated they are done.
    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")


# The file read code, game loop code, and file close code goes here.



def main ():
    use_save = input('would you like to use your saved board? y/n ')
    print("The current board is:")
    if use_save == 'y':
        board = read_board('saved_board.json')
    else:
        board = blank_board['board']
    
    done = True
    while done != False:
        display_board(board)
        done = play_game(board)
        if done == False:
            save_board('saved_board.json', board)
        
        if game_done(board) == True:
            display_board(board)
            game_done(board, message=True)
            again = ""
            again = input('would you like to play again? y/n ')
            
            if again == 'y':
                board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                done = True
                
            else:
                done = False
        

main()