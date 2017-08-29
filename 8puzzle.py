goal_state = [1, 4, 7, 2, 5, 8, 3, 6, 0]

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
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 3, 6]:
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_down( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [2, 5, 8]:
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_left( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 1, 2]:
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_right( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [6, 7, 8]:
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	return expanded_nodes

def bfs( start, goal ):

	nodes = []
	
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:

		if len( nodes ) == 0: return None

		node = nodes.pop(0)

		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth == 1: break
				temp = temp.parent
			return moves				

		nodes.extend( expand_node( node, nodes ) )

def dfs( start, goal, depth=10 ):

	depth_limit = depth

	nodes = []

	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:

		if len( nodes ) == 0: return None

		node = nodes.pop(0)
	
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth <= 1: break
				temp = temp.parent
			return moves				
		if node.depth < depth_limit:
			expanded_nodes = expand_node( node, nodes )
			expanded_nodes.extend( nodes )
			nodes = expanded_nodes

def ids( start, goal, depth=50 ):
	for i in range( depth ):
		result = dfs( start, goal, i )
		if result != None:
			return result

def a_star( start, goal ):
	nodes = []
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		if len( nodes ) == 0: return None
		nodes.sort( cmp )
		node = nodes.pop(0)
		print "Current state", node.state, " and move: ", node.operator
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert( 0, temp.operator )
				if temp.depth <=1: break
				temp = temp.parent
			return moves
		nodes.extend( expand_node( node, nodes ) )
		
def cmp( x, y ):
	return (x.depth + h( x.state, goal_state )) - (y.depth + h( y.state, goal_state ))

def h( state, goal ):
	score = 0
	for i in range( len( state ) ):
		if state[i] != goal[i]:
			score = score + 1
	return score

class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth
		self.cost = cost

def readfile( filename ):
	f = open( filename )
	data = f.read()
	data = data.strip( "\n" )
	data = data.split( " " )
	state = []
	for element in data:
		state.append( int( element ) )
	return state

# Main method
def main():
	starting_state = readfile( "state.txt" )
	print("starting")
	display_board(starting_state)
	print("final state")
	display_board(goal_state)
	result = bfs( starting_state, goal_state )
	if result == None:
		print "No solution found"
	elif result == [None]:
		print "Start node was the goal!"
	else:
		print result
		print "number of moves",len(result)

if __name__ == "__main__":
	main()