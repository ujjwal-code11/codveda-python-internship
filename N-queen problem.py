def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

def print_board(board, n):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

n = int(input("Enter number of queens: "))
board = [[0]*n for _ in range(n)]

if solve(board, 0, n):
    print("\n✅ Solution Found:\n")
    print_board(board, n)
else:
    print("❌ No solution exists")