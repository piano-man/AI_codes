goal_state = [1, 8, 7, 2, 0, 6, 3, 4, 5]
#
# The code will read state from a file called "state.txt" where the format is
# as above but space seperated. i.e. the content for the goal state would be
# 1 8 7 2 0 6 3 4 5

### Code begins.
import sys

def display_board( state ):
    print "-------------"
    print "| %i | %i | %i |" % (state[0], state[3], state[6])
    print "-------------"
    print "| %i | %i | %i |" % (state[1], state[4], state[7])
    print "-------------"
    print "| %i | %i | %i |" % (state[2], state[5], state[8])
    print "-------------"
    
def move_up( state ):
    """Moves the blank tile up on the board. Returns a new state as a list."""
    # Perform an object copy
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [0, 3, 6]:
        # Swap the values.
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None (Pythons NULL)
        return None

def move_down( state ):
    """Moves the blank tile down on the board. Returns a new state as a list."""
    # Perform object copy
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [2, 5, 8]:
        # Swap the values.
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None.
        return None

def move_left( state ):
    """Moves the blank tile left on the board. Returns a new state as a list."""
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [0, 1, 2]:
        # Swap the values.
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move it, return None
        return None

def move_right( state ):
    """Moves the blank tile right on the board. Returns a new state as a list."""
    # Performs an object copy. Python passes by reference.
    new_state = state[:]
    index = new_state.index( 0 )
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None
        return None

def create_node( state, parent, operator, depth, cost ):
    return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
    return expanded_nodes

def bfs( start, goal ):

    """Performs a breadth first search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.
    nodes = []
    # Create the queue with the root node in it.
    nodes.append( create_node( start, None, None, 0, 0 ) )
    print("in bfs")
    #print((nodes.pop(0)))

    
    while True:

        # We've run out of states, no solution.
        
        if len( nodes ) == 0: 
            return None
        # take the node from the front of the queue
        node = nodes.pop(0)
        #print(len(nodes))
        # Append the move we made to moves
        # if this node is the goal, return the moves it took to get here.
        if node.state == goal:
            moves = []
            temp = node
            while True:
                print("inside while")
                print(temp)
                if((temp) is not None):
                    moves.insert(0, temp.operator)
                    if temp.depth == 1: 
                        break
                    temp = temp.parent
                return moves                
        # Expand the node and add all the expansions to the front of the stack
        nodes.extend( expand_node( node, nodes ) )
class Node:
    def __init__( self, state, parent, operator, depth, cost ):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

def readfile( filename ):
    f = open( filename )
    data = f.read()
    # Get rid of the newlines
    data = data.strip( "\n" )
    #Break the string into a list using a space as a seperator.
    data = data.split( " " )
    state = []
    for element in data:
        state.append( int( element ) )
    return state

# Main method
def main():
    starting_state = readfile( "state.txt" )
    display_board(starting_state)
    print("hello")
    ### CHANGE THIS FUNCTION TO USE bfs, dfs, ids or a_star
    result = bfs( starting_state, goal_state )
    if result == None:
        print "No solution found"
    elif result == [None]:
        print "Start node was the goal!"
    else:
        print result
        print len(result), " moves"

# A python-isim. Basically if the file is being run execute the main() function.
if __name__ == "__main__":
    main()