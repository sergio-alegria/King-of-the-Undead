from abc import ABC, abstractmethod

class Character(ABC):
     
    def __init__(self, x : int):
        self.x = x
        pass

    def draw(self) -> None:
        pass

    def update() -> None:
        pass
    
    def move() -> None:
        pass
    
    def attack() -> None:
        pass
    
    def die() -> None:
        pass

class Enemy(Character):
    def __init__(self, id, x : int = None):
        super().__init__(x)
    
    def draw(self) -> None:
        print(self.x)

    
    