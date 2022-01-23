"""
    Game developed by Alejandro Benitez, Raul Eguren and Sergio Alegria for the Computer Animation and Videogames lesson at the Universidad de Cantabria
    Contact Info:
    Sergio Alegria: sergiioalegriia@gmail.com
"""
import pygame
from Map import Map
import common
from Character import Character, Point
import json

pygame.init()

clock = pygame.time.Clock()
FPS = 60

with open("enemies.json") as f:
    _enemies = json.load(f)

BLOCK_DOORS_THREASHOLD = FPS*2

# define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
PURPLE = (150, 150, 200)
BLACK = (0, 0, 0)



TILE_SIZE = common.TILE_SIZE

# Display 16x16 tiles to the player
SCREEN_WIDTH = common.DISPLAY_COLS * TILE_SIZE
SCREEN_HEIGHT = common.DISPLAY_ROWS * TILE_SIZE
SIDE_MARGIN = 400


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("King of the Undead")

# stores all the characters
characters: "list[Character]" = []

# store character images un a list
main_character_animations = {
    "Top_walk": [],
    "Top_walk_S": [],
    "Down_walk": [],
    "Down_walk_S": [],
    "Rside_walk": [],
    "Rside_walk_S": [],
    "Lside_walk_S": [],
    "Top_attack": [],
    "Down_attack": [],
    "Lside_attack": [],
    "Rside_attack": [],
    "Dying": [],
    "Stall": [],
}

mobs_animations = {
    "Ghost": {
        "Down_walk": [],
        "Top_walk": [],
        "Rside_walk": [],
        "Lside_walk": [],
        "Dying": [],
        "Stall": [],
    },
    "Goblin": {
        "Down_walk": [],
        "Top_walk": [],
        "Rside_walk": [],
        "Lside_walk": [],
        "Dying": [],
        "Stall": [],
    },
    "Skeleton": {
        "Down_walk": [],
        "Top_walk": [],
        "Rside_walk": [],
        "Lside_walk": [],
        "Dying": [],
        "Stall": [],
    },
    "Wizard": {
        "Down_walk": [],
        "Top_walk": [],
        "Rside_walk": [],
        "Lside_walk": [],
        "Dying": [],
        "Stall": [],
    },
}
MOB_ANIMATION_TYPES = [
    "Down_walk",
    "Top_walk",
    "Rside_walk",
    "Lside_walk",
    "Dying",
    "Stall",
]
main_character_list = (8, 8, 8, 8, 8, 12, 8, 6, 6, 6, 6, 4, 1)

for i, j in zip(main_character_animations, main_character_list):
    for k in range(j):
        img = pygame.image.load(f"resources/Sprites_pj/{i}/{i}-{k + 1}.png").convert_alpha()
        img = pygame.transform.scale(img, (common.TILE_SIZE, common.TILE_SIZE))
        main_character_animations[i].append(img)

for key, mob_dict in mobs_animations.items():
    for count, type in enumerate(MOB_ANIMATION_TYPES):
        num_files = 2 if count < 4 else 1
        for i in range(num_files):
            img = pygame.image.load(
                f"resources/Sprites_mobs/{key}/{type}/{type}-{i+1}.png"
            ).convert_alpha()
            img = pygame.transform.scale(img, (common.TILE_SIZE, common.TILE_SIZE))
            mobs_animations[key][type].append(img) 


# store tiles in a list
img_list = []
for x in range(common.TILE_TYPES):
    img = pygame.transform.scale(pygame.image.load(f"resources/Tileset/{x}.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
    
save_img = pygame.image.load("resources/Icons/save_btn.png").convert_alpha()
load_img = pygame.image.load("resources/Icons/load_btn.png").convert_alpha()


# create function for drawing background
def draw_bg():
    """
    """
    screen.fill(PURPLE)
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[0], (x * TILE_SIZE, y * TILE_SIZE))


# function for drawing the world tiles
def draw_map(map : Map):
    """
        Displays the map tiles
        
        :param map: Map to be displayed
    """
    screen.fill(BLACK)
    for j, row in enumerate(map.grid):
        for i, tile in enumerate(row):
            if tile >= 0:
                for key, list in common.NEED_BAKGROUND.items():
                    if tile in list:
                        screen.blit(img_list[key],(i * TILE_SIZE, j * TILE_SIZE))
                screen.blit(img_list[tile], (i * TILE_SIZE, j * TILE_SIZE))

FRAMES_PER_IMAGE = 5
frame_counter = 0

SPEED_RUN_MUL = 1.75

dead_enemies : "dict[int, list[int]]" = {0 : []}
def draw_characters(map : Map):
    """
        Draws all the characters in the given map
        
        :param map: Current level/map
    """
    global frame_counter, dead_enemies
    
    frame_counter += 1
    if frame_counter >= FRAMES_PER_IMAGE:
        characters[0].update()
        frame_counter = 0
        
    # Display main character
    screen.blit(characters[0].image, (characters[0].pos.x, characters[0].pos.y))
    
    for c in characters[1:]:
        if c.AI_move(characters[0], map):
            die = characters[0].receive_dmg(c.weapon.dmg)
            if die:
                characters.remove(characters[0])
                print("GAME OVER!!")
                dead_enemies = {0 : []}
                return True
        if frame_counter >= FRAMES_PER_IMAGE:
            c.update()
            frame_counter = 0
        # Display enemy
        screen.blit(c.image, (c.pos.x, c.pos.y))
        # Enemy health bar
        pygame.draw.rect(screen,(0,0,0),(c.pos.x, c.pos.y - common.TILE_SIZE*0.5, common.HEALTH_BAR_WIDTH, common.HEALTH_BAR_HEIGHT))
        pygame.draw.rect(screen,(255,0,0),(c.pos.x, c.pos.y - common.TILE_SIZE*0.5 ,c.hp*common.HEALTH_BAR_WIDTH / c.max_hp, common.HEALTH_BAR_HEIGHT))
    # Player helth bar
    pygame.draw.rect(screen,(0,0,0),(characters[0].pos.x, characters[0].pos.y - common.TILE_SIZE*0.5, common.HEALTH_BAR_WIDTH, common.HEALTH_BAR_HEIGHT))
    pygame.draw.rect(screen,(0,255,0),(characters[0].pos.x, characters[0].pos.y - common.TILE_SIZE*0.5 ,characters[0].hp*common.HEALTH_BAR_WIDTH / characters[0].max_hp, common.HEALTH_BAR_HEIGHT))
    return False
 
def atack_enemies_in_range(character, direction, map_id):
    """
        Check if the atack can hit any enemie based on the weapon's range and hits them
    """
    for e in characters[1:]:
        if e.image.get_rect(center=e.pos.toTuple()).colliderect(character.weapon.get_rect(character.pos.toTuple(), direction)):
            die = e.receive_dmg(character.weapon.dmg)
            if die:
                characters.remove(e)
                dead_enemies[map_id].append(e.id)


def load_map_enemies(map_id : int):
    """
        Loads the enemies for the given map_id
        
        :param map_id: Identifier of the map/level 
    """
    with open("enemies.json", "r") as file:
        data = json.load(file)
        
    try:
        for i, c in enumerate(data[str(map_id)]):
            if i not in dead_enemies[map_id]:
                characters.append(Character(i, common.ENEMIES_HP[c['Type']],[c['i']*TILE_SIZE, c['j']*TILE_SIZE], mobs_animations[c["Type"]]))
    except Exception: 
        pass                 
       
base_x = 0
base_y = 0


def main():
    global base_x, base_y, characters, screen
    base_x = 0
    base_y = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("King of the Undead")
    
    attack = False
    run = True
    map = Map(19)
    characters = [Character(0, 200, [10 * TILE_SIZE, 8 * TILE_SIZE,],main_character_animations)]
    draw_map(map=map)
    
    # Display variables
    scroll_left = False
    scroll_right = False
    scroll_up = False
    scroll_down = False
    block_doors = 0
    while run:
        clock.tick(FPS)
        # draw_bg()
        base_x = characters[0].pos.x
        base_y = characters[0].pos.y
        
        prev_pos: Point = characters[0].pos
        # movement management
        if scroll_left is True:
            characters[0].move(common.Dir.left, map)
        if scroll_right is True:
            characters[0].move(common.Dir.right, map)
        if scroll_up is True:
            characters[0].move(common.Dir.down, map)
        if scroll_down is True:
            characters[0].move(common.Dir.up, map)
         
        if block_doors: 
            block_doors += 2
        if block_doors > BLOCK_DOORS_THREASHOLD:
            block_doors = 0
            
        # Check if door
        door : common.Door = map.check_door(*characters[0].pos.toMatrixIndex(), map.level)
        if door and not block_doors:
            block_doors = 1
            # Change map
            characters[0].pos = door.toPoint()
            for c in characters[1:]: characters.remove(c)
            map = Map(door.map_id)
            if door.map_id not in dead_enemies:
                dead_enemies[door.map_id] = []
            load_map_enemies(door.map_id)
            
        # Dont move if nor accesible
        if map.getTile(characters[0].pos) not in common.FLOOR:
            characters[0].pos = prev_pos
        if not (scroll_down or scroll_right or scroll_left or scroll_up):
            characters[0].move(common.Dir.stall, map)
        
        

        # Draw the map
        screen.fill(BLACK)
        draw_map(map=map)
        is_dead = draw_characters(map)
        if is_dead: run = False

        if attack:
            characters[0].is_moving = True
            dir = characters[0].attack()
            atack_enemies_in_range(characters[0], dir, map.level)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # keyboard presses
            if event.type == pygame.KEYDOWN:
                characters[0].is_moving = True
                if event.key == pygame.K_w:
                    scroll_up = True
                if event.key == pygame.K_s:
                    scroll_down = True
                if event.key == pygame.K_a:
                    scroll_left = True
                if event.key == pygame.K_d:
                    scroll_right = True
                if event.key == pygame.K_SPACE:
                    attack = True
                if event.key == pygame.K_LSHIFT:
                    characters[0].speed = characters[0].speed * SPEED_RUN_MUL
                if event.key == pygame.K_ESCAPE:
                    return 

            if event.type == pygame.KEYUP:
                characters[0].is_moving = False
                characters[0].img_index = 0
                if event.key == pygame.K_w:
                    scroll_up = False
                if event.key == pygame.K_s:
                    scroll_down = False
                if event.key == pygame.K_a:
                    scroll_left = False
                if event.key == pygame.K_d:
                    scroll_right = False
                if event.key == pygame.K_LSHIFT:
                    characters[0].speed = characters[0].speed/ SPEED_RUN_MUL
                if event.key == pygame.K_SPACE:
                    dir = characters[0].sprite_key.split('_')[0]
                    characters[0].sprite_key = f'{dir}_walk_S'
                    attack = False

        pygame.display.update()

if __name__ == "__main__":
    print("Welcome to Game of the Undead")
    main()
