import random;
def INTERPRET_INPUT(a, x, y):
        if(a[x][y] == 1):
                return 1;
        else:
                return 0;

def SIMPLE_REFLEX_AGENT(a, x, y):
		if (INTERPRET_INPUT(a, x, y)):
			print("SUCKUP AT ", x, y);
			a[x][y] = 0;
def RULE_MATCH(x, y, vis, a, n, m):
	vis[x][y] = 1;
	
	SIMPLE_REFLEX_AGENT(a, x, y);

	if(x-1 >= 0 and INTERPRET_INPUT(a, x-1, y) and vis[x-1][y] == 0):
		print("MOVE LEFT");
		RULE_MATCH(x-1,y,vis,a,n, m);
	elif(x+1 < n and INTERPRET_INPUT(a, x+1, y) and vis[x+1][y] == 0):
		print("MOVE RIGHT");
		RULE_MATCH(x+1,y,vis,a,n,m);
	elif(y-1 >= 0 and INTERPRET_INPUT(a, x, y-1) and vis[x][y-1] == 0):
		print("MOVE UP");
		RULE_MATCH(x, y-1, vis, a, n, m);
	elif(y+1 < m and INTERPRET_INPUT(a, x, y+1) and vis[x][y+1] == 0):
		print("MOVE DOWN");
		RULE_MATCH(x, y+1, vis, a, n, m);
	else:
		flag = 0;
		x1 = -1;
		y1 = -1;
		for i in range(n):
			for j in range(m):
				if(INTERPRET_INPUT(a, i, j)):
					flag = 1;
					x1 = i;
					y1 = j;
					break;
		if(flag):
			RULE_MATCH(x1, y1, vis, a, n, m);

n = input();
m = input();
a = [];

for i in range(int(n)):
	a.append([]);
	for j in range(int(m)):
		a[i].append(random.randint(0,1));

print(a);
print("Generating random coordinates");
x = random.randint(0, int(n)-1);
y = random.randint(0, int(m)-1);
print(x);
print(y);

vis = [];

for i in range(int(n)):
	vis.append([]);
	for j in range(int(m)):
		vis[i].append(0);



RULE_MATCH(x, y, vis, a, int(n), int(m));
print(a);

