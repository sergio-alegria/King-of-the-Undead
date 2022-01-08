import pygame
import common
import random
import a_star_matrix
import numpy
from copy import deepcopy
from common import TILE_SIZE, Point


class Weapon:
    def __init__(self, dmg, range):
        self.dmg = dmg
        self.range = range

    def get_rect(self, pos, direction):
        if dir == common.Dir.up or dir == common.Dir.down:
            return pygame.Rect(pos, (self.range / 2, self.range))
        else:
            return pygame.Rect(pos, (self.range, self.range / 2))


class Character:
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
                self.img_index = (self.img_index + 1) % len(
                    self.sprites[self.sprite_key]
                )
        except IndexError:
            pass
        finally:
            self.image = self.sprites[self.sprite_key][self.img_index]
    def change_sprite(self, sprite_key):
        if self.is_attacking:
            return  # If attacking dont change
        self.sprite_key = sprite_key

    def move(self, dir, map) -> None:
        if self.attacking_frames:
            pass
        if dir == self.dir:
            return
        
        # Copy pos
        new_pos = deepcopy(self.pos)
        self.is_moving = True
        if dir == common.Dir.up:
            new_pos.update_y(common.speed)
        elif dir == common.Dir.down:
            new_pos.update_y(-common.speed)
        elif dir == common.Dir.left:
            new_pos.update_x(-common.speed)
        elif dir == common.Dir.right:
            new_pos.update_x(common.speed)
        elif dir == common.Dir.stall: return 
        
        pos_i, pos_j = self.pos.toMatrixIndex()
        new_pos_i,new_pos_j = new_pos.toMatrixIndex()
          
        if not (pos_i == new_pos_i and pos_j == new_pos_j):
            if not map.getTile(new_pos) in common.FLOOR:
                return 
                 
        if dir == common.Dir.up:
            self.pos.update_y(common.speed)
            self.change_sprite("Down_walk_S")
        elif dir == common.Dir.down:
            self.pos.update_y(-common.speed)
            self.change_sprite("Top_walk_S")
        elif dir == common.Dir.left:
            self.pos.update_x(-common.speed)
            self.change_sprite("Lside_walk_S")
        elif dir == common.Dir.right:
            self.pos.update_x(common.speed)
            self.change_sprite("Rside_walk_S")
                
    def receive_dmg(self, dmg) -> bool:
        self.hp -= dmg
        if self.hp <= 0:
            return True
        return False

    def attack(self):
        direction = self.sprite_key.split("_")[0]
        if direction == "Stall":
            direction = "Down"
        self.prev_key = self.sprite_key
        self.change_sprite(f"{direction}_attack")
        self.is_atacking = True
        return self.dir, self.weapon.dmg

    def die(self) -> bool:
        self.died_counter = 1
        self.change_sprite("Dying")

    def AI_move(self, mc_pos, map):
        print(self.pos.__dict__)
        print(mc_pos.__dict__)
        self.is_moving = True
        moves = [common.Dir.stall]
        if self.pos.x > mc_pos.x:
            moves.append(common.Dir.left)
        elif self.pos.x < mc_pos.x:
            moves.append(common.Dir.right)
        if self.pos.y < mc_pos.y:
            moves.append(common.Dir.down)
        if self.pos.y > mc_pos.y:
            moves.append(common.Dir.up)
        print(moves)
        self.move(moves[random.randint(0, len(moves) - 1)], map)

    def AI_move_a_star(self, map, pos: Point):
        self.is_moving = True
        moves = [common.Dir.stall]

        nmap = numpy.array(map)

        mob_x, mob_y = self.pos.toTuple()
        character_x, character_y = pos.toTuple()

        print(
            a_star_matrix.astar(
                nmap,
                (mob_x / common.TILE_SIZE, mob_y / common.TILE_SIZE),
                (character_x / common.TILE_SIZE, character_y / common.TILE_SIZE),
            )
        )


"""
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
"""
