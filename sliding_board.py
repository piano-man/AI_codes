from copy import deepcopy

STACK, visited = None, None
N = 0

def row_rotate(state, row):
    state[row] = state[row][-1:] + state[row][:-1]

def column_rotate(state, column):
    saved = state[-1][column]
    for row in range(N - 2, -1, -1):
        state[row + 1][column] = state[row][column]
    state[0][column] = saved

def make_tuple(state):
    return tuple([tuple(row) for row in state])

def dfs(state, goal, depth):
    global STACK, visited
    if state == goal:
        if make_tuple(state) not in visited:
            visited.add(make_tuple(state))
            STACK += [state]
        return True
    
    if depth < 0:
        return False

    saved_state = deepcopy(state)
    for row in range(N):
        for rotation_units in range(N - 1):
            row_rotate(state, row)
            if dfs(state, goal, depth - 1):
                if make_tuple(state) not in visited:
                    visited.add(make_tuple(state))
                    STACK += [state]
                return True
        state = deepcopy(saved_state)

    for column in range(N):
        for rotation_units in range(N - 1):
            column_rotate(state, column)
            if dfs(state, goal, depth - 1):
                if make_tuple(state) not in visited:
                    visited.add(make_tuple(state))
                    STACK += [state]
                return True
        state = deepcopy(saved_state)
    return False

def iterative_deepening(source, goal):
    for depth in range(100):
        if dfs(source, goal, depth):
            return True
    return False

def print_state(state):
    print(' '.join([' '.join([str(state[row][column]) for column in range(N)]) for row in range(N)]))

def main():
    global N, STACK, visited
    t = int(input())
    for _ in range(t):
        STACK, visited = [], set()
        N = int(input())
        source = [list(map(int, input().strip().split())) for __ in range(N)]
        goal = [list(map(int, input().strip().split())) for __ in range(N)]
        if iterative_deepening(source, goal):
            path = STACK[::-1]
            for state in path:
                print_state(state)
        else:
            print(-1)

if __name__ == '__main__':
    main()