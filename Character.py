import common
import pygame

#store character images un a list
main_character_animations = {"Top_walk" : [],
                             "Top_walk_S" : [],
                             "Down_walk" : [],
                             "Down_walk_S" : [],
                             "Rside_walk" : [],
                             "Rside_walk_S" : [],
                             "Lside_walk" : [],
                             "Lside_walk_S" : [],
                             "Top_attack" : [],
                             "Down_attack" : [],
                             "Lside_attack" : [],
                             "Rside_attack" : [],
                             "Dying" : []}

character_list = (8, 8, 8, 8, 8, 12, 0, 8, 6, 6, 6, 6, 4)

for i in main_character_animations:
    for j in character_list:
        for k in range(j):
            img = pygame.image.load(f'resources/Sprites pj/{i}/{i}-{k + 1}.png').convert_alpha()
            img = pygame.transform.scale(img, (common.TILE_SIZE, common.TILE_SIZE))
            main_character_animations[i] = img
            break
    break

class Character():
    def __init__(self, id, hp, pos, dir, dmg, sprites, index, image):
        """
            Init class for the character
            
            :param id: Character´s id
            :type id: int
        """
        self.id = id
        self.hp = hp
        self.pos = pos
        self.dir = common.Dir.stall
        self.dmg = dmg
        self.sprites = main_character_animations
        self.image = image

    def update(self) -> None:
        if self.dir == common.Dir.up:
            self.pos.y += common.speed
        elif self.dir == common.Dir.down:
            self.pos.y -= common.speed
        elif self.dir == common.Dir.left:
            self.pos.x -= common.speed
        elif self.dir == common.Dir.right:
            self.pos.x += common.speed
        '''match self.dir:
            case common.Dir.up :
                self.pos.y += common.speed
            case common.Dir.down :
                self.pos.y -= common.speed
            case common.Dir.left :
                self.pos.x -= common.speed
            case common.Dir.right :
                self.pos.x += common.speed'''

    def update_animation(self) -> None:
        #self.image = character_dict[]
        pass

    def move(self, dir) -> None:
        self.dir = dir

    def receiveDmg(self, dmg = 1) -> None:
        self.hp -= dmg
        if self.hp <= 0:
            self.die()

    def attack(self) -> None:
        return self.dir, self.dmg

    def die() -> None:
        pass


'''
class MainCharacter(Character):

    def __init__(self, id, hp, pos, dir, dmg, sprites):
        super().__init__(self, id, hp, pos, dir, sprites)

    def die() -> None:
        #Fin del juego
        pass


class Enemy(Character):

    def __init__(self, id, hp, pos, dir, sprites):
        super().__init__(self, id, hp, pos, dir, sprites)

    def draw(self) -> None:
        print(self.x)

    def move(self, dir) -> None:
        # Seguir al personaje principal
        pass


class Point():

    def __init__(self, x : int = None, y : int = None):
        self.x = x
        self.y = y


class Weapon(ABC):

    def __init__(self, dmg):
        self.dmg = dmg
'''