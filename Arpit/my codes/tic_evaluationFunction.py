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
    max_counter = 0
    min_counter = 0
    flag1 = 0
    for row in range(3):
        flag1 = 0
        for col in range(3):
            if b[row][col] == 'o':
                flag1 = 1
                break
        if flag1 == 0:
            max_counter += 1
    for col in range(3):
        flag1 = 0
        for row in range(3):
            if b[row][col] == 'o':
                flag1 = 1
                break
        if flag1 == 0:
            max_counter +=1

    flag1 = 0
    for i in range(3):
        if b[i][i] == 'o':
            flag1 = 1
            break
    if flag1 == 0:
        max_counter += 1

    flag1 = 0
    for i in range(3):
        if b[i][2 - i] == 'o':
            flag1 = 1
            break
    if flag1 == 0:
        max_counter += 1

#for min:

    flag1 = 0
    for row in range(3):
        flag1 = 0
        for col in range(3):
            if b[row][col] == 'x':
                flag1 = 1
                break
        if flag1 == 0:
            min_counter +=1
    for col in range(3):
        flag1 = 0
        for row in range(3):
            if b[row][col] == 'x':
                flag1 = 1
                break
    if flag1 == 0:
        min_counter +=1

    flag1 = 0
    for i in range(3):
        if b[i][i] == 'x':
            flag1 = 1
            break
    if flag1 == 0:
        min_counter += 1
    
    flag1 = 0
    for i in range(3):
        if b[i][2 - i] == 'x':
            flag1 = 1
            break
    if flag1 == 0:
        min_counter += 1

    print(max_counter-min_counter, "**")
    return(max_counter - min_counter)


def minimax(board, depth, isMax):
    
    if isMoveLeft(board) == False:
        return 0
    
    if depth == 1:
        val = evaluate(board)
        return val
    
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



def findBestMove(board):
    lst=[]
    bestVal = -1000
    m = move()
    m.row = -1
    m.col = -1
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
                    #print("***")
                    #print(m.row)
                    #print(m.col)
                    #print(bestVal)
    bestVal = -1000
    for i in lst:
        if i[2] > bestVal:
            bestVal = i[2]
    for i in lst:
        if i[2] != bestVal:
            lst.remove(i)
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
m = findBestMove(board)
print(m.row)
print(m.col)
