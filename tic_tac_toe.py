
def print_board(board):
    """
    Prints the game board. 
    Board is a list of length 9. 
    The entries in board can only be " ", "X" or "O".
    """
    
    border = "-"*9

    line_1 = f"| {board[0]} {board[1]} {board[2]} |"
    line_2 = f"| {board[3]} {board[4]} {board[5]} |"
    line_3 = f"| {board[6]} {board[7]} {board[8]} |"

    print(border)
    print(line_1)
    print(line_2)
    print(line_3)
    print(border)


def check_three_in_row(marker,board):
    """
    Returns True, if there are three in a row for a given marker.
    
    The form of the board is:
        0 1 2
        3 4 5
        6 7 8
    """

    # Check the first row
    if (board[0] == marker) and (board[1] == marker) and (board[2] == marker):
        return True
    # Check the second row
    elif (board[3] == marker) and (board[4] == marker) and (board[5] == marker):
        return True
    # Check the third row
    elif (board[6] == marker) and (board[7] == marker) and (board[8] == marker):
        return True
    # Check the first column
    elif (board[0] == marker) and (board[3] == marker) and (board[6] == marker):
        return True
    # Check the second column
    elif (board[1] == marker) and (board[4] == marker) and (board[7] == marker):
        return True
    # Check the third column
    elif (board[2] == marker) and (board[5] == marker) and (board[8] == marker):
        return True
    # Check acros from top left corner to lower right corner
    elif (board[0] == marker) and (board[4] == marker) and (board[8] == marker):
        return True
    # Check acros from top right corner to lower left corner
    elif (board[2] == marker) and (board[4] == marker) and (board[6] == marker):
        return True
    else:
        return False



def index_of_move(move):
    """
    Returns the index of the board-list that corresponds to the space the player 
    wants to move his marker to.

    The posible spaces on the board are positioned like this:
        (1 3)   (2 3)   (3 3)
        (1 2)   (2 2)   (3 2)
        (1 1)   (2 1)   (3 1)
    Note that it is similar to xy-coordinates.

    """

    if move == "1 3":
        index = 0
    elif move == "2 3":
        index = 1
    elif move == "3 3":
        index = 2
    elif move == "1 2":
        index = 3
    elif move == "2 2":
        index = 4
    elif move == "3 2":
        index = 5
    elif move == "1 1":
        index = 6
    elif move == "2 1":
        index = 7
    elif move == "3 1":
        index = 8
    return index

def occupied(move, board):
    """Checks whether a space is already occupied."""
    index = index_of_move(move)
    return board[index] == "X" or board[index] == "O"


def out_of_range(move):
    """
    Checks whether the user typed a number different from 1, 2 or 3.
    Note: assumes that the move is not invalid.
    """

    # First we convert the string to a list.
    move_as_list = move.split(" ")

    # Then we convert the entries of the list to integers and checks that they
    # are not greater than 3 or smaller than 1.
    if int(move_as_list[0]) > 3 or int(move_as_list[0]) < 1:
        return True
    elif int(move_as_list[1]) > 3 or int(move_as_list[1]) < 1:
        return True
    else:
        return False


def invalid(move):
    """Checks that move consists of two integers seperated by a single space."""

    # First we convert the string to a list.
    move_as_list = move.split(" ")
    
    # If the list doesn't contain exactly two entries the move is invalid.
    if len(move_as_list) != 2:
        return True

    # If the entries of the list cannot be converted to integers then the
    # move is invalid.
    try:
        col = int(move_as_list[0])
        row = int(move_as_list[1])
        return False

    except ValueError:
        return True

def take_turn(board, marker):
    """
    Prompts the user to input a move until the move is valid.
    Updates the board and prints the new board.
    """
    running = True

    while running:

        move = input("Enter the coordinates: ")

        if invalid(move):
            print("You should enter two numbers seperated by a single space!")
        elif out_of_range(move):
            print("Coordinates should be from 1 to 3.")
        elif occupied(move, board):
            print("This cell is occupied! Choose another one!")
        else:
            update_board(move, board, marker)
            print_board(board)
            running = False


def update_board(move, board, marker):
    """Updates the board with the new move with the given marker."""
    index = index_of_move(move)
    board[index] = marker


# The starting board without any markers
board = [" "]*9

# Number of moves is used to determine whether it's X or Os turn
number_of_moves = 0

# We start the game by printing the empty board    
print_board(board)


running = True

while running:

    if check_three_in_row("X", board):
        print("X wins")
        running = False
    elif check_three_in_row("O", board):
        print("O wins")
        running = False
    elif " " not in board: # No more empty spaces on board
        print("Draw")
        running = False
    else:
        # Alternate between X and O taking a turn. X starts.
        if number_of_moves % 2 == 0:
            take_turn(board,"X")
            number_of_moves += 1
        else:
            take_turn(board, "O")
            number_of_moves += 1
