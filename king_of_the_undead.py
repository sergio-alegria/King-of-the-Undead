"""
    Game developed by Alejandro Benitez, Raul Eguren and Sergio Alegria for the Computer Animation and Videogames lesson at the Universidad de Cantabria
    Contact Info:
    Sergio Alegria: sergiioalegriia@gmail.com
"""

import pygame
from Map import Map
from map_generator import draw_text

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Display 16x16 tiles to the player
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SIDE_MARGIN = 400

#Tilesize
MAX_DISPLAY_TILES = 24 
TILE_SIZE = SCREEN_WIDTH//MAX_DISPLAY_TILES

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
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



#function for drawing the world tiles
def draw_world(map, x, y):
    for row in map.diplayable_sub_matrix(x,y):
        for tile in row:
            screen.blit(img_list[tile], (x * TILE_SIZE, y * TILE_SIZE))
            

def main():
    run = True
    map_test = Map(0)
    while run:
        draw_world(map=map_test)
        pass 
        

if __name__ == "__main__":
    print("Welcome to Game of the Undead")
    main()