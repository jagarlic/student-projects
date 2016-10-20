# import gamePlay
# from copy import deepcopy

DEPTH = 6

def alphaBeta(board, color, depth = DEPTH, isMax = True, alpha = float('-inf'), beta = float('inf')):
	if depth == 0:
		return [value(board, color), (0,0)]
	if isMax:
		bestValue = float('-inf')
	else:
		bestValue = float('inf')
	bestMove = "pass"
	for i in range(len(board)):
		for j in range(len(board[0])):
			if gamePlay.valid(board, color, (i,j)):
				newBoard = deepcopy(board)
				gamePlay.doMove(newBoard, color, (i,j))
				currValue = alphaBeta(newBoard, color, depth-1, not isMax, alpha, beta)[0]
				if (isMax):
					if currValue >= bestValue:
						bestValue = currValue
						bestMove = (i,j)
					if bestValue > alpha:
						alpha = bestValue
					if (beta < alpha):
						return bestValue, bestMove
				else:
					if currValue <= bestValue:
						bestValue = currValue
						bestMove = (i,j)
					if bestValue < beta:
						beta = bestValue
					if (beta < alpha):
						return bestValue, bestMove
	return bestValue, bestMove

def nextMove(board, color):
	return alphaBeta(board, color)[1]

def value(board, color):
	value = 0
	if color == "W":
		for row in board:
			for e in row:
				if e == "W":
					value+=1
				elif e == "B":
					value-=1
	else:
		for row in board:
			for e in row:
				if e == "B":
					value+=1
				elif e == "W":
					value-=1
	return value
