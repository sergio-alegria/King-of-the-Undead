import pygame
from GUI import Button
from World import Map, Tile

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Level Editor")

map = Map(0) # Map object

#moving the map variables
scroll = 0  # Horizontal Offset 
scroll_speed = 1 # Base scroll speed
scroll_dir={"L" : False, "R" : False}

def draw_grid():
  # Vertical lines
	for c in range(Map.COLS + 1):
		pygame.draw.line(screen, pygame.WHITE, (c * Tile.TILE_SIZE - scroll, 0), (c * Tile.TILE_SIZE - scroll, SCREEN_HEIGHT))
	# Horizontal lines
	for c in range(Map.ROWS + 1):
		pygame.draw.line(screen, pygame.WHITE, (0, c * Tile.TILE_SIZE), (SCREEN_WIDTH, c * Tile.TILE_SIZE))

# Load button images
Utility_Buttons = {
  "LOAD" : Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, "button_load"), 
  "SAVE" : Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 50, "button_save")
}

# List with Tile Buttons
Tile_Buttons = []
button_col = 0
button_row = 0
# Import all the tiles and create a button for each
for x in range(Tile.TILE_TYPES):
	Tile_Buttons.append(Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, x))
	button_col += 1
	if button_col == 3:
		button_row += 1
		button_col = 0


run = True
while run:

  clock.tick(FPS)

  for event in pygame.event.get():
	  if event.type == pygame.QUIT:
		  run = False

  pygame.display.update()


pygame.quit()








