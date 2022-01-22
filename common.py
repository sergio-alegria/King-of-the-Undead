from enum import Enum


# Map variables
DISPLAY_ROWS = 20
DISPLAY_COLS = 30

TILE_SIZE = 32

TILE_TYPES = 45

ROWS = DISPLAY_ROWS
MAX_COLS = DISPLAY_COLS

# Game variables
speed = 1.4

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0: [15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
}

HP_SKELETON = 15
HP_GOBLIN = 10
HP_WIZARD = 35
HP_GHOST = 25

HEALTH_BAR_WIDTH = TILE_SIZE
HEALTH_BAR_HEIGHT = 5

FLOOR = [0,1,2,3,4,39,13,14,20,21,17,18,15]

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
        
    def equals(self, i, j):
        return self.i == j and self.j == i
    
    def toPoint(self) -> Point:
        return Point(self.i*TILE_SIZE, self.j*TILE_SIZE)
        
class DoorLink:
    def __init__(self, door1 : Door, door2 : Door):
        self.door1 : Door = door1
        self.door2 : Door = door2
    
    def doors(self):
        return self.door1, self.door2
        
DOOR_LIST : "list[DoorLink]" = []

DOOR_LIST.append(DoorLink(Door(9,3,0), Door(7,19,2)))   # Level_0 door1 to Level_2
DOOR_LIST.append(DoorLink(Door(10,3,0), Door(8,19,2)))  # Level_0 door1 to Level_2
DOOR_LIST.append(DoorLink(Door(24,3,0), Door(5,19,1)))  # Level_0 door2 to Level_1 door1
DOOR_LIST.append(DoorLink(Door(14,1,1), Door(20,19,3))) # Level_1 door2 to Level_3 door1
DOOR_LIST.append(DoorLink(Door(13,1,1), Door(19,19,3))) # Level_1 door2 to Level_3 door1
DOOR_LIST.append(DoorLink(Door(26,1,3), Door(22,19,4))) # Level_3 door2 to Level_4 door1
DOOR_LIST.append(DoorLink(Door(4,10,4), Door(5,11,5)))  # Level_4 door2 to Level_5 door1

SONG = "resources/Music/The_Crypt_Loop.wav" 