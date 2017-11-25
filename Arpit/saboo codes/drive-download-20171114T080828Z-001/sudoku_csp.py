import copy
def reduce_domain(board,x,y,dom):
    i=x//3
    i*=3
    j=y//3
    j*=3
    v=board[x][y]
    for x1 in range(i,i+3):
        for y1 in range(j,j+3):
            if x1!=x or y1!=y:
                if dom[x1][y1].__contains__(v):
                    dom[x1][y1].remove(v)
    for x1 in range(9):
        if x1!=y:
            if dom[x][x1].__contains__(v):
                dom[x][x1].remove(v)
    for y1 in range(9):
        if y1!=x:
            if dom[y1][y].__contains__(v):
                dom[y1][y].remove(v)


    for i in range(9):
        for j in range(9):
            if len(dom[i][j])==0:
                return False
    return True

def validate(board,dom):
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                reduce_domain(board,i,j,dom)
    for i in range(9):
        for j in range(9):
            if len(dom[i][j])==0:
                return False
    return True
def check(board,x,y,dom):
    i=x//3
    i*=3
    j=y//3
    j*=3
    v=board[x][y]
    for x1 in range(i,i+3):
        for y1 in range(j,j+3):
            if (x1!=x or y1!=y) and board[x1][y1]==board[x][y]:
                return False
    for x1 in range(9):
        if x1!=y and board[x][x1]==board[x][y]:
            return False
    for y1 in range(9):
        if y1!=x and board[y1][y]==board[x][y]:
            return False

    return True
def find_unass(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return [i,j]
    return False
def backtrack(board,dom):
    a=find_unass(board)
    if a==False:
        return True
    i,j=a[0],a[1]
    for k in dom[i][j]:
        board[i][j]=k
        dom1=copy.deepcopy(dom)
        if reduce_domain(board,i,j,dom1):
            if backtrack(board,dom1):
                return True
        board[i][j]=0
    return False

board=[[0 for j in range(9)]for i in range(9)]
dom=[[[j+1 for j in range(9)]for k in range(9)]for i in range(9)]
for i in range(9):
    x=input().split(' ')
    for j in range(9):
        board[i][j]=int(x[j])
if validate(board,dom):
    if backtrack(board,dom):
        print('Solvable',board)
    else:
        print('Not solvable')
else:
    print('Not solvable')

    '''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
    '''