import pygame


class Tile():
    TILE_TYPES = 10
    TILE_SIZE = 64 #Static
    GROUND_TILES = (0) #Set of tiles that count as ground

    def __init__(self, x, y, id, subdir="Tileset"):
        """
            @id -> name of the file (without .png)
            Optional @subdir specify if not from Tileset
        """
        self.img = pygame.image.load(f'resources/{subdir}/{id}.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (Tile.TILE_SIZE, Tile.TILE_SIZE))   # Scale the img to the size we are using them.
        self.rect = self.image.get_rect()   # Rect object we gonna use to check collisions
        self.rect.topleft = (x,y)
    
    
    def draw(self, screen):
        """
            @screen display where the button is being drawn.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y)) # Display the img

