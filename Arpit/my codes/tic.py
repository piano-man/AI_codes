class move:
    def __inti__(self):
        self.row
        self.col


def isMoveLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                return True
    return False

def evaluate(b):
    for row in range(3):
        if b[row][0]==b[row][1] and b[row][1]==b[row][2]:
            if b[row][0] == 'x':
                return 10
            elif b[row][0] == 'o':
                return -10

    for col in range(3):
        if b[0][col]==b[1][col] and b[1][col]==b[2][col]:
            if b[0][col] == 'x':
                return 10
            elif b[0][col] == 'o':
                return -10

    if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
        if b[0][0] == 'x':
            return 10
        elif b[0][0] == 'o':
            return -10

    if b[0][2]==b[1][1] and b[1][1]==b[2][0]:
        if b[2][0] == 'x':
            return 10
        elif b[2][0] == 'o':
            return -10
    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return (score)
    
    if score == -10:
        return (score)

    if isMoveLeft(board) == False:
        return 0

    if isMax == True:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'x'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = '_'
        return best
                               
    if isMax == False:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = '_'
        return best
                            


def findBestMove(board, player):
    lst=[]
    bestVal = -1000
    m = move()
    m.row = -1
    m.col = -1
    if player == 'x':
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'x'
                    moveVal = minimax(board, 0, False)
                    board[i][j] = '_'
                    if moveVal >= bestVal:
                        lst.append([i,j,moveVal])
                        m.row = i
                        m.col = j
                        bestVal = moveVal

        bestVal = -1000
        print(lst)
        for i in lst:
            if i[2] > bestVal:
                bestVal = i[2]
        tmp=[]
        for i in lst:
            #print(i,"*****")
            if i[2] != bestVal:
                tmp.append(i)
        for u in tmp:
            lst.remove(u)
        print(lst)
        return m
    else:
        bestVal = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    moveVal = minimax(board, 0, True)
                    board[i][j] = '_'
                    if moveVal <= bestVal:
                        lst.append([i,j,moveVal])
                        m.row = i
                        m.col = j
                        bestVal = moveVal
    
        bestVal = 1000
        print(lst)
        for i in lst:
            if i[2] < bestVal:
                bestVal = i[2]
        tmp=[]
        for i in lst:
            #print(i,"*****")
            if i[2] != bestVal:
                tmp.append(i)
        for u in tmp:
            lst.remove(u)
        print(lst)
        return m



player = raw_input()
board = [[] for i in range(3)]
for i in range(3):
    x = raw_input().split(' ')
    board[i].append(x[0])
    board[i].append(x[1])
    board[i].append(x[2])
print(board)
m = findBestMove(board, player)
print(m.row)
print(m.col)
