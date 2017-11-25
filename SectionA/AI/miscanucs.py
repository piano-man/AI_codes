from queue import PriorityQueue

def valid(leftc, leftm, rightc, rightm):
    if (leftc >= 0 and leftm >= 0 and rightm >= 0 and rightc >= 0 and (leftm == 0 or leftm >= leftc) and (
            rightm == 0 or rightm >= rightc) and leftc <= 3 and leftm <= 3 and rightm <= 3 and rightc <= 3):
        return 1
    else:
        return 0

def findnextlevel(state):
    nextp = []
    lm = state[2]
    lc = state[1]
    boat = state[3]
    rm = 3 - lm
    rc = 3 - lc
    costlm = 2
    costlc = 5
    costrc = 7
    costrm = 3
    if(boat == 'L'):
        if(valid(lc - 1, lm, rc + 1, rm)):
            cost = costlc
            nextp.append([cost, lc - 1, lm, 'R'])
        if (valid(lc - 2, lm, rc + 2, rm)):
            cost = costlc * 2
            nextp.append([cost, lc - 2, lm, 'R'])
        if (valid(lc, lm - 1, rc, rm + 1)):
            cost = costlm
            nextp.append([cost, lc, lm - 1, 'R'])
        if (valid(lc, lm - 2, rc, rm + 2)):
            cost = costlm * 2
            nextp.append([cost, lc, lm - 2, 'R'])
        if (valid(lc - 1, lm - 1, rc + 1, rm + 1)):
            cost = costlm + costlc
            nextp.append([cost, lc - 1, lm - 1, 'R'])
    else:
        if (valid(lc + 1, lm, rc - 1, rm)):
            cost = costrc
            nextp.append([cost, lc + 1, lm, 'L'])
        if (valid(lc + 2, lm, rc - 2, rm)):
            cost = costrc * 2
            nextp.append([cost, lc + 2, lm, 'L'])
        if (valid(lc, lm + 1, rc, rm - 1)):
            cost = costrm
            nextp.append([cost, lc, lm + 1, 'L'])
        if (valid(lc, lm + 2, rc, rm - 2)):
            cost = costrm * 2
            nextp.append([cost, lc, lm + 2, 'L'])
        if (valid(lc + 1, lm + 1, rc - 1, rm - 1)):
            cost = costrc + costrm
            nextp.append([cost, lc + 1, lm + 1, 'L'])
    return (tuple(tuple(x) for x in nextp))

def solve(parent):
    q = PriorityQueue();
    #print("1")
    visited = set()
    q.put((0, 3 ,3, 'L'))
    visited.add((0, 3, 3, 'L'))
    parent[(0, 3, 3, 'L')] = (-1, -1, -1, 'N')
    goal = (100, 0, 0, 'R')

    while(not q.empty()):
        state = q.get()
        if(state[1:] == goal[1:]):
            return state[0]
        nextlevel = findnextlevel(state)
        for x in nextlevel:
            if x not in visited:
                #print(x, state)
                q.put(x)
                visited.add(x)
                parent[x] = state
                if(x[1:] == goal[1:]):
                    return x[0]
    return 0

def printsol(parent, state):
    if(parent[state] == (-1, -1, -1, 'N')):
        print(state[1:])
        return
    printsol(parent, parent[state])
    print(state[1:])

def main():
    parent = {}
    ans = solve(parent)
    if not ans == 0:
        #print(parent)
        printsol(parent, (ans, 0, 0, 'R'))
    else:
        print("Solution does not exist")

if __name__ == "__main__":
    main()