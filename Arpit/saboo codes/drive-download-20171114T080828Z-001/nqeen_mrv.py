import copy
def select_unass_var(dom,n,vis):
    mn=10005
    x=0
    for i in range(n):
        if mn>len(dom[i]) and vis[i]==0:
            mn=len(dom[i])
            x=i
    return x
def reduce_domain(dom1,n,x,p,board):
    for i in range(n):
        if i!=p:
            rem=[]
            for j in dom1[i]:
                if abs(i-p)==abs(x-j) or i==p or x==j:
                    rem.append(j)
            for u in rem:
                dom1[i].remove(u)
    for i in range(n):
        if len(dom1[i])==0:
            return False
    #print(x,p,dom1)
    return True
def backtrack(n,dom,board,ans):
    flag=0
    for i in range(n):
        if vis[i]==0:
            flag=1
    if flag==0:
        return True
    col=select_unass_var(dom,n,vis)
    for i in dom[col]:
        #print(i,col)
        board[i][col]=1
        vis[col]=1
        ans[col]=i
        dom1=copy.deepcopy(dom)
        if reduce_domain(dom1,n,i,col,board):
            if backtrack(n,dom1,board,ans):
                return True
        ans[col]=-1;
        vis[col]=0
        board[i][col]=0
    #print(i,dom[i])
    return False
n=int(input())
board=[[0 for j in range(n)]for i in range(n)]
vis=[0 for i in range(n)]
ans=[-1 for i in range(n)]
dom=[[i for i in range(n)]for j in range(n)]
if backtrack(n,dom,board,ans):
    print(ans)
else:
    print('No solution')