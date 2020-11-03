import random


# The board is a 2 dimensional list,
# When every list inside the containing list, is a line in the sudoku
# If it were 2x2 [[1,2],
# [2,1]]

def is_soduku_rows_valid(board):
    for row in board:
        lst = [i for i in range(1, 10)]
        for number in row:
            if number in lst:
                lst.remove(number)
        if len(lst) != 0:
            return False
    return True


def is_soduku_columns_valid(board):
    for i in range(0, len(board)):
        lst = [i for i in range(1, 10)]
        for j in range(0, 9):
            if board[j][i] in lst:
                lst.remove(board[j][i])
        if len(lst) != 0:
            return False
    return True


def is_sudoku_boxes_valid(board):
    # Should be checking code
    return True


def is_sudoku_valid(board):
    if not is_soduku_columns_valid(board):
        return False
    if not is_soduku_rows_valid(board):
        return False
    if not is_sudoku_boxes_valid(board):
        return False
    return True


def create_random_sudoku_board():
    board = []
    for j in range(9):
        row = []
        numbers = [i for i in range(1, 10)]
        for i in range(9):
            index_to_take = random.randint(0, len(numbers) - 1)
            row.append(numbers[index_to_take])
            del numbers[index_to_take]
        board.append(row)
    return board


def create_sudoku_board():
    board = create_random_sudoku_board()
    while not is_sudoku_valid(board):
        board = create_random_sudoku_board()
    return board


if __name__ == '__main__':
    print(create_sudoku_board())
