
from copy import deepcopy


MOVES = [[-1, 0],[0, -1],[0, 1],[1, 0]]
ROWS, COLUMNS = 0, 0

def move_next(grid, coordinate):
    next_moves = []
    for MOVE in MOVES:
        next_x, next_y = coordinate['x'] + MOVE[0], coordinate['y'] + MOVE[1]
        if next_x < 0 or next_x >= ROWS or next_y < 0 and next_y >= COLUMNS:
            continue
        if grid[next_x][next_y] == '-' or grid[next_x][next_y] == '.':
            grid[next_x][next_y] = '='
            next_moves.append(dict(x=next_x, y=next_y))
    return next_moves

def iterative_dfs(grid, source, goal):
    stack = [[source, []]]
    nodes_explored, path = [], None
    while stack:
        coordinate, previous_path = stack.pop()
        current_path = deepcopy(previous_path)
        current_path.append(coordinate)
        nodes_explored.append(coordinate)
        if coordinate == goal:
            if path is None:
                path = current_path
                break
        stack += [[node, current_path] for node in move_next(grid, coordinate)]
    return nodes_explored, path

def main():
    pacman_row, pacman_column = map(int, input().strip().split())
    food_row, food_column = map(int, input().strip().split())
    global ROWS, COLUMNS
    ROWS, COLUMNS = map(int, input().strip().split())

    grid = []
    for _ in range(ROWS):
        grid.append(list(input().strip()))

    source = dict(x=pacman_row, y=pacman_column)
    goal = dict(x=food_row, y=food_column)
    nodes_explored, path = iterative_dfs(grid, source, goal)

    print(len(nodes_explored))
    for node in nodes_explored:
        print(node['x'], node['y'])

    print(len(path) - 1)
    for node in path:
        print(node['x'], node['y'])

if __name__ == '__main__':
    main()