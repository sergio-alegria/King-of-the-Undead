from abc import ABC, abstractmethod
from common import Dir

class Character(ABC):

    def __init__(self, id, hp, pos, dir, dmg, sprites):
        self.id = id
        self.hp = hp
        self.pos = pos
        self.dir = Dir.stall
        self.dmg = dmg
        self.sprites = sprites

    def draw(self) -> None:
        pass

    def update(self) -> None:
        match self.dir:
            case Dir.up :
                self.pos.y += 1
            case Dir.down :
                self.pos.y -= 1
            case Dir.left :
                self.pos.x -= 1
            case Dir.right :
                self.pos.x += 1

    def move(self, dir) -> None:
        self.dir = dir

    def receiveDmg(self, dmg = 1) -> None:
        self.hp -= dmg
        if self.hp <= 0:
            self.die()

    def attack(self) -> None:
        return self.dir, self.dmg

    @abstractmethod
    def die() -> None:
        pass


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
