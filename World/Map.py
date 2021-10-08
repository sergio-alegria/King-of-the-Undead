import pygame
import Tile

pygame.init()


class Map():
    MAX_ROWS = 16
    MAX_COLS = 150

    def __init__ (self, id):
        self.rows = Map.MAX_ROWS
        self.cols = Map.MAX_ROWS #Base map is a square one
        self.id = id
        self.tiles = []
        for r in range(self.rows):
            for c in  range(self.cols):
                self.tiles[r][c] = Tile(r, c, 0) # Create the tiles, all the tiles are ground
        self.x_offset = 0
        self.y_offset = 0

    def import_from_csv(self):
        pass

    def export_to_csv(self):
        pass
    
    def draw(self, screen):
        """
            @screen display where the button is being drawn.
        """
        for t in self.tiles:
            t.draw(screen)

    