from abc import ABC, abstractmethod
import common

class Character(ABC):
    def __init__(self, id, hp, pos, dir, dmg, sprites):
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
        self.sprites = sprites

    def draw(self) -> None:
        pass

    def update(self) -> None:
        match self.dir:
            case common.Dir.up :
                self.pos.y += common.speed
            case common.Dir.down :
                self.pos.y -= common.speed
            case common.Dir.left :
                self.pos.x -= common.speed
            case common.Dir.right :
                self.pos.x += common.speed

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
