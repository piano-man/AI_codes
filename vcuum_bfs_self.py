from copy import deepcopy
class vaccum:
    def __init__(self, parent, x, y,n,m):
        self.parent = parent
        self.x = x
        self.y = y
        self.grid = []
        self.vis = [[0 for column in range(n)]\
                              for row in range(n)]


def create_node (parent, x, y,n,m):
    return vaccum(parent, x, y,n,m)

def goal(vis, n, m):
    for i in range(n):
        for j in range (m):
            if vis[i][j] == 0:
                return 0
    return 1

def isvalid(node,x, y, n, m):
    if x >= 0 and x < n and y >= 0 and y < m:
        if(node.vis[x][y]==0):
            return 1
    return 0

def expand_nodes (node, n, m):
    expanded_nodes = []
    x1 = node.x
    y1 = node.y
    if isvalid(node,x1-1, y1, n, m):
        expanded_nodes.append(create_node(node, x1-1, y1,n,m))
    if isvalid(node,x1+1, y1, n, m):
        expanded_nodes.append(create_node(node, x1+1, y1,n,m))
    if isvalid(node,x1, y1-1, n, m):
        expanded_nodes.append(create_node(node, x1, y1-1,n,m))
    if isvalid(node,x1, y1+1, n, m):
        expanded_nodes.append(create_node(node, x1, y1+1,n,m))
    return expanded_nodes

def bfs(adj, vis, x, y, n, m):
    nodes = []
    nodes.append(create_node(None, x, y,n,m))
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
        print("position")
        print(node.grid)
        print("visited")
        print(node.vis)
        print("parent")
        if(node.parent==None):
            print("None")
        else:
            print(node.parent.grid)
        print("")

        if goal(node.vis, n, m) == 1:
            return node
        expanded_nodes = expand_nodes(node, n, m)
        nodes = nodes + [node for node in expanded_nodes]

def display_result(node, x, y):
    ans = []
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

        print (node.grid)
        node = node.parent

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
print("")
print("The answer is: ")
display_result(result, x, y)
#print(vis)