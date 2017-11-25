from queue import PriorityQueue

import copy

def isSafe ( cur , row , col ) :
	#same row
	i = col-1 ;
	while ( i >= 0 ) :
		for j in cur :
			if ( j[0] == row and j[1] == i ) :
				return False ;
		i = i-1 ;
	#same column
	i = row-1 ;
	while ( i >= 0 ) :
		for j in cur :
			if ( j[0] == i and j[1] == col ) :
				return False ;
		i = i-1 ;
	#same upper diagonal
	new_row = row-1 ;
	new_col = col-1 ;
	while ( new_row >= 0 and new_col >= 0 ) :
		for j in cur :
			if ( j[0] == new_row and j[1] == new_col ) :
				return False ;
		new_row = new_row - 1 ;
		new_col = new_col - 1 ;
	#same lower diagonal
	new_row = row+1 ;
	new_col = col-1 ;
	while ( new_row < n and new_col >= 0 ) :
		for j in cur :
			if ( j[0] == new_row and j[1] == new_col ) :
				return False ;
		new_row = new_row + 1 ;
		new_col = new_col - 1 ;
	return True ;

def NQueens() :
	q = PriorityQueue() ;
	for i in range(0,n) :
		temp = [] ;
		l = [] ;
		l.append(i) ;
		l.append(0) ;
		temp.append(l) ;
		q.put( [cost[i][0],temp] ) ;

	while ( q.empty() == False ) :
		cur = q.get() ;
		row = cur[1][-1][0] ;
		col = cur[1][-1][1] ;
		if ( col == n-1 ) :
			answers.put ( cur ) ;
			continue ;
		for i in range ( 0 , n ) :
			if ( isSafe ( cur[1] , i , col+1 ) ) :
				temp = copy.deepcopy( cur[1] ) ;
				lis = [] ;
				lis.append(i) ;
				lis.append(col+1) ;
				temp.append( lis ) ;
				q.put( [cur[0]+cost[i][col+1] , temp] ) ;

n = int ( input() ) ;
cost = [ [ 0 for i in range(0,n) ] for i in range(0,n) ] ;
hello = 100 ;
for i in range ( 0,n ) :
	for j in range ( 0 , n ) :
		cost[i][j] = hello ;
		hello -= 1 ;
answers = PriorityQueue() ;
NQueens() ;
print ( "Total Solutions = " , answers.qsize() , sep = ' ' ) ;
places = answers.get() ;
grid = [ [ 0 for i in range(0,n)] for i in range(0,n) ] ;
print("cost is - " , places[0] , sep=' ' ) ;
for i in places[1] :
	u = i[0] ; 
	v = i[1] ;
	grid[u][v] = 1 ;
for i in range ( 0 , n ) :
	for j in range ( 0 , n ) :
		print ( grid[i][j] , end = ' ' ) ;
	print ( end = '\n' ) ;