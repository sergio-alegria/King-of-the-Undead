import pygame
import common
import random 
import a_star_matrix
import numpy


class Point():
    def __init__(self, x : int = None, y : int = None):
        self.x = x
        self.y = y
        
    def toTuple(self):
        return (self.x,self.y)

class Weapon():
    def __init__(self, dmg, range):
        self.dmg = dmg
        self.range = range
    
    def get_rect(self, pos, direction):
        if dir == common.Dir.up or dir == common.Dir.down:
            return pygame.Rect(pos,(self.range/2, self.range))     
        else: 
            return pygame.Rect(pos,(self.range, self.range/2))
        
class Character():
    ATTACK_FRAMES = 6
    def __init__(self, id, hp, pos, sprites, starting_sprite="Stall"):
        """
            Init class for the character
            
            :param id: Character's id
            :type id: int
        """
        self.id = id
        self.hp = hp
        self.pos = Point(pos[0], pos[1])
        self.weapon = Weapon(0.5, 20)
        self.attacking_frames = 0
        self.attacking_counter = 0 
        self.sprites = sprites
        self.sprite_key = starting_sprite
        self.img_index = 0
        self.image = sprites[self.sprite_key][self.img_index]
        self.is_moving = False
        self.is_attacking = False
        self.delay_counter = 0
        self.dir = common.Dir.stall

    def update(self) -> None:
        if self.is_attacking and self.img_index >= len(self.sprites[self.sprite_key]):
            self.is_attacking = False
            pass
        try:
            if self.is_moving: 
                self.img_index = (self.img_index + 1) % len(self.sprites[self.sprite_key])
        except IndexError: pass
        finally:
            self.image = self.sprites[self.sprite_key][self.img_index]
    
    def change_sprite(self, sprite_key):
        if self.is_attacking: return # If attacking dont change
        self.sprite_key = sprite_key
        
    def move(self, dir) -> None:
        if self.attacking_frames:
            pass 
        if dir == self.dir:
            return
        self.is_moving = True
        if dir == common.Dir.up:
            self.pos.y += common.speed
            self.change_sprite("Down_walk_S")
        elif dir == common.Dir.down:
            self.pos.y -= common.speed
            self.change_sprite("Top_walk_S")
        elif dir == common.Dir.left:
            self.pos.x -= common.speed
            self.change_sprite("Lside_walk_S")
        elif dir == common.Dir.right:
            self.pos.x += common.speed
            self.change_sprite("Rside_walk_S")
        elif dir == common.Dir.stall:
            self.change_sprite("Stall")

    def receive_dmg(self, dmg) -> bool:
        self.hp -= dmg
        if self.hp <= 0:
           return True
        return False
         
    def attack(self):
        direction = self.sprite_key.split("_")[0]
        if direction == 'Stall':
            direction = 'Down'
        self.prev_key = self.sprite_key
        self.change_sprite(f"{direction}_attack")
        self.is_atacking = True
        return self.dir, self.weapon.dmg
        
    def die(self) -> bool:
        self.died_counter = 1
        self.change_sprite("Dying")
    
    def AI_move(self, mc_pos):
        self.is_moving = True
        moves = [common.Dir.stall]
        if self.pos.x > mc_pos.x:
           moves.append(common.Dir.left) 
        elif self.pos.x < mc_pos.x:
            moves.append(common.Dir.right)
        if self.pos.y < mc_pos.y:
            moves.append(common.Dir.up)
        if self.pos.y > mc_pos.y:
            moves.append(common.Dir.down)
        #print(f"{self.id}\nenemy(x,y)=({self.pos.x},{self.pos.y})\nmain_char(x,y)=({mc_pos.x},{mc_pos.y})\n{moves = }")    
        self.move(moves[random.randint(0,len(moves)-1)])


    del parse_map(map):
        map_parsed = []
        row = []
        for i in map:
            for j in i:
                if j != 0:
                    j = -1
                    row.append(j)
            map_parsed.append[i]

    def AI_move_a_star(self):
        self.is_moving = True
        moves = [common.Dir.stall]
        nmap = numpy.array([
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
        print(a_star_matrix.astar(nmap, (0,0), (10,13)))

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





class Weapon(ABC):

    def __init__(self, dmg):
        self.dmg = dmg
'''