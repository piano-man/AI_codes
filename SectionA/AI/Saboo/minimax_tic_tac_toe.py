import copy
def terminal_state(board,maxp):
    for j in range(3):
        c = 0
        d = 0
        for i in range(3):
            if board[j][i]=='X':
                c=c+1
            elif board[j][i]=='O':
                d=d+1
            if (c==3 and maxp==1) or (d==3 and maxp==0):
                return 1
            elif (c==3 and maxp==0) or (d==3 and maxp==1):
                return -1

    for i in range(3):
        c = 0
        d = 0
        for j in range(3):
            if board[j][i]=='X':
                c=c+1
            elif board[j][i]=='O':
                d=d+1
            if (c==3 and maxp==1) or (d==3 and maxp==0):
                return 1
            elif (c==3 and maxp==0) or (d==3 and maxp==1):
                return -1

    if (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X' and maxp==1) or (board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O' and maxp==0):
        return 1
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' and maxp == 0) or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' and maxp == 1):
            return -1
    if (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X' and maxp==1) or (board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O' and maxp==0):
        return 1
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' and maxp == 0) or (board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0' and maxp == 1):
            return -1
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                return 2
    return 0

def alpha_beta(board,player,ismax,maxp):
    d=terminal_state(board,maxp)
    #print(board,d)
    if d!=2:
        return d
    else:
        if ismax:
            v=-10005
            for i in range(3):
                for j in range(3):
                    if board[i][j]=='_':
                        bc=copy.deepcopy(board)
                        if maxp==1:
                            bc[i][j]='X'
                        else:
                            bc[i][j]='O'
                        v=max(v,alpha_beta(bc,1-player,False,maxp))
            return v
        else:
            v=10005
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        bc = copy.deepcopy(board)
                        if maxp==1:
                            bc[i][j]='O'
                        else:
                            bc[i][j]='X'
                        v = min(v,alpha_beta(bc, 1 - player,True, maxp))
            return v


def nextMove(player, board):
    mv=-10005
    nm=[]
    if player=="0":
        player=0
    else:
        player=1
    #print(player)
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                bc=copy.deepcopy(board)
                if player==0:
                    bc[i][j]='O'
                else:
                    bc[i][j]='X'
                v=alpha_beta(bc,1-player,False,player)
                #print(i,j,v)
                if mv<v:
                    nm=[i,j]
                    mv=v
    print(nm[0],nm[1])
player = input()
board = [['_' for i in range(3)] for i in range(3)]
for i in range(3):
    x = input()
    #print(x)
    j = 0
    for u in x:
        board[i][j] = u
        j = j + 1
# print(board)
nextMove(player, board)