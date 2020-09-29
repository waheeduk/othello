#checks the validity of moves by the player and computer
def flip(n, set1, set2):
	"""if the piece n has been surrounded, flip it from one set to the other"""
	if n in set1:
		set1.remove(n)
		set2.append(n)
	elif n in set2:
		set2.remove(n)
		set1.append(n)

flip_list = [ ]

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
	valid = False
	if tile >= 10 and tile <= 72:
		values = [-9, -8, -7, -1, 1, 7, 8, 9]
		for n in values:
			if (n +tile) in set2:
				for x in range(1, 8):
					if (tile + (n*x)) in set1:
						valid = True
	# elif tile % 8 == 0:
	# 	values = [-9, -8, -7, -1, 1, 7, 8, 9]
	# 	for n in values:
	# 		checked = n + tile
	# 		if turn % 2 == 1:
	# 			if checked <=0 or checked >= 81:
	# 				continue
	# 			elif checked in set2:
	# 				valid = True
	# 				break
	# 			else:
	# 				valid = False
	# 		elif turn % 2 == 1:
	# 			if 0>= checked >= 81:
	# 				continue
	# 			elif checked in set1:
	# 				valid = True
	# 				break
	# 			else:
	# 				valid = False
	return(valid)
	

b_set = [25, 62]
w_set = [44, 53]