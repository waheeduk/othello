def Grid_number(x, y):
	"""produces a grid number from 1 to 64, to represent the placement of the 
	othello pieces on the board"""
	out_a = x+1
	out_b = y*8
	return(out_a+out_b)

def get_position(n):
	"""produces a number between 0 and 7 for the position of the mouse
	for the x and y coordinates"""
	output = n//64
	return(output)

def get_Grid_number(x,y):
	"""transforms the x and y coordinates into the grid number"""
	out_x = get_position(x)
	out_y = get_position(y)
	grid_no = Grid_number(out_x, out_y)
	return(grid_no)