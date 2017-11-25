import random
import queue
class Vacuum:

	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.arr = [];
		for i in range(0, n):
			en = []
			for j in range(0, m):
				en.append(0)
			self.arr.append(en)


	def fill(self, p):
		val = p * (self.n) * (self.m)
		val = val//100
		while(val > 0):
			fx = random.randint(0, self.n - 1);
			fy = random.randint(0, self.m - 1);
			if self.arr[fx][fy] != 1:
				self.arr[fx][fy] = 1
				val = val - 1
	

	def show(self):
		print(self.arr);
	
	def moveUp(self, tup):
		tup1 = (tup[0] - 1, tup[1])
		print("MOVE UP FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveDown(self, tup):
		tup1 = (tup[0] + 1, tup[1])
		print("MOVE DOWN FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveLeft(self, tup):
		tup1 = (tup[0], tup[1] - 1)
		print("MOVE LEFT FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveRight(self, tup):
		tup1 = (tup[0], tup[1] + 1)
		print("MOVE RIGHT FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def INTERPRET_INPUT(self, x, y):
		if(self.arr[x][y] == 1):
			return "dirty"
		return "clean"
	def NEXT_CHILDREN(self, x, y):
		nexxt = []
		tup = (x, y)
		if x == 0 and y == 1:
			nexxt.append(self.moveLeft(tup))
			nexxt.append(self.moveDown(tup))
		if x == 0 and y == 0:
			nexxt.append(self.moveRight(tup))
			nexxt.append(self.moveDown(tup))
		if x == 1 and y == 0:
			nexxt.append(self.moveRight(tup))
			nexxt.append(self.moveUp(tup))
		if x == 1 and y == 1:
			nexxt.append(self.moveLeft(tup))
			nexxt.append(self.moveUp(tup))
		return nexxt

	def SIMPLE_REFLEX_AGENT(self, x, y):
		if self.arr[x][y] == 1:
			print("SUCKUP AT " + str(x) + " " + str(y))
			self.arr[x][y] = 0
		#return self.RULE_MATCH(x, y)
	def RULE_MATCH(self, x, y):

		vis = set()
		frontier = list()
		
		tup = (x, y)
		frontier.append((x, y))
		while frontier:
			curr = frontier.pop(0)
			vis.add(curr)
			#self.SIMPLE_REFLEX_AGENT(curr[0], curr[1])
			#print(self.arr[curr[0]][curr[1]])
			if (self.arr[curr[0]][curr[1]]):
				print("SUCKUP")
				self.arr[curr[0]][curr[1]] = 0
			next_state = self.NEXT_CHILDREN(curr[0], curr[1])
			for z in next_state:
				if z not in vis:
					frontier.append(z)
		print(curr)

	def reachTop(self, x, y):
		tup = (x, y)
		while(tup[0] > 0):
			if(self.arr[tup[0]][tup[1]] == 1):
				print("SUCKUP AT " + str(x) + " " + str(y))
				self.arr[x][y] = 0
			tup = self.moveUp(tup)
		while(tup[1] > 0):
			if(self.arr[tup[0]][tup[1]] == 1):
				print("SUCKUP AT " + str(x) + " " + str(y))
				self.arr[x][y] = 0
			tup = self.moveLeft(tup)

	def clearAll(self, x, y):
		#self.reachTop(x, y)
		#tup = (x,y)
		#while(tup[0] < self.n):
		#tup = self.SIMPLE_REFLEX_AGENT(tup[0], tup[1], self.INTERPRET_INPUT(tup[0], tup[1]))
		self.RULE_MATCH(x, y)
n1, m1 = input().split(' ')
vac = Vacuum(2, 2)
#vac.fill(40)
temp = input().split(' ')
vac.arr[0][0] = temp[0]
vac.arr[0][1] = temp[1]
vac.arr[1][0] = temp[2]
vac.arr[1][1] = temp[3]
print("Initial State:")
vac.show()
#vac.clearAll(int(n1), int(m1))
vac.RULE_MATCH(int(n1), int(m1))
vac.show()