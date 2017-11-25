def isLeft(board):
	for i in range(3):
		for j in range(3):
			if (board[i][j] == '_'):
				return True
	return False

def evaluate(board):
	for row in range(3):
		if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
			if (board[row][0] == 'X'):
				return 10
			elif (board[row][0] == '0'):
				return -10;
	for col in range(3):
		if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
			if (board[0][col] == 'X'):
				return 10
			elif(board[0][col] == '0'):
				return -10
	if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
		if (board[0][0] == 'X'):
			return 10
		elif(board[0][0] == '0'):
			return -10
	if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
		if (board[0][2] == 'X'):
			return 10
		elif(board[0][2] == '0'):
			return -10
	return 0

def minmax(board, depth, isMax, alpha, beta):
	score = evaluate(board)

	if (score == 10):
		return score
	if (score == -10):
		return score
	if (isLeft(board) == False):
		return 0
	if (isMax == True):
		best = -1000
		for i in range(3):
			for j in range(3):
				if (board[i][j] == '_'):
					board[i][j] = 'X'
					best = max(best, minmax(board,depth+1,False, alpha, beta))
					board[i][j] = '_'
					if (beta <= best):
						return best
					alpha = max(alpha,best)
		return best
	else :
		best = 1000
		for i in range(3):
			for j in range(3):
				if (board[i][j] == '_'):
					board[i][j] = '0'
					best = min(best, minmax(board,depth+1,True, alpha, beta))
					board[i][j] = '_'
					if (best <= alpha):
						return best
					beta = min(beta, best)
		return best



def findbestmove(board, player):
	if (player == 'X'):
		bestval = -1000
	else :
		bestval = 1000
	Brow = -1
	Bcol = -1
	for i in range(3):
		for j in range(3):
			if (board[i][j] == '_'):
				print("Loop")
				board[i][j] = player
				if (player == 'X'):
					moveVal = minmax(board, 0 , False, -1000, 1000)
				else:
					moveVal = minmax(board, 0, True, -1000, 1000)
				board[i][j] = '_'
				print("MoveVal: ", moveVal)
				if (player == 'X'):
					if (moveVal > bestval):
						bestval = moveVal
						Brow = i
						Bcol = j
				else:
					if (moveVal < bestval):
						bestval = moveVal
						Brow = i
						Bcol = j
	print("Best")
	print(Brow, Bcol)
	if (Brow != -1):
		board[Brow][Bcol] = player
		for row in (board):
			print(row)

player = input()
board = []
print(player)
for i in range(3):
	temp = []
	for j in range(3):
		k = input()
		temp.append(k)
	board.append(temp)
for row in (board):
	print(row)
minx = -1000
maxx = 1000
findbestmove(board,player)