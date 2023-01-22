from typing import List, Tuple

global board
board = [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]

def get_new_board(): 
    return [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]

def print_board():
    print("")
    for row in board:
        print(row)
    print("")
    pass

def get_input() -> Tuple[int, int]:
    valid = False
    while not valid:
        coordinates_string = input(
            "Enter a row and a column, separate with space: ")
        valid, res = validate_input(coordinates_string)
    return res

def validate_input(string: str) -> Tuple[bool, Tuple[int, int]]:
    string = string.strip()
    split_string: List[str] = string.split(" ")
    if len(split_string) < 2:
        print("Wrong input")
        return (False, None)
    if not str.isdigit(split_string[0]) or not str.isdigit(split_string[1]):
        print("Wrong input")
        return (False, None)

    row: int = int(split_string[0])
    col: int = int(split_string[1])
    
    if not 1 <= row <= 3 or not 1 <= col <= 3:
        print("Wrong input")
        return (False, None)

    if board[row - 1][col - 1] != "#":
        print("Wrong input")
        return (False, None)

    return (True, (row - 1, col - 1))

def update_board(row: int, col: int, marker: str):
    board[row][col] = marker

def check_winner() -> bool:
    for row in board:
        row_set = set(row)
        if len(row_set) == 1 and row_set.pop() != "#":
            return True

    for i in range(2):
        col_set = {board[0][i], board[1][i], board[2][i]}
        if len(col_set) == 1 and col_set.pop() != "#":
            return True

    across_set1 = {board[0][0], board[1][1], board[2][2]}
    if len(across_set1) == 1 and across_set1.pop() != "#":
        return True
    across_set2 = {board[0][2], board[1][1], board[2][0]}
    if len(across_set2) == 1 and across_set2.pop() != "#":
        return True

    return False

def check_tie() -> bool:
    for i in range(2):
        for j in range(2):
            if board[i][j] == "#":
                return False

    return True

def resetBoard():
    board = get_new_board()

def main():
    marker = "X"
    winner = False
    while not winner or tie:
        marker = "O" if marker == "X" else "X"
        print_board()
        row, col = get_input()
        update_board(row, col, marker)
        winner = check_winner()
        tie = check_tie()

    if winner == True:
        print(f"Winner is {marker}")
        resetBoard()

    if tie == True:
        print("The game was a tie!")
        resetBoard()
    
    print_board()
    

main()