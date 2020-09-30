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
	checked = [ ]
	if tile >= 10 and tile <= 72:
		values = [-9, -8, -7, -1, 1, 7, 8, 9]
		test_values = [1, 8, 9]
		# checked = [ ]
		for n in values:
			for x in range(1, 9):
				check = tile+ n*x
				if check in set1 or check not in set2:
					break
				elif check in set2:
					checked.append(check)
	return(checked)

b_set = [38, 59, 71]
w_set = [36, 37, 43, 44, 51, 53, 62, 39]

a = (check_valid(35, b_set, w_set))
print(a)
print(len(a))
b = (check_valid(59, b_set, w_set))
print(b)
print(len(b))
c = (check_valid(40, b_set, w_set))
print(c)
print(len(c))