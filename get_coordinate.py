def get_coordinates(n, factor, offset):
	"""produces an x and y value, based upon an 8x8 grid, numbered from left
	to right, top to bottom, starting at 1 and ending at 64. This value 
	expressed from 0 to 7, is then multiplied by a factor dependent on the 
	pixels per each tile in the game"""
	if n % 8 == 0:
		x = (7* factor)+offset
		y = ((n / 8) - 1)*factor + offset
	else:
		x = ((n % 8) - 1)*factor+offset
		y = (n // 8)*factor + offset
	
	return(x, y)
