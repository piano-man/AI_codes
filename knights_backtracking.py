N = 5 # This way you can test it with 5 or 6 and even 100 if you want to.
visited = [[False for x in range(N)] for y in range(N)]

def move(x,y,m):

    result=False
    if x<0 or x>=N or y<0 or y>=N or visited[x][y]==True: # You may merge these two ifs.
        return False
    visited[x][y]=True
    if m==(N * N - 1):
        print "a solution has been found"
        visited[x][y]=True # Set visited here tot true.
        return True
    else:
        print x,",",y
        if (move(x+2,y+1,m+1) or move(x+2,y-1,m+1)
            or move(x-2,y+1,m+1) or move(x-2,y-1,m+1)
            or move(x+1,y+1,m+1) or move(x+1,y-1,m+1)
            or move(x-1,y+1,m+1) or move(x-1,y-1,m+1)): # Place them in one if.
            print x,",",y

            return True
    return False # If the algorithm comes here it may return false

print move(2,1,0)