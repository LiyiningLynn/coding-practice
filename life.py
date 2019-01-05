#life

import numpy as np
from random import randint
def life(m,n):
	#initialize board randomly
	board = [[0]*n for i in range(m)]
	alive_count = [[0]*n for i in range(m)]
	for i in range(m):
		for j in range(n):
			board[i][j] = randint(0,1)
			#alive_count[i][j] = 0
	temp = list(board)
	print 'original board is :'
	for i in range(m):
		print board[i]
	print 'its copy temp is :'
	for i in range(m):
		print temp[i]
    #edges
    #for i in range(1,m-1):
    #get the set of neighbors of different cells
	for x in range(m):
		for y in range(n):
			if x == 0 and y!=0 and y != n-1:
            #upper
				neighbor = [board[x][y-1],board[x+1][y-1],board[x+1][y],board[x+1][y+1],board[x][y+1]]
			elif x==m-1 and y!=0 and y!=n-1:
    	    #low
				neighbor = [board[x][y-1],board[x-1][y-1],board[x-1][y],board[x-1][y+1],board[x][y+1]]
			elif y==0 and x!=0 and x!=m-1:
    	    #left
				neighbor = [board[x-1][y],board[x-1][y+1],board[x][y+1], board[x+1][y+1],board[x+1][y]]
			elif y==n-1 and x!=0 and x!=m-1:
    	    #right
				neighbor = [board[x-1][y],board[x-1][y-1],board[x][y-1],board[x+1][y-1],board[x+1][y]]
			elif 0<x<m-1 and 0<y<n-1:
    	    #middle
				neighbor = [board[x-1][y-1],board[x-1][y],board[x-1][y+1],board[x][y+1],board[x+1][y+1],board[x+1][y],board[x+1][y-1],board[x][y-1]]
			elif x == 0 and y == 0:
				neighbor = [board[0][1], board[1][0], board[1][1]]
			elif x == m-1 and y == n-1:
				neighbor = [board[m-2][n-1], board[m-1][n-2], board[m-2][n-2]]
			elif x==0 and y==n-1:
				neighbor = [board[0][n-2], board[1][n-1], board[1][n-2]]
			elif x==m-1 and y==0:
				neighbor = [board[m-2][0], board[m-1][1], board[m-2][1]]
			else:
				neighbor = None

			#alive_count[x][y] = len(np.nonzero(neighbor))#error !!!
			for i in range(len(neighbor)):
				if neighbor[i] != 0:
					alive_count[x][y] +=1#now the alive_count is correct
	print 'alive_count matrix is :'
	#print 'neighbor of board[1][1]',
	for i in range(m):
		print alive_count[i]
    
	for i in range(m):
		for j in range(n):
			if board[i][j] == 1:
				if alive_count[i][j] < 2:
					temp[i][j]=0
				elif alive_count[i][j] > 3:
					temp[i][j]=0
    			elif alive_count[i][j] == 2:
    				temp[i][j] = 1
    			elif alive_count[i][j] == 3:
    				temp[i][j] = 1
				
			elif board[i][j] == 0:
				if alive_count[i][j] == 3:
					temp[i][j] = 1
    			else:
    				temp[i][j] = 0

	for i in range(m):
		for j in range(n):
			board[i][j] = temp[i][j]

	print 'after one round:'
	for i in range(m):
		print board[i]

#m,n = tuple(input('please input row and col'))
life(4,4)

