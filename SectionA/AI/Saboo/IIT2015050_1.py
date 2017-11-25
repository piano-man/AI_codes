import copy
def printboard(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == '0'):
                print('_', end = " ")
            else:
                print(board[i][j], end = " ")
        print()
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
def check(board,x,y):
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
def ac3(board,dom,n,col):
    qu=[]
    for i in range(n):
        for j in range(n):
            if i!=j and i!=col and i!=n and j!=n:
                qu.append([i,j])
   # print(qu)
    while len(qu):
        a=qu[0]
        qu.remove(qu[0])
        i,j=a[0],a[1]
        rem=[]
        #print(i,j,"*******")
        for x in dom[i]:
            if check(board,i,j):
                #print(i,j,x,board)
                rem.append(x)
        for u in rem:
            dom[i].remove(u)
        if len(dom[i])==0:
            return False
        if len(rem)>0:
            for b in range(n):
                if b!=i and qu.__contains__([b,i])==False:
                    qu.append([b,i])
    return True
def AC3(board,dom):
    a=find_unass(board)
    if a==False:
        return True
    i,j=a[0],a[1]
    for k in dom[i][j]:
        #board[i][j]=k
        board1 = copy.deepcopy(board)
        board1[i][j] = k
        dom1=copy.deepcopy(dom)
        if reduce_domain(board1,i,j,dom1):
            if AC3(board1,dom1):
                return True
        #board[i][j]=0
    return False

'''def backtrack(board,dom):
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
'''
def backtrack(board, dom):
    a = find_unass(board)
    if a == False:
        return True
    i, j = a[0], a[1]
    for k in dom[i][j]:
        board[i][j] = k
        if check(board, i, j):
            if(backtrack(board, dom)):
                return True
        board[i][j] = 0
    return False
board=[[0 for j in range(9)]for i in range(9)]
board2=[[0 for j in range(9)]for i in range(9)]
dom=[[[j+1 for j in range(9)]for k in range(9)]for i in range(9)]
for i in range(9):
    x=input().split(' ')
    for j in range(9):
        board[i][j]=int(x[j])
if validate(board,dom):
    if AC3(board,dom):
        print('Solvable-')
        print('Domain-')
        print(dom)
        print()
        print()
        print()
        for i in range(9):
            x=input().split(' ')
            for j in range(9):
                board2[i][j]=int(x[j])
        print()
        print()
        if(backtrack(board2, dom)):
            printboard(board2)
    else:
        print('Not solvable')
else:
    print('Not solvable')


    '''
0 0 0 1 0 0 7 0 2
0 3 0 9 5 0 0 0 0
0 0 1 0 0 2 0 0 3
5 9 0 0 0 0 3 0 1
0 2 0 0 0 0 0 7 0
7 0 3 0 0 0 0 9 8
8 0 0 2 0 0 1 0 0
0 0 0 0 8 5 0 6 0
6 0 5 0 0 9 0 0 0
    '''

    '''
9 5 6 1 3 8 7 4 2 
2 3 7 9 5 4 8 1 6 
4 8 1 6 7 2 9 5 3 
5 9 4 8 6 7 3 2 1 
1 2 8 5 9 3 6 7 4 
7 6 3 4 2 1 5 9 8 
8 7 9 2 4 6 1 3 5 
3 1 2 7 8 5 4 6 9 
6 4 5 3 1 9 2 8 7 
 '''

