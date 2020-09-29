import random

turn = 1

def reset_board(set1, set2):
	"""resets the entire board to the starting state, set1 must be black and
	set2 must be white"""
	set1.clear()
	set2.clear()
	set1.extend([29, 36])
	set2.extend([28, 37])