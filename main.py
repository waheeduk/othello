from get_coordinate import get_coordinates
from check_validity import check_valid, flip_list, flip, check_valid_two, recursive_check
from start_reset import reset_board
import random
from datetime import datetime
from logic import *
import pygame
from pygame.locals import *

#constants
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
TILE_SIZE = 64

pygame.init()
pygame.display.set_caption('OTHELLO')
clock = pygame.time.Clock()

# create a surface on screen that has the size of 512 x 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#images
black = pygame.image.load('art/black.png')
white = pygame.image.load('art/white.png')

#sound effects
piece = pygame.mixer.Sound('art/piece.wav')

#lists containing tiles placed into the game board, represented by grid numbers,
#in addition to the 4 starting pieces in othello
black_tiles = [29, 36]
white_tiles = [28, 37]

#keeps track of whose turn it is, 1 is the player, 2 is the computer
turn = 2
player = 2



def draw_grid():
	bg = (255, 255, 255)
	screen.fill(bg)
	"""creates an 8 x 8 grid for the othello game"""
	for n in range(1, 8):
		pygame.draw.line(screen, (0, 0, 0), (0, n * TILE_SIZE), (SCREEN_WIDTH, n * TILE_SIZE)) 
		pygame.draw.line(screen, (0, 0, 0), (n * TILE_SIZE, 0), (n * TILE_SIZE, SCREEN_HEIGHT))
		#following draws two starting black and two starting white pieces
		for n in black_tiles:
			screen.blit(black, get_coordinates(n, TILE_SIZE, 8))
		for n in white_tiles:
			screen.blit(white, get_coordinates(n, TILE_SIZE, 8))


running = True
while running:
	draw_grid()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#detects if a section of the board was selected, and if it was, then 
		#detects the position of the mouse
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
			turn % player  == 0:
			#need to check if move is valid before increasing turn counter
			#and before placing tiles
			x, y = pygame.mouse.get_pos()
			selected = get_Grid_number(x, y)
			check_valid_two(selected, black_tiles, white_tiles)
			if len(flip_list) >= 1:
				if selected not in black_tiles:
					for captured in flip_list:
						if captured != selected:
							print(f'captured are {captured}')
							flip(captured, black_tiles, white_tiles)
							print(captured)
					black_tiles.append(selected)
					turn += 1
					print(f'after black go turn is ')
					flip_list.clear()
					print(f'after clearing fliplist is {flip_list}')
					print('\n')
			#if it is not valid then clear thfe flip list
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and \
			turn % player == 1:
			#need to check if move is valid before increasing turn counter
			#and before placing tiles
			x, y = pygame.mouse.get_pos()
			selected = get_Grid_number(x, y)
			check_valid_two(selected, white_tiles, black_tiles)
			if len(flip_list) >= 1:
				if selected not in white_tiles:
					for captured in flip_list:
						if captured != selected:
							print(f'captured are {captured}')
							flip(captured, white_tiles, black_tiles)
					white_tiles.append(selected)
					turn += 1
					flip_list.clear()
					print(f'after clearing fliplist is {flip_list}')
		if event.type == pygame.KEYDOWN:
			 if event.key == pygame.K_r:
				 reset_board(black_tiles, white_tiles)

	pygame.display.update()