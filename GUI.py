import pygame
from World import Tile

class Button(Tile):
    """Button class"""
    def __init__ (self, x, y, path):
        """
            @x,y Topleft coords of the button.
            @image : Image to display.
        """ 
        super().__init__()
        self.clicked = False

    def draw(self, screen):
        """
            @screen display where the button is being drawn.
            @returns True if the button was pressed, else returns False.
        """
        pressed = False 

        # Mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if button was clicked
        if self.rect.collideoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                pressed = True
                self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        # Draw button
        super().draw()  # Call the super method for drawing

        return pressed