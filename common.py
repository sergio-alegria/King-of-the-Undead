from enum import Enum

from numpy import common_type, tile

# Map variables
DISPLAY_ROWS = 20
DISPLAY_COLS = 20

TILE_SIZE = 32

TILE_TYPES = 45

ROWS = 20
MAX_COLS = 50

# Game variables
speed = 1

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0: [15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
}

FLOOR = [0,1,2,3,4,39]


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
        self.factor = int(TILE_SIZE/2)
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