board = [[0,0,0,4,0,0,1,2,0],
	 [0,0,0,0,7,5,0,0,9],
	 [0,0,0,6,0,1,0,7,8],
	 [0,0,7,0,4,0,2,6,0],
	 [0,0,1,0,5,0,9,3,0],
	 [9,0,4,0,6,0,0,0,5],
	 [0,7,0,3,0,0,0,1,2],
	 [1,2,0,0,0,7,4,0,0],
	 [0,4,9,2,0,6,0,0,7]]


def print_board():
	global board
	for i in range(len(board)):
		# Print "-" every 3 rows
		if i % 3 == 0 and i != 0:
			print('- - - - - - - - - - - -')

		for j in range(len(board)):
			# Print "|" every 3 columns
			if j % 3 == 0 and j != 0:
				print(' | ', end = '')
			
			# Print number in (i, j)
			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + ' ', end = '')
	return ''


def possible(x, y, n):
	global board

	# Reads through [y][i] horizontal row.
	for i in range(len(board)):
		if board[x][i] == n:
			#print(f'{n} is already in row {x}')
			return False
	
	# Reads through vertical column
	for i in range(len(board)):
		if board[i][y] == n:
			#print(f'{n} is already in column {y}')
			return False

	box_x = (x//3)*3
	box_y = (y//3)*3

	# Checks if {n} it is in the box.
	for i in range(0,3):
		for j in range(0,3):			
			if board[box_x+i][box_y+j] == n:
				# print(f'{n} is already in box ({box_x}, {box_y})')
				return False

	return True


def solve():
	global board

	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				
				for n in range(1, 10):
					if possible(i, j, n):
						board[i][j] = n
						solve()
						board[i][j] = 0
				return
	
	print(f'-------------------------\nSolved board:')
	print_board()

print('Board to solve:')
print_board()
solve()
