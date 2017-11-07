#solved using bfs to reduce computational time

class vaccum:
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x = x
        self.y = y

def create_node (parent, x, y):
    return vaccum(parent, x, y)

def goal(vis, n, m):
    for i in range(n):
        for j in range (m):
            if vis[i][j] == 0:
                return 0
    return 1

def isvalid(x, y, n, m):
    if x >= 0 and x < n and y >= 0 and y < m:
        return 1
    else:
        return 0

def expand_nodes (node, n, m):
    expanded_nodes = []
    x1 = node.x
    y1 = node.y
    if isvalid(x1-2, y1+1, n, m):
        expanded_nodes.append(create_node(node, x1-1, y1))
    if isvalid(x1+2, y1+1, n, m):
        expanded_nodes.append(create_node(node,x1-2, y1+1))
    if isvalid(x1-2, y1-1, n, m):
        expanded_nodes.append(create_node(node, x1-2, y1-1))
    if isvalid(x1+2, y1-1, n, m):
        expanded_nodes.append(create_node(node,x1+2, y1-1))
    if isvalid(x1+1, y1+2, n, m):
        expanded_nodes.append(create_node(node, x1+1, y1+2))        
    return expanded_nodes
    if isvalid(x1+1, y1-2, n, m):
        expanded_nodes.append(create_node(node,x1+1, y1-2))
    if isvalid(x1-1, y1-2, n, m):
        expanded_nodes.append(create_node(node, x1-1, y1-2))
    if isvalid(x1-1, y1+2, n, m):
        expanded_nodes.append(create_node(node, x1-1, y1+2))        
def bfs(adj, vis, x, y, n, m):
    nodes = []
    nodes.append(create_node(None, x, y))
    while True:
        if len(nodes) == 0:
            return None
        node = nodes.pop(0)
        adj[node.x][node.y] = 0
        vis[node.x][node.y] = 1
        print("position")
        print(node.x)
        print(node.y)
        if goal(vis, n, m) == 1:
            return node
        expanded_nodes = expand_nodes(node, n, m)
        nodes = nodes + [node for node in expanded_nodes]

def display_result(node, x, y):
    ans = []
    while node.parent != None:
        temp = []
        temp.append(node.x)
        temp.append(node.y)
        ans.insert(0,temp)
        node = node.parent
    temp = []
    temp.append(x)
    temp.append(y)
    ans.insert(0,temp)
    print (ans)

n,m=input().strip().split()
n,m=int(n),int(m)

adj = []
vis = []

for i in range (n):
    temp = []
    vis.append([])
    for j in range(m):
        temp.append(int(input().strip()))
        vis[i].append(0)
    adj.append(temp)

print(adj)
print(vis)
x = int(input())
y = int(input())
result = bfs(adj, vis, x, y, n, m)
display_result(result, x, y)
print(vis)
