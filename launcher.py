import pygame
from pathlib import Path
import king_of_the_undead
import map_generator
import common 

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
pygame.display.set_caption("Launcher")

MAIN_MENU_DIR = Path("resources/Frames_menu")
MAIN_MENU_IMAGES = 6
MAIN_MENU_CHANGE_FRAME = FPS * 3


def main_menu():
    global screen
    
    pygame.mixer.music.load(Path(common.SONG))
    pygame.mixer.music.play(-1)           # Play the music

    run = True
    index = 0
    count = 0
    image_pos = (0,0)
    images = []
    for i in range(1,MAIN_MENU_IMAGES+1):
        img = pygame.image.load(MAIN_MENU_DIR / f"main_menu_{i}.png").convert_alpha()
        img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        images.append(img)
    
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    game_text = myfont.render('K: King of the Undead', False, (255, 255, 255))
    maps_text = myfont.render('M: Map generator', False, (255, 255, 255))
    game_pos = (100, SCREEN_HEIGHT-75)
    maps_pos = (SCREEN_WIDTH-375, SCREEN_HEIGHT-75)
    while run:
        # Load image
        screen.blit(images[index], image_pos)
        screen.blit(game_text,game_pos)
        screen.blit(maps_text,maps_pos)
        
        count = (count + 1) % MAIN_MENU_CHANGE_FRAME
        if not count: 
            index = (index + 1) % MAIN_MENU_IMAGES
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_k:
                    king_of_the_undead.main()
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    pygame.display.set_caption("Launcher")
                if event.key == pygame.K_m:
                    map_generator.map_generator()
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    pygame.display.set_caption("Launcher")
        pygame.display.update()


if __name__ == "__main__":
    main_menu()
    pygame.quit()