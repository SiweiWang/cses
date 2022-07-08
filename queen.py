#! /usr/bin/python3

n = int(input())
res = []
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    board =  [["."] * n for i in range(n)]
    backtrack(board, 0)
    return res

def backtrack(board, row):  
    if (row == len(board)):
        res.append(["".join(row) for row in board])
        return

    n = len(board[row])
    for col in range(n):

        if (not isValid(board, row, col)):
            continue
        board[row][col] = 'Q'
        backtrack(board, row+1)
        board[row][col] ='.'

def isValid(board, row, col):
    n = len(board[row])
    for i in range(len(board)):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n, 1)):

        if board[i][j] =='Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]=='Q':
            return False
    return True

print(solveNQueens(n))


