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

    flag1 = 0
    flag2 = 0
    #print(dom,"this is dom")
    for f in dom[j]:
        if f != x:
            flag1 = 1
    for f in dom[j]:
        if abs(i-j)!=abs(f-x):
            flag2 = 1
    if flag1 == 1 and flag2 == 1:
        return 1
    return 0


def ac3(board,dom,n,col):
    qu=[]
    for i in range(n):
        if(i > col):
            qu.append([i,col])
    print(qu)
    while len(qu):
        a=qu[0]
        qu.remove(qu[0])
        i,j=a[0],a[1]
        rem=[]
        #print(i,j,"*******")
        for x in dom[i]:
            if check(board,i,j,dom,x,n)==0:
                #print(i,j,x,board)
                #print(x,"**")
                rem.append(x)
        for u in rem:
            dom[i].remove(u)
        if len(dom[i])==0:
            return False
        if len(rem)>0:
            for b in range(n):
                if b!=i and qu.__contains__([b,i])==False and b!=j:
                    qu.append([b,i])
#   print(qu,"this is qu")
    return True

def backtrack(n,board,col,ans,dom):
    print(col)
    print(dom)
    if col==n:
        return True
    for i in dom[col]:
        #print(i,col)
        board[i][col] = 1
        dom1 = copy.deepcopy(dom)
        del dom1[col][:]
        dom1[col].append(i)
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
#print(board)
dom=[[j for j in range(n)]for i in range(n)]
#print(dom)
ans=[]
if backtrack(n,board,0,ans,dom):
    print('Yes',ans)
else:
    print('No')

print(nqchecker(ans,n))
