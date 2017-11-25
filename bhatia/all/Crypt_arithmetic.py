def issolv(a,b,c,map):
    na,nb,nc=0,0,0
    for u in a:
        na*=10
        na+=map[u]
    for u in b:
        nb*=10
        nb+=map[u]
    for u in c:
        nc*=10
        nc+=map[u]
    if na+nb==nc:
        print(map,na,nb,nc)
        return True
    else:
        return False

def recur(a,b,c,str,cd,map,pos):
        if  len(str)==pos:
            return issolv(a,b,c,map)
        else:
            for i in range(10):
                if cd[i]==0:
                    cd[i]+=1
                    map[str[pos]]=i
                    if recur(a,b,c,str,cd,map,pos+1):
                        return True
                    cd[i]=0
                    map[str[pos]]=-1

ls=input().split(' ')
a,b,c=ls[0],ls[1],ls[2]
cnt={}
for x in a:
    if cnt.__contains__(x):
        cnt[x]+=1
    else:
        cnt[x]=1
for x in b:
    if cnt.__contains__(x):
        cnt[x]+=1
    else:
        cnt[x]=1
for x in c:
    if cnt.__contains__(x):
        cnt[x]+=1
    else:
        cnt[x]=1
str=""
for k,v in cnt.items():
    str=str+k;
cd=[0 for i in range(10)]
map={}
for u in str:
    map[u]=-1
if recur(a,b,c,str,cd,map,0):
    print('Solved')
else:
    print('Not solvable')


#give input as send more money (send+more=money)