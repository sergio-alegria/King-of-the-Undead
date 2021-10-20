import pygame
from World import Tile
from GUI import Button 

pygame.init()

images = {}  # Dict with the images and their id
sprites = {}
TILESET_SIZE = 1

def load_characters_sprite():
    characters = ["Ghost", "Goblin", "Skeleton", "Wizard"]
    for character in characters:
        list = []
        for i in range(1,9):
            image = pygame.image.load(f'resources/Sprites mobs/{character}-{i}.png') # Load the 9 images that conform the character sprite
            image = pygame.transform.scale(image, (2*Tile.TILE_SIZE, 2*Tile.TILE_SIZE))   # Scale the img to the size we are using them.
            list.append(image)
        sprites[character] = list

def init():
    load_characters_sprite()
    
    image = pygame.image.load(f'resources/Icons/button_save.png').convert_alpha()
    image = pygame.transform.scale(image, (Tile.TILE_SIZE, Tile.TILE_SIZE))   # Scale the img to the size we are using them.
    images["SAVE"] = image
    
    image = pygame.image.load(f'resources/Icons/button_load.png').convert_alpha()
    image = pygame.transform.scale(image, (Tile.TILE_SIZE, Tile.TILE_SIZE))   # Scale the img to the size we are using them.
    images["LOAD"] = image
    
    # Import the Tileset as images
    for i in range(TILESET_SIZE):
        image = pygame.image.load(f'resources/Tileset/{i}.png').convert_alpha()
        image = pygame.transform.scale(image, (Tile.TILE_SIZE, Tile.TILE_SIZE))   # Scale the img to the size we are using them.
        images[f'{i}'] = image