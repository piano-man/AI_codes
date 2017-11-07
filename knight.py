import sys;

xg = [2,2,-2,-2,1,1,-1,-1]
yg = [1,-1,1,-1,2,-2,2,-2]

def checkc(grid,n):
    for i in range (n):
        for j in range (n):
            if(grid[i][j]==-1):
                return False
    return True

def is_safe(grid,x,y,n):
    if(x>=n or x<0 or y>=n or y<0):
        return False
    if(grid[x][y]!=-1):
        return False
    return True



def knightm(grid,n,x,y,num):
    if(checkc(grid,n)):
        return grid
    else:
        print(grid)
        for i in range (n):

            if(is_safe(grid,x+xg[i],y+yg[i],n)):
                grid[x+xg[i]][y+yg[i]] = num+1
                if(knightm(grid,n,x+xg[i],y+yg[i],num+1)==None):
                    grid[x+xg[i]][y+yg[i]] = -1
                else:
                    return grid
        return None


def main():
    n = 6
    grid = []
    temp = []
    #nn = n*n
    for i in range (n):
        for j in range (n):
            temp.append(-1)
        grid.append(temp)
        temp = []
    grid[0][0]=0
    new_grid = knightm(grid,n,0,0,0)
    if(new_grid == None):
        print("No solution")
    else:
        for i in range (8):
            for j in range (8):
                print(new_grid[i][j])


main()
"""
0 59 38 33 30 17 8 63
37 34 31 60 9 62 29 16
58 1 36 39 32 27 18 7
35 48 41 26 61 10 15 28
42 57 2 49 40 23 6 19
47 50 45 54 25 20 11 14
56 43 52 3 22 13 24 5
51 46 55 44 53 4 21 12
"""