import pygame
from logic import *
from pygame.locals import *

#constants
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
TILE_SIZE = 64

grid_pieces = [ ]

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

def adjust_centre(n, s):
	"""pygame blits/draws from the top left on an x, y coordinate, not the centre,
	this function adjusts for this so I can just type in the centre coordinates"""
	return(n - s/2)

print(adjust_centre(48, 48))

def draw_grid():
	bg = (255, 255, 255)
	screen.fill(bg)
	"""creates an 8 x 8 grid for the othello game"""
	for n in range(1, 8):
		pygame.draw.line(screen, (0, 0, 0), (0, n * TILE_SIZE), (SCREEN_WIDTH, n * TILE_SIZE)) 
		pygame.draw.line(screen, (0, 0, 0), (n * TILE_SIZE, 0), (n * TILE_SIZE, SCREEN_HEIGHT))
		#following draws two starting black and two starting white pieces
		screen.blit(black, ((TILE_SIZE*4.5 - 24), (TILE_SIZE*3.5 - 24)))
		screen.blit(black, ((TILE_SIZE*3.5 - 24), (TILE_SIZE*4.5 - 24)))
		screen.blit(white, ((TILE_SIZE*3.5 - 24), (TILE_SIZE*3.5 - 24)))
		screen.blit(white, ((TILE_SIZE*4.5 - 24), (TILE_SIZE*4.5 - 24)))

running = True
while running:
	draw_grid()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#detects if a section of the board was selected, and if it was, then 
		#detects the position of the mouse
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x, y = pygame.mouse.get_pos()
			print(x, y)
		
		
	pygame.display.update()