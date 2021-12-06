"""
    Game developed by Alejandro Benitez, Raul Eguren and Sergio Alegria for the Computer Animation and Videogames lesson at the Universidad de Cantabria
    Contact Info:
    Sergio Alegria: sergiioalegriia@gmail.com
"""

import pygame
from Map import Map
import common



#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
PURPLE = (150, 150, 200)
BLACK = (0, 0, 0)

pygame.init()

clock = pygame.time.Clock()
FPS = 60

TILE_SIZE = common.TILE_SIZE
# Display 16x16 tiles to the player
SCREEN_WIDTH = common.DISPLAY_COLS * TILE_SIZE
SCREEN_HEIGHT = common.DISPLAY_ROWS * TILE_SIZE
SIDE_MARGIN = 400


screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('King of the Undead')

TILE_TYPES = 44
#store tiles in a list
img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'resources/Tileset/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img = pygame.image.load('resources/Icons/save_btn.png').convert_alpha()
load_img = pygame.image.load('resources/Icons/load_btn.png').convert_alpha()


#create function for drawing background
def draw_bg():
	screen.fill(PURPLE)
	for y, row in enumerate(map):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[0], (x * TILE_SIZE, y * TILE_SIZE))

#function for drawing the world tiles
def draw_map(map, x=0, y=0):
    screen.fill(BLACK)
    for j, row in enumerate(map.grid):
        for i, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[tile], (i * TILE_SIZE - base_x, j * TILE_SIZE - base_y))

base_x = 0
base_y = 0
def main():
    global base_x, base_y
    run = True
    map_test = Map(1)
    draw_map(map=map_test)
    
    #Display variables 
    scroll_left = False
    scroll_right = False
    scroll_up = False
    scroll_down = False
    while run:
        clock.tick(FPS)
        #draw_bg()
        
        #scroll the map
        if scroll_left is True and base_x > 0:
            base_x -= common.speed
        if scroll_right is True and base_x < common.MAX_COLS*TILE_SIZE:
            base_x += common.speed
        if scroll_up is True and base_y > 0:
            base_y -=  common.speed
        if scroll_down is True and base_y < common.DISPLAY_ROWS*TILE_SIZE:
            base_y +=  common.speed
        
        # Draw the map
        screen.fill(BLACK)
        draw_map(map=map_test, x=int(base_x), y=int(base_y))
        
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    scroll_up = True
                if event.key == pygame.K_s:
                    scroll_down = True
                if event.key == pygame.K_a:
                    scroll_left = True
                if event.key == pygame.K_d:
                    scroll_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    scroll_up = False
                if event.key == pygame.K_s:
                    scroll_down = False
                if event.key == pygame.K_a:
                    scroll_left = False
                if event.key == pygame.K_d:
                    scroll_right = False

        print(f'{base_x = }\t{base_y = }')
        pygame.display.update()

if __name__ == "__main__":
    print("Welcome to Game of the Undead")
    main()