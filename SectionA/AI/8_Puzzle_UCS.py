from queue import PriorityQueue 
import copy

class State :
	def __init__ ( self , new_grid ) :
		self.grid = [ [ 0 for i in range(0,3) ] for i in range ( 0,3 ) ] ;
		it = 0 ;
		for i in range ( 0 , 3 ) :
			for j in range ( 0 , 3 ) :
				self.grid[i][j] = new_grid[it] ;
				it = it+1 ;
		self.parent = [ [0 for i in range(0,3)] for i in range ( 0,3) ] ;

	def assign_parent ( self , parent_state ) :
		self.parent = parent_state ;

def getList ( current_grid ) :
	lis = [] ;
	for i in range ( 0,3 ) :
		for j in range ( 0,3 ) :
			lis.append( current_grid[i][j] ) ;
	return lis ;

def hashed ( state1 ) :
	temp = "" ;
	for i in range ( 0 , 3 ) :
		for j in range ( 0 , 3 ) :
			temp = temp + str( state1.grid[i][j] ) ;
	return temp ;

def get_reverseHash ( hash_val ) :
	ind = 0 ;
	return_grid = [ [ 0 for i in range(0,3) ] for i in range ( 0,3 ) ] ;
	for i in range ( 0 , 3 ) :
		for j in range ( 0 , 3 ) :
			return_grid[i][j] = hash_val[ind] ;
			ind += 1 ;
	return return_grid ;

def isEqual ( state1 , state2 ) :
	for i in range ( 0,3 ) :
		for j in range ( 0,3 ) :
			if ( state1.grid[i][j] != state2.grid[i][j] ) :
				return False ;
	return True ;

def bfs ( src ) :
	cnter = int(1) ;
	q = PriorityQueue() ;
	q.put( [0, cnter , src] ) ;
	while ( q.empty() == False ) :
		temporary = q.get() ;
		thiscost = temporary[0] ;
		cur = temporary[2] ;
		if ( hashed(cur) == hashed( final_state ) ):
			return temporary ;
		if ( visited.get( hashed(cur) , 0 ) == 1 ) :
			continue ;
		visited[hashed(cur)] = 1 ;
		cur_grid = copy.deepcopy(cur.grid) ;
		#print ( cur_grid , end = '   ' ) ;
		zero_i = 0 ;
		zero_j = 0 ;
		for i in range ( 0,3 ) :
			for j in range ( 0 , 3 ) :
				if ( cur_grid[i][j] == '0' ) :
					zero_i = i ;
					zero_j = j ;
					break ;
		#print ( zero_i , zero_j , sep = ' ' ) ;
		if ( zero_i-1 >= 0 ) :
			temp_grid = State ( getList( cur_grid ) ) ;
			temp_grid.grid[zero_i-1][zero_j] = '0' ;
			temp_grid.grid[zero_i][zero_j] = cur_grid[zero_i-1][zero_j] ;
			temp_grid.assign_parent ( cur ) ;
			cnter += 1 ;
			q.put ( [upCost+thiscost , cnter , temp_grid] ) ;
		if ( zero_i+1 < 3 ) :
			temp_grid = State ( getList( cur_grid ) ) ;
			temp_grid.grid[zero_i+1][zero_j] = '0' ;
			temp_grid.grid[zero_i][zero_j] = cur_grid[zero_i+1][zero_j] ;
			temp_grid.assign_parent ( cur ) ;
			cnter += 1 ;
			q.put ( [downCost+thiscost , cnter , temp_grid] ) ;
		if ( zero_j-1 >= 0 ) :
			temp_grid = State ( getList( cur_grid ) ) ;
			temp_grid.grid[zero_i][zero_j-1] = '0' ;
			temp_grid.grid[zero_i][zero_j] = cur_grid[zero_i][zero_j-1] ;
			temp_grid.assign_parent ( cur ) ;
			cnter += 1 ;
			q.put ( [ leftCost+thiscost , cnter , temp_grid] ) ;
		if ( zero_j+1 < 3 ) :
			temp_grid = State ( getList( cur_grid ) ) ;
			temp_grid.grid[zero_i][zero_j+1] = '0' ;
			temp_grid.grid[zero_i][zero_j] = cur_grid[zero_i][zero_j+1] ;
			temp_grid.assign_parent ( cur ) ;
			cnter += 1 ;
			q.put ( [ rightCost+thiscost , cnter , temp_grid] ) ;

	return par ;

upCost = int(input("Enter up cost") ) ;
downCost = int(input("Enter down cost") ) ;
leftCost = int(input("Enter left cost") ) ;
rightCost = int(input("Enter right cost") ) ;
str1 = input( "Enter initial state ( in a single row ) " ) ;
lis = str1.split(' ') ;
initial_state = State ( lis ) ;
lis = [ '0' for i in range ( 0 , 9 ) ] ;
par = State ( lis ) ;
initial_state.assign_parent ( par ) ;
str1 = input ( "Enter final state ( in a single row )" ) ;
lis = str1.split(' ') ;
final_state = State ( lis ) ;
visited = {} ;
answered = bfs ( initial_state ) ;
print ( "Total Cost is " , answered[0] , sep = ' ' ) ;
answer = answered[2] ;
if ( isEqual ( answer , par ) ) :
	print ( "No Solution Found" ) ;
else :
	current = answer ;
	while ( not isEqual( current , par ) ) :
		print ( current.grid ) ;
		current = current.parent ;
