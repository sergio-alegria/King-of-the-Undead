import common
import random 

class Character():
    def __init__(self, id, hp, pos, dmg, sprites, starting_sprite="Stall"):
        """
            Init class for the character
            
            :param id: Character´s id
            :type id: int
        """
        self.id = id
        self.hp = hp
        self.pos = Point(pos[0], pos[1])
        self.dmg = dmg
        self.sprites = sprites
        self.sprite_key = starting_sprite
        self.img_index = 0
        self.image = sprites[ self.sprite_key][self.img_index]
        print(f'{self.image = }')

    def update(self) -> None:
        #update image
        self.img_index = (self.img_index + 1) % len(self.sprites[self.sprite_key])
        self.image = self.sprites[self.sprite_key][self.img_index]
    
    def change_sprite(self, sprite_key):
        self.sprite_key = sprite_key
        self.index = 0
        
    def move(self, dir) -> None:
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

    def receiveDmg(self, dmg = 1) -> None:
        self.hp -= dmg
        if self.hp <= 0:
            self.die()

    def attack(self) -> None:
        pass

    def die() -> None:
        pass
    
    def AI_move(self, mc_pos):
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

class Point():

    def __init__(self, x : int = None, y : int = None):
        self.x = x
        self.y = y
        
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