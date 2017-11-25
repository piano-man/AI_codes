import random


def rule(cstatus, x, y, c, n, m, visited):
    flag = 0
    while flag == 0:
        #r = random.randrange(4)
        if (x - 1 >= 0):
            print('UP ', x, y, ' to ', x - 1, y)
            func(cstatus, x - 1, y, c, n, m, visited)
            flag = 1
        elif (x + 1 < n):
            print('DOWN ', x, y, ' to ', x + 1, y)
            func(cstatus, x + 1, y, c, n, m, visited)
            flag = 1
        elif (y - 1 >= 0):
            print('LEFT ', x, y, ' to ', x, y - 1)
            func(cstatus, x, y - 1, c, n, m, visited)
            flag = 1
        elif (y + 1 < m):
            print('RIGHT ', x, y, ' to ', x, y + 1)
            func(cstatus, x, y + 1, c, n, m, visited)
            flag = 1
    return


def func(cstatus, x, y, c, n, m, visited):
    if (n == 1 and m == 1):
        if (cstatus[0][0] == 'D'):
            print('Sucked at ', 0, 0)
            cstatus[0][0] = 'C'
            visited[0][0] = 1
        else:
            visited[0][0] = 1
            return
    flag = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                flag = 1
    if flag == 0:
        return

    visited[x][y] = 1

    if (cstatus[x][y] == 'D'):
        cstatus[x][y] = 'C'
        print('Sucked at ', x, y)
    if (x - 1 >= 0 and cstatus[x - 1][y] == 'D'):
        print('UP ', x, y, ' to ', x - 1, y)
        func(cstatus, x - 1, y, c, n, m, visited)
    elif (x + 1 < n and cstatus[x + 1][y] == 'D'):
        print('DOWN ', x, y, ' to ', x + 1, y)
        func(cstatus, x + 1, y, c, n, m, visited)
    elif (y - 1 >= 0 and cstatus[x][y - 1] == 'D'):
        print('LEFT ', x, y, ' to ', x, y - 1)
        func(cstatus, x, y - 1, c, n, m, visited)
    elif (y + 1 < m and cstatus[x][y + 1] == 'D'):
        print('RIGHT ', x, y, ' to ', x, y + 1)
        func(cstatus, x, y + 1, c, n, m, visited)
    else:
        rule(cstatus, x, y, c, n, m, visited)


n, m = input().split(' ')
n = int(n)
m = int(m)
cstatus = []
visited = []
for i in range(n):
    cstatus.append([])
    visited.append([])
    for j in range(m):
        x = random.randrange(2)
        visited[i].append(0)
        if x == 0:
            cstatus[i].append('C')
        else:
            cstatus[i].append('D')
print(cstatus)
x = random.randrange(n)
y = random.randrange(m)
c = 0
func(cstatus, x, y, c, n, m, visited)
print(visited)