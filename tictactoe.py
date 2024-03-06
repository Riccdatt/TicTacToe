"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX=0
    numO=0

    for i in range (3):
        for j in range (3):
            if board[i][j]==X:
                numX+=1
            if board[i][j]==O:
                numO+=1
    if numX > numO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range (3):
        for j in range (3):
            if board[i][j]==EMPTY:
                actionsSet.add((i,j))
    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    
    boardCopy = copy.deepcopy(board)
    sign=player(board)
    boardCopy[action[0]][action[1]]=sign
    return boardCopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[0][1] == board[0][2]) or (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
    if (board[1][0] == board[1][1] == board[1][2]) or (board[0][1] == board[1][1] == board[2][1]) or (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
        return board[1][1]
    if (board[2][0] == board[2][1] == board[2][2]) or (board[0][2] == board[1][2] == board[2][2]):
        return board[2][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    count=0
    for i in range (3):
        for j in range (3):
            if board[i][j] != EMPTY:
                count += 1
    if count == 9:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    if winner(board)==O:
        return -1
    return 0
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    currentPlayer = player(board)
    bestMove = None

    if currentPlayer == O:
        currentMin=2
        for action in actions(board):
            currentResult=result(board,action)
            mV=maxValue(currentResult)
            if mV < currentMin:
                bestMove = action
                currentMin = mV
    
    if currentPlayer == X:
        currentMax=-2
        for action in actions(board):
            currentResult=result(board,action)
            mV=minValue(currentResult)
            if mV > currentMax:
                bestMove = action
                currentMax = mV

    return bestMove
        
def maxValue (board):
    if terminal(board):
        return utility(board)
    val=-2
    for action in actions(board):
        val=max(val,minValue(result(board,action)))
    return val

def minValue (board):
    if terminal(board):
        return utility(board)
    val=2
    for action in actions(board):
        val=min(val,maxValue(result(board,action)))
    return val