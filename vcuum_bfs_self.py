from copy import deepcopy
class vaccum:
    def __init__(self, parent, x, y,n,m,move):
        self.parent = parent
        self.x = x
        self.y = y
        self.grid = []
        self.vis = [[0 for column in range(n)]\
                              for row in range(n)]
        self.move = move

def create_node (parent, x, y,n,m,move):
    return vaccum(parent, x, y,n,m,move)

def goal(vis, n, m):
    for i in range(n):
        for j in range (m):
            if vis[i][j] == 0:
                return 0
    return 1

def check(node,move):
    if(node.move=="UP"):
        if(move == "DOWN"):
            return False
    if(node.move=="DOWN"):
        if(move == "UP"):
            return False
    if(node.move=="LEFT"):
        if(move == "RIGHT"):
            return False
    if(node.move=="RIGHT"):
        if(move == "LEFT"):
            return False
    return True

def isvalid(node,x, y, n, m,move):
    if x >= 0 and x < n and y >= 0 and y < m:
        #if(node.vis[x][y]==0):
        if(check(node,move)):
            return 1
    return 0

def expand_nodes (node, n, m):
    expanded_nodes = []
    x1 = node.x
    y1 = node.y
    if isvalid(node,x1-1, y1, n, m,"UP"):
        expanded_nodes.append(create_node(node, x1-1, y1,n,m,"UP"))
    if isvalid(node,x1+1, y1, n, m,"DOWN"):
        expanded_nodes.append(create_node(node, x1+1, y1,n,m,"DOWN"))
    if isvalid(node,x1, y1-1, n, m,"LEFT"):
        expanded_nodes.append(create_node(node, x1, y1-1,n,m,"LEFT"))
    if isvalid(node,x1, y1+1, n, m,"RIGHT"):
        expanded_nodes.append(create_node(node, x1, y1+1,n,m,"RIGHT"))
    return expanded_nodes

def bfs(adj, vis, x, y, n, m):
    nodes = []
    nodes.append(create_node(None, x, y,n,m,"NULL"))
    while True:
        if len(nodes) == 0:
            return None
        node = nodes.pop(0)
        if(node.parent == None):
            node.grid = deepcopy(adj)

        else:
            node.grid = deepcopy(node.parent.grid)
            node.vis = deepcopy(node.parent.vis)
        node.grid[node.x][node.y] = 0
        node.vis[node.x][node.y] = 1
        """print("position")
        print(node.grid)
        print("visited")
        print(node.vis)
        print("parent")"""
        #if(node.parent==None):
            #print("None")
        #else:
            #print(node.parent.grid)
        #print("")

        if goal(node.vis, n, m) == 1:
            """print("Returned node: ")
            print(node.grid)
            print(node.vis)
            print(node.parent)"""
            return node
        expanded_nodes = expand_nodes(node, n, m)
        nodes = nodes + [node for node in expanded_nodes]
    return None

def display_result(node, x, y):
    ans = []
    count = 0
    #print("Inside display")
    while node != None:
        """temp = []
        temp.append(node.x)
        temp.append(node.y)
        ans.insert(0,temp)
        node = node.parent
    temp = []
    temp.append(x)
    temp.append(y)
    ans.insert(0,temp)"""
        #print("Inside display while")
        count=count+1
        ans.append(node.grid)
        node = node.parent
    while(count>0):
        count=count-1
        print(ans[count])

n,m=input().strip().split()
n,m=int(n),int(m)

adj = []
vis = []

for i in range (n):
    temp = []
    vis.append([])
    for j in range(m):
        temp.append(int(input()))
        vis[i].append(0)
    adj.append(temp)

print(adj)
print(vis)
x = int(input())
y = int(input())
result = bfs(adj, vis, x, y, n, m)
if(result==None):
    print("Result is None")
print("")
print("The answer is: ")
display_result(result, x, y)
#print("Hello")
#print(vis)