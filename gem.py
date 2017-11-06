from copy import deepcopy

MOVES = [[-1, 0],[1,1],[-1,-1],[-1,1],[1,-1],[0, -1],[0, 1],[1, 0]]
ROWS, COLUMNS = 0, 0

def move_next(grid, coordinate):
    next_moves = []
    for move in MOVES:
        next_x, next_y = coordinate['x'] + move[0], coordinate['y'] + move[1]
        if next_x < 0 or next_x >= ROWS or next_y < 0 and next_y >= COLUMNS:
            continue
        if grid[next_x][next_y] == '0' or grid[next_x][next_y] == '1':
            next_moves.append(dict(x=next_x, y=next_y))
    return next_moves

def bfs(grid, source, goal):
    queue = [[source, []]]
    nodes_explored, path = [], None
    while queue:
        coordinate, previous_path = queue.pop(0)
        current_path = deepcopy(previous_path)
        current_path.append(coordinate)
        nodes_explored.append(coordinate)
        if coordinate == goal:
            if path is None:
                path = current_path
                break
        queue += [[node, current_path] for node in move_next(grid, coordinate)]
    return nodes_explored, path

def main():

    global ROWS, COLUMNS
    flag=0
    ROWS, COLUMNS = map(int, input().strip().split())

    grid = []
    for _ in range(ROWS):
        grid.append(list(input().strip()))
    
    for i in range(len(grid)):

        for j in range(len(grid[i])):

            if grid[i][j] == "1":
                food_row=i
                food_column=j
                flag=1
                break
        if flag==1 :
            break
    pacman_row, pacman_column = map(int, input().strip().split())

    
    source = dict(x=pacman_row, y=pacman_column)
    goal = dict(x=food_row, y=food_column)
    nodes_explored, path = bfs(grid, source, goal)


    print(len(path) - 1)
    for node in path:
        print(node['x'], node['y'])

if __name__ == '__main__':
    main()