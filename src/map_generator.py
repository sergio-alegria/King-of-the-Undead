import pygame
import csv
import common, button

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LOWER_MARGIN = 100
SIDE_MARGIN = 825

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


#define game variables
TILE_SIZE = SCREEN_HEIGHT // common.ROWS

level = 0
current_tile = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


#store tiles in a list
img_list = []
for x in range(common.TILE_TYPES):
	img = pygame.image.load(f'resources/Tileset/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img = pygame.image.load('resources/Icons/save_btn.png').convert_alpha()
load_img = pygame.image.load('resources/Icons/load_btn.png').convert_alpha()


#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
PURPLE = (150, 150, 200)

#define font
font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(common.ROWS):
	r = [0] * common.MAX_COLS
	world_data.append(r)

#create ground
for tile in range(0, common.MAX_COLS):
	world_data[common.ROWS - 1][tile] = 0


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


#create function for drawing background
def draw_bg():
	screen.fill(PURPLE)	
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[0], (x * TILE_SIZE - scroll, y * TILE_SIZE))
	

#draw grid
def draw_grid():
	#vertical lines
	for c in range(common.MAX_COLS + 1):
		pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
	#horizontal lines
	for c in range(common.ROWS + 1):
		pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


#function for drawing the world tiles
def draw_world():
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))



#create buttons
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 75, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 75, load_img, 1)
#make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
	tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 15, 75 * button_row + 15, img_list[i], 1)
	button_list.append(tile_button)
	button_col += 1
	if button_col == 11:
		button_row += 1
		button_col = 0


def map_generator():
    global level, current_tile, scroll_left, scroll_right, scroll, scroll_speed, screen
    screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
    pygame.display.set_caption('Level Editor')
    scroll = 0
    try:
        with open(f'levels/level{level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)
    except Exception: 
        for x in range(common.ROWS):
            for y in range(common.MAX_COLS):
                world_data[x][y] = 0
    run = True
    while run:

        clock.tick(FPS)
        
        draw_bg()
        draw_grid()
        draw_world()

        draw_text(f'Level: {level}', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
        draw_text('Press W or S to change level', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)
        draw_text('Press A or D to scroll', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 30)

        #save data if clicked
        if save_button.draw(screen):
            with open(f'levels/level{level}_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter = ',')
                for row in world_data:
                    writer.writerow(row)

        #load data if clicked
        if load_button.draw(screen):
            scroll = 0
            try:
                with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter = ',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)
            except Exception: 
                for x in range(common.ROWS):
                    for y in range(common.MAX_COLS):
                        world_data[x][y] = 0  

        #draw tile panel and tiles
        pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

        #choose a tile
        button_count = 0
        for button_count, i in enumerate(button_list):
            if i.draw(screen):
                current_tile = button_count

        #highlight the selected tile
        pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

        #scroll the map
        if scroll_left == True and scroll > 0:
            scroll -= 5 * scroll_speed
        if scroll_right == True and scroll < (common.MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
            scroll += 5 * scroll_speed

        #add new tiles to the screen
        #get mouse position
        pos = pygame.mouse.get_pos()
        x = (pos[0] + scroll) // TILE_SIZE
        y = pos[1] // TILE_SIZE

        #check that the coordinates are within the tile area
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            #update tile value
            if pygame.mouse.get_pressed()[0] == 1:
                if world_data[y][x] != current_tile:
                    world_data[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                world_data[y][x] = -1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    level += 1
                    scroll = 0
                    try:
                        with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter = ',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                    except Exception: 
                        for x in range(common.ROWS):
                            for y in range(common.MAX_COLS):
                                world_data[x][y] = 0
                if event.key == pygame.K_s and level > 0:
                    level -= 1
                    scroll = 0
                    try:
                        with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                            reader = csv.reader(csvfile, delimiter = ',')
                            for x, row in enumerate(reader):
                                for y, tile in enumerate(row):
                                    world_data[x][y] = int(tile)
                    except Exception: 
                        for x in range(common.ROWS):
                            for y in range(common.MAX_COLS):
                                world_data[x][y] = 0 
                if event.key == pygame.K_a:
                    scroll_left = True
                if event.key == pygame.K_d:
                    scroll_right = True
                if event.key == pygame.K_LSHIFT:
                    scroll_speed = 5
                if event.key == pygame.K_ESCAPE:
                    return 


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    scroll_left = False
                if event.key == pygame.K_d:
                    scroll_right = False
                if event.key == pygame.K_LSHIFT:
                    scroll_speed = 1
        pygame.display.update()