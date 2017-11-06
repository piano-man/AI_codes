from math import floor

def getX(index, m,n):
    return floor((index / n))


def getY(index,m,n):
    return floor((index % n))


def clear(matrix):
    for i in range(100):
        matrix[i] = -1

def is_safe(x,y,m,n):
    if (x >= m or x < 0 or y < 0 or y >= n):
        return False
    return True

def check(graph, mat, visit, m , n ,index):
    for i in range(0,index+1):
        if (mat[i] == -1):
            continue
        
        curr_x = int(getX(i,m,n))
        curr_y = int(getY(i,m,n))
        #print (curr_x,curr_y)
        for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
            if (is_safe(curr_x + x,curr_y + y , m , n)== False):
                continue
            child_x = curr_x + x
            child_y = curr_y + y
            child_index = int((child_x * n + child_y ))
            #print (child_index)
            if (mat[child_index] == -1):
                continue
            if mat[child_index] not in graph[i]:
                return 0
    print ("Nice bro")
    return 1

def solve(graph, mat, visit ,m, n, index):
    if (index >= m * n - 1):
        return 1
    flag = 0
    for i in range(0,m*n):
        if (visit[i] == 1):
            continue
        mat[index+1] = i
        visit[i] = 1
        temp = check(graph,mat,visit,m,n,index+1)
        if (temp == 0):
            mat[index + 1] = -1
            visit[i] = 0
            continue
        flag = 1
        ans = solve(graph, mat, visit, m , n, index + 1)
        if (ans == -1):
            for j in range(index + 1,100):
                mat[j] = -1
            flag = 0
            visit[i] = 0
    print (index)
    for i in range(0,m*n):
        print (mat[i], end = ' ')
    print ("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    if (flag == 0):
        return -1
    return 1

t= int(input())
while (t > 0):
    m,n = map(int,input().strip().split())
    
    total = m * n
    graph = [list() for x in range(100)]
    
    for x in range(total):
        num = list(map(int,input().strip().split()))
        for j in range(2,len(num)):
            graph[num[0]].append(num[j])
        #graph[num[0]].sort()

    
    matrix = [-1] * 100
    visit =[0 for x in range(100)]

    flag = 0
    for i in range(0,m*n):
        clear(matrix)
        for j in range(100):
            visit[j] = 0
        matrix[0] = i
        visit[i] = 1
        ans = solve(graph,matrix,visit,m,n,0)
        if (ans  != -1):
            flag = 1
            for x in range(0,m*n):
                print (matrix[i])
            break
        
    if (flag == 0):
        print ("NO solution found")
    t = t - 1
    