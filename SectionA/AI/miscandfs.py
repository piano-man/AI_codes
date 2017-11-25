class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
def dfs(n,par):
    q=Stack()
    vis=[]
    q.push((n,n,'L'))
    par[(n,n,'L')]=(-1,-1,'N')
    while not q.isEmpty():
        #print(q.peek())
        ls=q.pop()
        m=ls[0]
        c=ls[1]
        vis.append(ls)
       # print(vis)
        if m==0 and n==0 and ls[2]=='R':
            break
        if ls[2]=='L':
            if m-1>=0:
                lsm=m-1
                rsm=n-(m-1)
                lsc=c
                rsc=n-c
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                   # print(nl)
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if c-1>=0:
                lsm=m
                rsm=n-m
                lsc=c-1
                rsc=n-(c-1)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                   # print(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if m-1>=0 and c-1>=0:
                lsm=m-1
                rsm=n-(m-1)
                lsc=c-1
                rsc=n-(c-1)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                   # print(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if m-2>=0:
                lsm=m-2
                rsm=n-(m-2)
                lsc=c
                rsc=n-c
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                  #  print(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if c-2>=0:
                lsm=m
                rsm=n-m
                lsc=c-2
                rsc=n-(c-2)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                   # print(nl)
                    #vis.append(nl)
                    par[nl]=ls
        else:
            rm=n-m
            rc=n-c
            if rm-1>=0:
                lsm=m+1
                rsm=rm-1
                lsc=c
                rsc=rc
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if rc-1>=0:
                lsm=m
                rsm=rm
                lsc=c+1
                rsc=rc-1
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if rm-1>=0 and rc-1>=0:
                lsm=m+1
                rsm=rm-1
                lsc=c+1
                rsc=rc-1
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if rm-2>=0:
                lsm=m+2
                rsm=rm-2
                lsc=c
                rsc=rc
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls
            if rc-2>=0:
                lsm=m
                rsm=rm
                lsc=c+2
                rsc=rc-2
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.push(nl)
                    #vis.append(nl)
                    par[nl]=ls

def pp(ls,s,par):
    if ls.__eq__(s):
        print(s)
    elif ls not in par:
        print('Not exist')
        return
    else:
        pp(par[ls],s,par)
        print(ls)
n=input()
n=int(n)
par={}
dfs(n,par)
print()
#print(par)
pp((0,0,'R'),(n,n,'L'),par)
