from queue import PriorityQueue
from copy import deepcopy
import hashlib
states = []

class State:
	def __init__ (self, grid, val) :
		self.grid = deepcopy (grid)
		self.heuristic = self.cal_heur ()
		self.ctn = val

	def cal_heur (self) :
		#n = 5
		tl = deepcopy(self.grid)
		cnt = 0
		for i in range(n) :
			for j in range(i+1,n) :
				if tl[i] == tl[j] or abs(tl[i]-tl[j]) == abs(i-j) :
					cnt = cnt+1

		return cnt

def A_star (s) :
#	n = 5
	q = PriorityQueue ()
	q.put ([s.heuristic, s.grid, s.ctn])
	#st = ''.join (str(e) for e in s .grid)
	while q.empty() == False :
		cur = q.get()
		st = ''.join(str(e) for e in cur[1])
		if st in states:
			continue
		states.append(st)
		if cur[0]-cur[2] == 0 :
			return cur[1]
		lis = deepcopy(cur[1])
		for i in range(n) :
			if lis[i] < n-1 :
				lis[i] = lis[i]+1
				ns = State (lis, 0)
				lis[i] = lis[i]-1
				q.put ([ns.heuristic+cur[2]+1, ns.grid, cur[2]+1])


n = int(input())
initial_grid = []
for i in range(n) :
	initial_grid.append(0)


IN = State (initial_grid, 0)
ANS = A_star (IN)

for i in range(n):
	print (ANS[i], end = ' ')
print()
