import pygame
import common
import random
from copy import deepcopy
from Map import Map

class Weapon:
    """
        Class that defines the weapon attributes and it's functions.
    """
    def __init__(self, dmg: float, range: int):
        """
            Init class for the weapon

            :param dmg: Weapong's damage
            :param range: Weapong's range
        """
        self.dmg = dmg
        self.range = range

    def get_rect(self, pos : tuple, direction: common.Dir) -> pygame.Rect:
        """
            Function to get the weapon hitbox.

            :param pos: Weapon pos
            :param direction: Weapon direction
        """
        center = (pos[0] - common.TILE_SIZE//2, pos[1] - common.TILE_SIZE//3)
        if direction == common.Dir.up or direction == common.Dir.down:
            return pygame.Rect(center, (self.range / 2, self.range))
        else:
            return pygame.Rect(center, (self.range, self.range / 2))


class Character:
    """
        Class that defines characters attributes and it's functions.
    """
    ATTACK_FRAMES = 6

    def __init__(self, id, hp, pos, sprites, starting_sprite="Stall"):
        """
            Init class for the character

            :param id: Character's id
            :param hp: Character's health
            :param pos: Character's position
            :param sprites: Character's sprites
            :param starting_sprite: Character's starting sprite
        """
        self.id = id
        self.hp = hp
        self.max_hp = hp
        self.pos = self.pos = pos if isinstance(pos, common.Point) else common.Point(pos[0], pos[1])
        self.weapon = Weapon(1, common.TILE_SIZE) if not id else Weapon(0.5, common.TILE_SIZE//2)
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
        self.speed = common.speed
        self.hp_regen = 0.3

    def update(self) -> None:
        """
            Performs the periodic tasks such as update image or hp regeneration
        """
        # HP regeneration
        self.hp = self.hp + self.hp_regen if self.hp < self.max_hp else self.max_hp  
        if self.is_attacking and self.img_index >= len(self.sprites[self.sprite_key]):
            self.is_attacking = False
            pass
        try:
            # If is moving change to the next image
            if self.is_moving:
                self.img_index = (self.img_index + 1) % len(self.sprites[self.sprite_key])
        except IndexError:
            pass
        finally:
            # Update image frame 
            self.image = self.sprites[self.sprite_key][self.img_index]
            
    def change_sprite(self, sprite_key : str):
        """
            Changes the character sprite
            
            :param sprite_key: Sprite identifier 
        """
        if self.is_attacking:
            return  # If attacking dont change
        self.sprite_key = sprite_key

    def move(self, dir : common.Dir, map : Map) -> bool:
        """
            Returns if changed tile
        """
        if self.attacking_frames:
            pass
        if dir == self.dir:
            return
        
        # Copy pos
        new_pos = deepcopy(self.pos)
        self.is_moving = True
        if dir == common.Dir.up:
            new_pos.update_y(self.speed)
        elif dir == common.Dir.down:
            new_pos.update_y(-self.speed)
        elif dir == common.Dir.left:
            new_pos.update_x(-self.speed)
        elif dir == common.Dir.right:
            new_pos.update_x(self.speed)
        elif dir == common.Dir.stall: return 
        
        pos_i, pos_j = self.pos.toMatrixIndex()
        new_pos_i,new_pos_j = new_pos.toMatrixIndex()
        
        if not (pos_i == new_pos_i and pos_j == new_pos_j):
            try:
                if not map.getTile(new_pos) in common.FLOOR:
                    return False
            except IndexError as e:
                return False 
             
        self.prev_pos = deepcopy(self.pos)

        if dir == common.Dir.up:
            self.pos.update_y(self.speed)
            if self.pos.y > (common.ROWS)*common.TILE_SIZE: self.pos.update_y(-self.speed)
            self.change_sprite("Down_walk_S")
        elif dir == common.Dir.down:
            self.pos.update_y(-self.speed)
            if self.pos.y < 0: self.pos.update_y(self.speed)
            self.change_sprite("Top_walk_S")
        elif dir == common.Dir.left:
            self.pos.update_x(-self.speed)
            if self.pos.x < 0: self.pos.update_x(self.speed)
            self.change_sprite("Lside_walk_S")
        elif dir == common.Dir.right:
            self.pos.update_x(self.speed)
            if self.pos.x > (common.MAX_COLS)*common.TILE_SIZE: self.pos.update_x(-self.speed)
            self.change_sprite("Rside_walk_S")
        
        return not (pos_i == new_pos_i and pos_j == new_pos_j)
                
    def receive_dmg(self, dmg) -> bool:
        """
            Compute the new health after the hit, and return if the character is dead.

            :param dmg: Damage received.
        """
        self.hp -= dmg
        if self.hp <= 0:
            return True
        return False

    def attack(self):
        """
            Perform the attack changing the sprites and returning the direction and the damage
        """
        direction = self.sprite_key.split("_")[0]
        if direction == "Stall":
            direction = "Down"
        self.prev_key = self.sprite_key
        self.change_sprite(f"{direction}_attack")
        self.is_atacking = True
        return self.dir, self.weapon.dmg

    def AI_move(self, character, map):
        """
            Little algorithm for the enemies AI.

            :param character: Character to move.
            :param map: Map in where the character.
            
            :returns: True if it is in range to atack the main character
        """
        mc_pos = character.pos
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
        self.move(moves[random.randint(0, len(moves) - 1)], map)
        
        return self.image.get_rect(center=self.pos.toTuple()).colliderect(character.weapon.get_rect(character.pos.toTuple(), common.Dir.down))
    