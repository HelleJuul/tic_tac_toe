board = input("Enter cells: ")

board_as_list = list(board)

def print_board(board_as_list):
    """Prints the game board given a list of game markers"""
    
    for pos, cell in enumerate(board_as_list):
        if cell == "_":
            board_as_list[pos] = " " 

    border = "-"*9

    line_1 = f"| {board_as_list[0]} {board_as_list[1]} {board_as_list[2]} |"
    line_2 = f"| {board_as_list[3]} {board_as_list[4]} {board_as_list[5]} |"
    line_3 = f"| {board_as_list[6]} {board_as_list[7]} {board_as_list[8]} |"

    print(border)
    print(line_1)
    print(line_2)
    print(line_3)
    print(border)


def check_three_in_row(marker,board_as_list):
    """Checks if there are three in a row."""

    # Check the first row
    if (board_as_list[0] == marker) and (board_as_list[1] == marker) and (board_as_list[2] == marker):
        return True
    # Check the second row
    elif (board_as_list[3] == marker) and (board_as_list[4] == marker) and (board_as_list[5] == marker):
        return True
    # Check the third row
    elif (board_as_list[6] == marker) and (board_as_list[7] == marker) and (board_as_list[8] == marker):
        return True
    # Check the first column
    elif (board_as_list[0] == marker) and (board_as_list[3] == marker) and (board_as_list[6] == marker):
        return True
    # Check the second column
    elif (board_as_list[1] == marker) and (board_as_list[4] == marker) and (board_as_list[7] == marker):
        return True
    # Check the third column
    elif (board_as_list[2] == marker) and (board_as_list[5] == marker) and (board_as_list[8] == marker):
        return True
    # Check acros from top left corner to lower right corner
    elif (board_as_list[0] == marker) and (board_as_list[4] == marker) and (board_as_list[8] == marker):
        return True
    # Check acros from top right corner to lower left corner
    elif (board_as_list[2] == marker) and (board_as_list[4] == marker) and (board_as_list[6] == marker):
        return True
    else:
        return False

def print_status(board_as_list):
    if check_three_in_row("X", board_as_list) and check_three_in_row("O", board_as_list):
        print("Impossible")

    elif ((board_as_list.count("X") - board_as_list.count("O")) >= 2) or ((board_as_list.count("X") - board_as_list.count("O")) <= -2):
        print("Impossible")

    elif check_three_in_row("X", board_as_list):
        print("X wins")

    elif check_three_in_row("O", board_as_list):
        print("O wins")

    elif "_" in board_as_list:
        print("Game not finished")

    else:
        print("Draw")


def index_of_move(move):
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

def occupied(move, board_as_list):
    index = index_of_move(move)
    if board_as_list[index] == "X" or board_as_list[index] == "O":
        return True
    else:
        return False

def out_of_range(move):
    move_as_list = move.split(" ")
    if int(move_as_list[0]) > 3 or int(move_as_list[0]) < 1:
        return True
    elif int(move_as_list[1]) > 3 or int(move_as_list[1]) < 1:
        return True
    else:
        return False

def invalid(move):
    move_as_list = move.split(" ")

    try:
        col = int(move_as_list[0])
        row = int(move_as_list[1])
        return False

    except ValueError:
        return True

def make_move(move, board_as_list):
    """Changes the board."""
    index = index_of_move(move)
    board_as_list[index] = "X"



running = True

print_board(board_as_list)

while running:

    move = input("Enter the coordinates: ")

    if invalid(move):
        print("You should enter numbers!")
    elif out_of_range(move):
        print("Coordinates should be from 1 to 3!")
    elif occupied(move, board_as_list):
        print("This cell is occupied! Choose another one!")
    else:
        make_move(move, board_as_list)
        print_board(board_as_list)
        running = False


