#just a small file where i test out some python ideas and concepts before
#implementing them in the code proper

def reset_board(set1, set2):
	"""resets the entire board to the starting state"""
	set1.clear()
	set2.clear()
	set1.extend([29, 36])
	set2.extend([28, 37])

black_tiles = [35, 62, 38]
white_tiles = [44, 53, 36, 37]

def check_valid(tile):
	values = [-1, 1, -7, -8, -9, 7, 8, 9]
	valid = False
	for n in values:
		checked = tile + n
		if checked in white_tiles:
			valid = True
	return(valid)

# for n in range(35, 80, 9):
# 	print(n)
flip_list = [ ]

def flipped(tile, diff, seta, setb):
	valid = False
	for n in range(0, 80, 9):
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

print(flipped(35, 9, black_tiles, white_tiles))
print('the flip list is')
print(flip_list)

for x in range(2,9):
	print(x)