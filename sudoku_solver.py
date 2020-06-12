board = [
    [1,2,0,6,0,0,4,0,9],
    [0,0,0,0,0,4,1,0,2],
    [0,0,6,0,1,0,5,0,0],
    [6,0,8,1,0,0,0,0,0],
    [0,5,0,3,4,2,0,0,0],
    [4,0,2,0,0,8,0,0,0],
    [8,0,7,0,0,0,3,0,5],
    [3,0,4,0,0,0,0,2,6],
    [0,0,0,4,0,0,0,0,0]
]

def print_sudoku(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print("-------------------------")

        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                print(" |  ", end="")

            if y == 8:
                print(board[x][y])
            else:
                print(str(board[x][y]) + " ", end="")



def find_blank(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x, y)

    return False


def solution_num(board, num, coord):
    for x in range(len(board[0])):
        if board[coord[0]][x] == num and coord[1] != x:
            return False

    for y in range(len(board)):
        if board[y][coord[1]] == num and coord[0] != y:
            return False


    # Check Local Box
    box_x = coord[1] // 3
    box_y = coord[0] // 3

    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):
            if board[x][y] == num and (x, y) != coord:
                return False


    return True


def solve(board):
    if not find_blank(board):
        return True
    else:
        x, y = find_blank(board)

    for i in range(1, 10):
        if solution_num(board, i, (x, y)):
            board[x][y] = i

            if solve(board):
                return True
            else:
                board[x][y] = 0

    return False


print_sudoku(board)
solve(board)

print("")
print("")
print("SOLUTION BELOW:")
print("")

print_sudoku(board)
