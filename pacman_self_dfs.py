from copy import deepcopy

moves = [[-1,0],[0,-1],[0,1],[1,0]]
rows,columns = 0,0

def adj_nodes(grid,current_cor):
    adj = []
    for move in moves:
        print (move)
        print(move[0])
        print(current_cor['x'])
        adj_x,adj_y = current_cor['x']+move[0],current_cor['y']+move[1]
        if adj_x < 0 or adj_x >= rows or adj_y < 0 and adj_y >= columns:
            continue
        if grid[adj_x][adj_y] == '-' or grid[adj_x][adj_y] == '.':
            grid[adj_x][adj_y] = '='
            adj.append(dict(x=adj_x, y=adj_y))
    return adj

def dfs(grid,start_pos,end_pos):
    stack = [[start_pos, []]]
    path = None
    visited_nodes = [] 
    path = None #python equivalent of none
    while stack:
        current_cor , previous_path = stack.pop()
        visited_nodes.append(current_cor)
        current_path = deepcopy(previous_path)
        current_path.append(current_cor)

        if current_cor==end_pos:
            if path is None:
                path = current_path
                break
        stack += [[node,current_path] for node in adj_nodes(grid,current_cor)]
    return visited_nodes,path 




def main():
    pacman_row, pacman_column = map(int, input().strip().split())
    food_row, food_column = map(int, input().strip().split())
    global rows,columns
    rows,columns = map(int,input().strip().split())
    grid = []
    for _ in range(rows):
        grid.append(list(input().strip()))
        start_pos = dict(x=pacman_row,y=pacman_column)
        end_pos = dict(x=food_row,y=food_column)
        visited_nodes,final_path = dfs(grid,start_pos,end_pos)


    print(len(visited_nodes))
    for node in visited_nodes:
        print(node['x'], node['y'])

    print(len(final_path) - 1)
    for node in final_path:
        print(node['x'], node['y'])

if __name__ == '__main__':
    main()


