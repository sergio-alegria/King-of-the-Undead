import pygame
import csv

from GUI import button

pygame.init() #Initialice pygame
clock = pygame.time.Clock()
FPS = 60

#window attributes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640 #Needs to be a multiple of 64
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.set_caption("Map generator")

#define map variables
ROWS = 32
MAX_COL = 300
TILE_SIZE = 16 #16x16 Tile
TILE_TYPES = 8

level = 0
current_tile = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

world_data = [] #Store the world data

#Image variables
img_list = []


def draw_grid():
  #draw grid lines
  for c in range(MAX_COL + 1):
    pygame.draw.line(screen, pygame.WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
  for c in range(ROWS + 1):
    pygame.draw.line(screen, pygame.WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))

def draw_level(level: int):
  for y, row in enumerate(world_data):
    for x, tile in enumerate(row):
      if tile >= 0:
        screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))


#Main loop
run = True
while run:
  
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
 


pygame.quit()