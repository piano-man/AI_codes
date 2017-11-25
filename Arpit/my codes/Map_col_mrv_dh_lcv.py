import Queue as q
def select_unassigned_var(n,col,dom,adj):
    mn=len(dom[n-1])+1
    mnv=0
    for i in range(n):
        if col[i]==-1:
            if mn>len(dom[i]):
                mn=len(dom[i])
                mnv=i
            elif mn==len(dom[i]):
                if len(adj[mnv])<len(adj[i]):
                    mnv=i
    return mnv
def is_safe(mnv,col,n,x):
    for i in adj[mnv]:
        if col[i]==x:
            return False
    return True
def order_dom_value(mnv,dom,col,adj):
    pq=q.PriorityQueue()
    for i in dom[mnv]:
        c=0
        for j in adj[mnv]:
            #print(col[j], "**")
            if col[j]==i:
                c=c+1
        pq.put(tuple((c,i)))
    ans=[]
    while pq.empty()==False:
        x=pq.get()
        ans.append(x[1])
    return ans
def backtrack_csp(n,adj,col,dom):
    f=0
    for i in range(n):
        if col[i]==-1:
            f=1
    if f==0:
        return True
    mnv=select_unassigned_var(n,col,dom,adj)
    print(mnv)
    lst=order_dom_value(mnv,dom,col,adj)
    for i in lst:
        if is_safe(mnv,col,n,i):
            col[mnv]=i
            aff=[]
            for j in adj[mnv]:
                if dom[j].__contains__(i):
                    dom[j].remove(i)
                    aff.append(j)
            if backtrack_csp(n,adj,col,dom)==True:
                return True
            col[mnv]=-1
            for j in aff:
                dom[j].append(i)
    return False
n,m=raw_input().split(' ')
n,m=int(n),int(m)
adj=[[]for i in range(n)]
col=[-1 for i in range(n)]
dom=[['Red','Green','Blue']for i in range(n)]
for i in range(m):
    u,v=raw_input().split(' ')
    u,v=int(u),int(v)
    adj[u].append(v)
    adj[v].append(u)
print(adj)
if backtrack_csp(n,adj,col,dom):
    for i in range(n):
        print('Node ',i,'has color : ',col[i])
else:
    print('No solution')
