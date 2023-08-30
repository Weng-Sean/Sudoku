import random
import time

board = [
    [0, 0, 3, 0, 0, 9, 0, 6, 1],
    [0, 0, 0, 0, 2, 3, 0, 0, 0],
    [2, 5, 0, 0, 1, 0, 0, 7, 0],
    [0, 0, 2, 0, 3, 0, 0, 0, 6],
    [0, 9, 0, 0, 0, 1, 0, 0, 5],
    [0, 0, 0, 6, 5, 0, 3, 0, 2],
    [0, 0, 0, 8, 0, 0, 4, 0, 0],
    [0, 2, 1, 0, 0, 6, 0, 0, 0],
    [8, 7, 0, 0, 0, 0, 2, 9, 0]

]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print('----------------------')
        for j in range(len(board[i])):
            if j != 8:
                if j % 3 == 2:
                    print(board[i][j], end=' | ')
                else:
                    print(board[i][j], end=' ')
            else:
                print(board[i][j])

        if i == 8:
            print('----------------------')


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)

    return False


def is_valid(board, value, position):
    for i in range(9):
        if board[position[0]][i] == value and i != position[1]:
            return False

    for i in range(9):
        if board[i][position[1]] == value and i != position[0]:
            return False

    box_y = position[0] // 3
    box_x = position[1] // 3

    for i in range((box_x) * 3, (box_x) * 3 + 3):
        for j in range((box_y) * 3, (box_y) * 3 + 3):
            if board[j][i] == value and position != (j, i):
                return False

    return True


def solved(board):
    if not find_empty(board):
        return True
    else:
        r, c = find_empty(board)
        for i in range(1, 10):
            if is_valid(board, i, (r, c)):
                board[r][c] = i
                if solved(board):
                    return True
                board[r][c] = 0
    return False


def random_sudoku(level = 200):
    board = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row.append(0)
        board.append(new_row)


    for i in range(level):
        a = random.randint(0, 8)
        b = random.randint(0, 8)
        c = random.randint(1, 9)
        board[a][b] = c
        if not is_valid(board, c, (a, b)):
            board[a][b] = 0

    return board


def random_game():
    board = random_sudoku()
    print_board(board)
    count = 1
    while not solved(board):
        print(
            f"The sudoku computer generated is not solvable, hold down while computer generate another one... #{count}")
        count += 1
        board = random_sudoku()
        print_board(board)
        print(board)
        b = time.time()
    user_input = input("Type answer for solution: ")
    if user_input == "answer":
        print_board(board)


if __name__ == '__main__':
    a = time.time()
    random_game()
    #print_board(board)
    #print(solved(board))
    #print_board(board)

    b = time.time()
    print('total time', b - a)
