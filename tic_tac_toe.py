
def print_board(board):
    """Prints the game board given a list of game markers"""
    
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

def make_move(move, board, marker):
    """Makes """
    index = index_of_move(move)
    board[index] = marker


board = [" "]*9

number_of_moves = 0

running = True
    
print_board(board)

while running:

    if check_three_in_row("X", board):
        print("X wins")
        running = False
    elif check_three_in_row("O", board):
        print("O wins")
        running = False
    elif " " not in board:
        print("Draw")
        running = False
    else:
        
        if number_of_moves % 2 == 0:
            marker = "X"
            making_move = True

            while making_move:

                move = input("Enter the coordinates: ")

                if invalid(move):
                    print("You should enter numbers!")
                elif out_of_range(move):
                    print("Coordinates should be from 1 to 3!")
                elif occupied(move, board):
                    print("This cell is occupied! Choose another one!")
                else:
                    make_move(move, board, marker)
                    print_board(board)
                    making_move = False

            number_of_moves += 1

        else:
            marker = "O"
            making_move = True

            while making_move:

                move = input("Enter the coordinates: ")

                if invalid(move):
                    print("You should enter numbers!")
                elif out_of_range(move):
                    print("Coordinates should be from 1 to 3!")
                elif occupied(move, board):
                    print("This cell is occupied! Choose another one!")
                else:
                    make_move(move, board, marker)
                    print_board(board)
                    making_move = False

            number_of_moves += 1
