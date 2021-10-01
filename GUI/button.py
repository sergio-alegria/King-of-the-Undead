import pygame

class Button():
    """Button class"""
    def __init__ (self, x, y, image, scale):
        """
            @x,y Topleft coords of the button.
            @image : Image to display.
            @scale : Value used to comput the image size.
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(int(scale * width), int(scale * height)) # Aplay the scale to the base img
        self.rect = self.image.get_rect() #Rect object we gonna use to check collisions
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen):
        """
            @screen display where the button is being drawn.
            @returns True if the button was pressed, else returns False.
        """
        action = False 

        #mouse position
        mouse_pos = pygame.mouse.get_pos()

        #check if button was clicked
        if self.rect.collideoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y)) #Display the button

        return action