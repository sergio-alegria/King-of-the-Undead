"""
    Game developed by Alejandro Benitez, Raul Eguren and Sergio Alegria for the Computer Animation and Videogames lesson at the Universidad de Cantabria
    Contact Info:
    Sergio Alegria: sergiioalegriia@gmail.com
"""

import pygame
from Map import Map
import common
from Character import Character


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

#stores all the characters
characters = []
#store character images un a list
main_character_animations = {"Top_walk" : [],
                             "Top_walk_S" : [],
                             "Down_walk" : [],
                             "Down_walk_S" : [],
                             "Rside_walk" : [],
                             "Rside_walk_S" : [],
                             "Lside_walk_S" : [],
                             "Top_attack" : [],
                             "Down_attack" : [],
                             "Lside_attack" : [],
                             "Rside_attack" : [],
                             "Dying" : [],
                             "Stall" : []}

mobs_animations = {"Ghost" : [{"Down_walk" : [], 
                               "Top_walk" : [], 
                               "Rside_walk" : [],
                               "Lside_walk" : [],
                               "Dying" : []}],
                   "Goblin" : [{"Down_walk" : [], 
                                "Top_walk" : [], 
                                "Rside_walk" : [],
                                "Lside_walk" : [],
                                "Dying" : []}],
                   "Skeleton" : [{"Down_walk" : [], 
                                  "Top_walk" : [], 
                                  "Rside_walk" : [],
                                  "Lside_walk" : [],
                                  "Dying" : []}],
                   "Wizard" : [{"Down_walk" : [], 
                                "Top_walk" : [], 
                                "Rside_walk" : [],
                                "Lside_walk" : [],
                                "Dying" : []}]}
    
main_character_list = (8, 8, 8, 8, 8, 12, 8, 6, 6, 6, 6, 4, 1)
mobs_list = (2, 2, 2, 2, 1)

for i, j in zip(main_character_animations,main_character_list):
    for k in range(j):
        print(f'resources/Sprites pj/{i}/{i}-{k + 1}.png')
        img = pygame.image.load(f'resources/Sprites pj/{i}/{i}-{k + 1}.png').convert_alpha()
        img = pygame.transform.scale(img, (common.TILE_SIZE, common.TILE_SIZE))
        main_character_animations[i].append(img)


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
                for key, list in common.NEED_BAKGROUND.items():
                    #print(key, list)
                    if tile in list:
                        screen.blit(img_list[key], (i * TILE_SIZE - base_x, j * TILE_SIZE - base_y))     
                screen.blit(img_list[tile], (i * TILE_SIZE - base_x, j * TILE_SIZE - base_y))

FRAMES_PER_IMAGE = 5
frame_counter = 0
def draw_characters():
    global frame_counter
    frame_counter += 1
    for c in characters:
        #print(c.image)
        screen.blit(c.image, (c.pos.x, c.pos.y))
        if frame_counter == FRAMES_PER_IMAGE: 
            c.update()
            frame_counter = 0

base_x = 0
base_y = 0
def main():
    global base_x, base_y
    run = True
    map_test = Map(2)
    draw_map(map=map_test)
    
    characters.append(Character(0,10,[common.DISPLAY_COLS//2*TILE_SIZE, common.DISPLAY_ROWS//2*TILE_SIZE], 1, main_character_animations))
    #Display variables 
    scroll_left = False
    scroll_right = False
    scroll_up = False
    scroll_down = False
    while run:
        clock.tick(FPS)
        #draw_bg()
        base_x = characters[0].pos.x
        base_y = characters[0].pos.y
        
        # movement management
        if scroll_left is True and base_x > 0:
            characters[0].move(common.Dir.left)
        if scroll_right is True and base_x < common.MAX_COLS*TILE_SIZE:
            characters[0].move(common.Dir.right)
        if scroll_up is True and base_y > 0:
            characters[0].move(common.Dir.down)
        if scroll_down is True and base_y < common.DISPLAY_ROWS*TILE_SIZE:
            characters[0].move(common.Dir.up)
        
        if not (scroll_down or scroll_right or scroll_left or scroll_up):
            characters[0].move(common.Dir.stall)
        # Draw the map
        screen.fill(BLACK)
        draw_map(map=map_test, x=int(base_x), y=int(base_y))
        draw_characters()
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

        #print(f'{base_x = }\t{base_y = }')
        pygame.display.update()

if __name__ == "__main__":
    print("Welcome to Game of the Undead")
    main()