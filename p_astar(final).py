from copy import deepcopy
from operator import itemgetter

MOVES = [[-1, 0],[0, -1],[0, 1],[1, 0]]
ROWS, COLUMNS = 0, 0
goal = dict()

def move_next(grid, coordinate):
    next_moves = []
    for move in MOVES:
        next_x, next_y = coordinate['x'] + move[0], coordinate['y'] + move[1]
        if next_x < 0 or next_x >= ROWS or next_y < 0 and next_y >= COLUMNS:
            continue
        if grid[next_x][next_y] == '-' or grid[next_x][next_y] == '.':
            grid[next_x][next_y] = '='
            next_moves.append(dict(x=next_x, y=next_y))
    next_moves.sort(key=lambda x: get_cost(x))
    print(next_moves)
    return next_moves

def get_cost(n1):
    global goal
    #print(goal)
    #print(n1)
    return abs(n1['x']-goal['x'])+abs(n1['y']-goal['y'])

def a_star(grid, source, goal):
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
    pacman_row, pacman_column = map(int, input().strip().split())
    food_row, food_column = map(int, input().strip().split())
    global ROWS, COLUMNS
    ROWS, COLUMNS = map(int, input().strip().split())
    global goal
    grid = []
    for _ in range(ROWS):
        grid.append(list(input().strip()))

    source = dict(x=pacman_row, y=pacman_column)
    goal = dict(x=food_row, y=food_column)
    nodes_explored, path = a_star(grid, source, goal)

    print(len(nodes_explored))
    for node in nodes_explored:
        print(node['x'], node['y'])

    print(len(path) - 1)
    for node in path:
        print(node['x'], node['y'])

if __name__ == '__main__':
    main()