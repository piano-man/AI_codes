import heapq

n = 20
adj = []
h = []
p = []
def initialize():
	for i in range(n):
		h.append(0)
		p.append(-1)
		temp = []
		for j in range(n):
			temp.append(0)
		adj.append(temp)
	mp = [ 'Arad', 'Oradea', 'Zerind','Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Rimnicu Vilcea', 'Pitesti', 'Fagaras', 'Giurgiu', 'Urziceni', 'Eforie', 'Hirsova', 'Vaslui', 'Iasi', 'Neamt', 'Bucharest']
	return mp

def getIndex(s):
	return mp.index(s);

def fill(s1, s2, v):
	id1 = getIndex(s1)
	id2 = getIndex(s2)
	adj[id1][id2] = v
	adj[id2][id1] = v

def initializeGraph():
	fill('Oradea', 'Zerind', 71)
	fill('Oradea', 'Sibiu', 151)
	fill('Zerind', 'Arad', 75)
	fill('Arad', 'Sibiu', 140)
	fill('Arad', 'Timisoara', 118)
	fill('Timisoara', 'Lugoj', 111)
	fill('Lugoj', 'Mehadia', 70)
	fill('Mehadia', 'Dobreta', 75)
	fill('Dobreta', 'Craiova', 120)
	fill('Sibiu', 'Fagaras', 99)
	fill('Sibiu', 'Rimnicu Vilcea', 80)
	fill('Rimnicu Vilcea', 'Craiova', 146)
	fill('Rimnicu Vilcea', 'Pitesti', 97)
	fill('Pitesti', 'Bucharest', 101)
	fill('Fagaras', 'Bucharest', 211)
	fill('Bucharest', 'Giurgiu', 90)
	fill('Urziceni', 'Bucharest', 85)
	fill('Vaslui', 'Urziceni', 142)
	fill('Iasi', 'Vaslui', 92)
	fill('Neamt', 'Iasi', 87)
	fill('Urziceni', 'Hirsova', 98)
	fill('Hirsova', 'Eforie', 86)
	
def mark(s, v):
	id = getIndex(s)
	h[id] = v

def initializeHeuristic():
	mark('Arad', 366)
	mark('Bucharest', 0)
	mark('Craiova', 160)
	mark('Dobreta', 242)
	mark('Eforie', 161)
	mark('Fagaras', 176)
	mark('Giurgiu', 77)
	mark('Hirsova', 151)
	mark('Iasi', 226)
	mark('Lugoj', 244)
	mark('Mehadia', 241)
	mark('Neamt', 234)
	mark('Oradea', 380)
	mark('Pitesti', 100)
	mark('Rimnicu Vilcea', 193)
	mark('Sibiu', 253)
	mark('Timisoara', 329)
	mark('Urziceni', 80)
	mark('Vaslui', 199)
	mark('Zerind', 374)

def calcDistance(initial, goal):
	pq = []
	path = []
	#path.append(initial)
	heapq.heapify(pq)
	val = 0
	dist = []
	for i in range(n):
		dist.append(100000000)
	dist[getIndex(initial)] = 0
	heapq.heappush(pq, (val, getIndex(initial)))
	fin = getIndex(goal)
	while pq:
		tup = heapq.heappop(pq)
		pq.clear()
		id = tup[1]
		path.append(mp[id])
		dist[id] = tup[0]
		wt = dist[id]
		if(id == fin):
			break
		for i in range(n):
			val2 = adj[id][i]
			if val2 != 0:
				heapq.heappush(pq, (wt + val2 , i))
	print(path)
	return dist[fin]

mp = initialize()
initializeGraph()
initializeHeuristic()
'''for i in range(n):
	for j in range(n):
		print(adj[i][j], end = ' ')
	print()'''
'''for i in range(n):
	print(h[i]) '''
initial = input()
goal = input()

ans = calcDistance(initial, goal)
print(ans)