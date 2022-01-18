from dataclasses import dataclass
from enum import Enum

from numpy import common_type, tile

# Map variables
DISPLAY_ROWS = 20
DISPLAY_COLS = 30

TILE_SIZE = 40

TILE_TYPES = 45

ROWS = DISPLAY_ROWS
MAX_COLS = DISPLAY_COLS

# Game variables
speed = 1.4

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0: [15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
}

FLOOR = [0,1,2,3,4,39]
DOOR_LIST = []

class Dir(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    stall = 4


class Point:
    def __init__(self, x: int = None, y: int = None):
        self.x = x
        self.y = y
        self.factor = int(TILE_SIZE)
        self.i = int(self.y/self.factor)
        self.j = int(self.x/self.factor)

    def update_y(self, value):
        self.y += value
        self.i =  int(self.y/self.factor)
        
    def update_x(self, value):
        self.x += value
        self.j =  int(self.x/self.factor) 
    
    def toTuple(self):
        return (self.x, self.y)

    def toMatrixIndex(self):
        return self.i, self.j
    
class Door:
    def __init__(self, i : int, j : int, map_id : int):
        self.i = i
        self.j = j
        self.map_id = map_id
        
class DoorLink:
    def __init__(self, door1 : Door, door2 : Door):
        self.door1 = door1
        self.door2 = door2
        

link.append(DoorLink(Door(2,2,1), Door(3,3,2)))
