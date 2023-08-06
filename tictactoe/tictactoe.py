"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0
    for i in board:
        for j in i:
            x_count += (j == "X")
            o_count += (j == "O")
    return X if x_count == o_count else O


def actions(board):
    action = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                move = (i, j)
                action.append(move)
    return action


def result(board, action):
    board_copy = copy.deepcopy(board)
    user = player(board)
    i, j = action
    if board_copy[i][j] is not None:
        raise Exception("infeasible move")
    board_copy[i][j] = user
    return board_copy


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] is not None:
        return board[2][0]
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    for line in board:
        for cell in line:
            if cell is None:
                return False
    return True


def utility(board):
    a = winner(board)
    if a == "X":
        return 1
    elif a == "O":
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    if player(board) == "X":
        __, action = maxvalue(board)
        return action
    else:
        __, action = minvalue(board)
        return action

def maxvalue(board):
    if terminal(board):
        return utility(board), None
    value = float("-inf")
    step = None
    for action in actions(board):
        v1,__= minvalue(result(board, action))
        if value < v1:
            value = v1
            step = action
    return value, step


def minvalue(board):
    if terminal(board):
        return utility(board), None
    value = float("inf")
    step = None
    for action in actions(board):
        v1,__ = maxvalue(result(board, action))
        if value > v1:
            value = v1
            step = action
    return value, step
