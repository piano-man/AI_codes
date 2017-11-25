import copy
import queue as q
def ac3(dom,n,u,col):
    qu=q.Queue()
    for i in range(n):
        for j in adj[i]:
            if i!=u and j!=i:
                qu.put([i,j])
    while qu.empty()==False:
        a=qu.get()
        i,j=a[0],a[1]
        flag=0
        if col[j]!=-1 and dom[i].__contains__(col[j]):
            dom[i].remove(col[j])
            flag=1
        if flag==1:
            for x in range(n):
                if x!=i and adj[x].__contains__(i):
                    qu.put([x,i])
    for i in range(n):
        if len(dom[i])==0:
            return False
    return True

def backtrack(u,dom,n,adj,col):
    if u==n:
        return True
    for i in dom[u]:
        col[u]=i
        dom1=copy.deepcopy(dom)
        if ac3(dom1,n,u,col):
            if backtrack(u+1,dom1,n,adj,col):
                return True
        col[u]=-1
    return False
n,m=input().split(' ')
n,m=int(n),int(m)
dom=[['Red','Blue','Green']for i in range(n)]
adj=[[]for i in range(n)]
col=[-1 for i in range(n)]
for i in range(m):
    u,v=input().split(' ')
    u,v=int(u),int(v)
    adj[u].append(v)
    adj[v].append(u)
if backtrack(0,dom,n,adj,col):
    print('Solved',col)
else:
    print('No solution')
