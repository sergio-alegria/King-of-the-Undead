"""
    Game developed by Alejandro Benitez, Raul Eguren and Sergio Alegria for the Computer Animation and Videogames lesson at the Universidad de Cantabria
    Contact Info:
    Sergio Alegria: sergiioalegriia@gmail.com
"""

import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Display 16x16 tiles to the player
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SIDE_MARGIN = 400

#Tilesize
TILESIZE = 64
MAP_TILES = SCREEN_WIDTH//TILESIZE

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
pygame.display.set_caption('King of the Undead')


def main():
    run = True
    while run:
        pass 
        

if __name__ == "__main__":
    print("Welcome to Game of the Undead")
    main()