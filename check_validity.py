#checks the validity of moves by the player and computer
def flip(n, set1, set2):
	"""if the piece n has been surrounded, flip it from one set to the other"""
	if n in set1:
		set1.remove(n)
		set2.append(n)
	elif n in set2:
		set2.remove(n)
		set1.append(n)


def flipped(tile, diff, seta, setb):
	valid = False
	for n in range(0, 80, diff):
		print(tile+n)
		if (tile+n) in seta:
			print(tile+n)
			print('in set a')
			if tile+n != tile and tile in seta:
				valid = True
		elif tile+ n in setb:
			print(tile+n)
			print('in set b')
			flip_list.append(tile+n)
	return valid

def check_valid(tile, set1, set2):
	"""checks if a move is valid, taking in the grid number of the tile 
	selected, whether it is black or white's turn, and the set1/set2 which are
	the list of black tiles/white tiles"""
	checked = [ ]
	if tile >= 10 and tile <= 72:
		values = [-9, -8, -7, -1, 1, 7, 8, 9]
		# test_values = [1, 8, 9]
		# checked = [ ]
		for n in values:
			for x in range(1, 9):
				check = tile+ n*x
				if check in set1 or check not in set2:
					break
				elif check in set2:
					checked.append(check)
	return(checked)

flip_list = []

def recursive_check(tile, diff, set1, set2):
	""" uses recursion to find if the selected tile is correct, where tile is 
	the original tile chosen by the player, plus n times the diff, that
	is difference between the original tile and the adjacent tile, where n is 
	initially one """
	for n in range(1, 8):
		if tile + (n*diff) in set1:
			print(f'flipped tiles are {tile}')
			if tile not in flip_list:
				flip_list.append(tile)
			end = tile + (n*diff)
			print(f'n*diff is {n}*{diff} is {n*diff}')
			print(f'end tile is {end}')
			if end in flip_list:
				flip_list.remove(end)
				print('\n')
				print('end removed from flip list')
				print('flip list')
		elif tile + (n*diff) in set2:
			new_tile = (tile + n*diff)
			recursive_check(new_tile, diff, set1, set2)
		else:
			break
	print(f'flip list is {flip_list}')

def check_valid_two(tile, set1, set2):
	values = [-9, -8, -7, -1, 1, 7, 8, 9]
	for value in values:
		if tile + value in set2:
			print(tile)
			print(value)
			recursive_check((tile+value), value, set1, set2)