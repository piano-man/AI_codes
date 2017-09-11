class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)
dirty_nodes = []
move=' '
board=[]
near_flag=0
nearest_node  = None


def next_move(posx, posy, board):
    # the input x and y were reversed in Hackerrank puzzles.
    bot_node = Node(posx, posy)
    global dirty_nodes
    global nearest_node
    dirty_nodes=[]
    print("in next move")
    for i in range(len(board)):

        for j in range(len(board[i])):
            print(board[i][j],end='')
        print('')
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":

                dirty_nodes.append(Node(i, j))

    # find the nearest dirty node.
    print("dirty nodes")
    for i in dirty_nodes:
        print(i.x,i.y,end='')
    print('')

    if near_flag is 0:

        nearest_node = None
        for node in dirty_nodes:
            if nearest_node is None or node.distTo(bot_node) < nearest_node.distTo(bot_node):
                nearest_node = node

    if nearest_node is not None:
        print_move(nearest_node.x - bot_node.x, nearest_node.y - bot_node.y,bot_node.x,bot_node.y,board)


def print_move(delta_x, delta_y,x,y,board):
    global move
    global near_flag
    if delta_y < 0 :

        print ("LEFT")
        move = 'l'
        board[x][y]='-'
        board[x][y-1]='b'
        near_flag=1
    elif delta_y > 0 :

        print ("RIGHT")
        move='r'
        board[x][y]='-'
        board[x][y+1]='b'
        near_flag=1
    elif delta_x < 0 :

        print ("UP")
        move='u'
        board[x][y]='-'
        board[x-1][y]='b'
        near_flag=1
    elif delta_x > 0 :

        print ("DOWN")
        move='d'
        board[x][y]='-'
        board[x+1][y]='b'
        near_flag=1
    else:

        print ("CLEAN")
        board[x][y]="b"
        move='c'
        near_flag=0

# Tail starts here
if __name__ == "__main__":
    
    
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    for i in range(len(board)):

        for j in range(len(board[i])):

            if board[i][j] == "d":
                dirty_nodes.append(Node(j, i))
    
    while dirty_nodes:
        print(pos[0],pos[1])
        next_move(pos[0], pos[1], board)
        if move is 'l':
            pos[0]=pos[0]
            pos[1]=pos[1]-1
        if move is 'r':
            pos[0]=pos[0]
            pos[1]=pos[1]+1
        if move is 'u':
            pos[0]=pos[0]-1
            pos[1]=pos[1]
        if move is 'd':
            pos[0]=pos[0]+1
            pos[1]=pos[1] 
        for i in range(len(board)):

            for j in range(len(board[i])):
                print(board[i][j],end='')
            print('')




    