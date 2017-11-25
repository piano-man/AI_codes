def getMRVDH(col):
	list1 = []
	for i in range(n):
		if(col[i] == -1):
			valid = []
			for j in range(c):
				valid.append(1)
			temp = 0;
			for j in range(n):
				if adj[i][j] != 0:
					temp+=1
					if col[j] != -1:
						valid[col[j]] = 0
			cur = 0
			for j in range(c):
				cur = cur + valid[j]
			list1.append((cur, temp, i))

	list1.sort()
	return list1

def getValid(id, col):
	count = 0
	vis = []
	for i in range(c):
		vis.append(1)
	for i in range(n):
		if adj[id][i] != 0 and col[i] != -1:
			vis[col[i]] = 0;
	for i in range(c):
		count+=vis[i]
	return count

def getTotal(id, col):
	sum = 0
	for i in range(n):
		if adj[id][i] != 0:
			sum+=getValid(i, col)
	return sum

def findColouring(col, count):
	if count == n:
		return True
	ord = getMRVDH(col)
	for el in ord:
		id = el[2]
		ord2 = []
		valid = []
		for i in range(c):
			valid.append(1)
		for i in range(n):
			if adj[id][i] != 0 and col[i] != -1:
				valid[col[i]] = 0
		for i in range(c):
			if valid[i] == 1:
				col[id] = i
				val = getTotal(id, col)
				col[id] = -1
				ord2.append((val, i))
		ord2.sort()
		for ind in ord2:
			sc = ind[1]
			col[id] = sc;
			if findColouring(col, count + 1):
				return True
			col[id] = -1
	return False
n = (int)(input())
adj = []
for i in range(n):
	adj.append(n * [0])
while True:
	a, b = (input().split(' '))
	a = (int)a 
	b = (int)b
	#b = (int)(input())
	if a == -1:
		break
	adj[a][b] = 1	    
	adj[b][a] = 1
c = (int)(input())
col = []
for i in range(n):
	col.append(-1)
if findColouring(col, 0):
	for i in range(n):
		print(i, end = " ")
		print(col[i])
else:
	print("Not colourable")