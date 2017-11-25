from queue import PriorityQueue
from copy import deepcopy
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
q = PriorityQueue()

def solver(parent):
    vis = set()
    while (not q.empty()):
        board = q.get()[1]
        vis.add(tuple(tuple(x) for x in board))
        if (board == goal):
            return 1
        x,y = 0,0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
        cost = x + y
        boardc = deepcopy(board)
        if(x - 1 >= 0):
            boardc[x - 1][y], boardc[x][y] = boardc[x][y],boardc[x - 1][y]
            if tuple(tuple(x) for x in boardc) not in vis:
                q.put([cost - 1, boardc])
                parent[tuple(tuple(x) for x in boardc)] = board
        boardc = deepcopy(board)
        if(x + 1 <= 2):
            boardc[x + 1][y], boardc[x][y] = boardc[x][y], boardc[x + 1][y]
            if tuple(tuple(x) for x in boardc) not in vis:
                q.put([cost + 1, boardc])
                parent[tuple(tuple(x) for x in boardc)] = board
        boardc = deepcopy(board)
        if (y + 1 <= 2):
            boardc[x][y + 1], boardc[x][y] = boardc[x][y], boardc[x][y + 1]
            if tuple(tuple(x) for x in boardc) not in vis:
                q.put([cost + 2, boardc])
                parent[tuple(tuple(x) for x in boardc)] = board
        boardc = deepcopy(board)
        if (y - 1 >= 0):
            boardc[x][y - 1], boardc[x][y] = boardc[x][y], boardc[x][y - 1]
            if tuple(tuple(x) for x in boardc) not in vis:
                q.put([cost - 2, boardc])
                parent[tuple(tuple(x) for x in boardc)] = board

def printsol(parent, board):
    # print(type(board))
    if parent[board] == None:
        print(board)
        return
    printsol(parent, tuple(tuple(i) for i in parent[board]))
    print(board)

def main():
    board = []
    parent = {}
    #print(goal)
    check = []
    for i in range(3):
        x = input().split(' ')
        l = [int(x[i]) for i in range(3)]
        for j in l:
            check.append(j)
        board.append(l)
    inv = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if(check[i] != 0 and check[j] != 0 and check[i] > check[j]):
                inv = inv + 1
    if inv % 2 == 1:
        print("No Path")
    else:
        q.put([0, board])
        parent[tuple(tuple(x) for x in board)] = None
        x = solver(parent)
        if(x == 1):
            printsol(parent, tuple(tuple(x) for x in goal))
        else:
            print("No Solution")

if __name__ == "__main__":
    main()