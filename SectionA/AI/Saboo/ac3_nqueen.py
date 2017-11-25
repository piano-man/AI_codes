import copy

def nqchecker(ans,n):
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if i==j or ans[i]==ans[j]:
                return False
            if abs(i-j)==abs(ans[i]-ans[j]):
                return False
    return True


def check(board,i,j,dom,x,n):

    if board[x][j]==1:
        return 0
    for f in dom[j]:
        if abs(i-j)==abs(f-x) and board[f][j]==1:
            return 0

    #print(i,j,1)
    return 1
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
            if check(board,i,j,dom,x,n)==0:
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

def backtrack(n,board,col,ans,dom):
    if col==n:
        return True
    for i in dom[col]:
        #print(i,col)
        board[i][col]=1
        dom1 = copy.deepcopy(dom)
        if ac3(board,dom1,n,col):
            #print(col,'*******')
            ans.append(i)
            #print(i,ans,col)
            if backtrack(n,board,col+1,ans,dom1):
                return True
            ans.pop()
        board[i][col]=0
    return False
n=input()
n=int(n)
board=[[0 for j in range(n)]for i in range(n)]
dom=[[j for j in range(n)]for i in range(n)]
#print(dom)
ans=[]
if backtrack(n,board,0,ans,dom):
    print('Yes',ans)
else:
    print('No')

print(nqchecker(ans,n))