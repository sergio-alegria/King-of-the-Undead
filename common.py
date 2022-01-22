from enum import Enum
import json

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
with open("doors.json", "r") as jsonfile:
    data = json.load(jsonfile)
for link in data["LINKS"]:
    DOOR_LIST.append(DoorLink(Door(link["d1_i"],link["d1_j"], link["d1_map_id"]), Door(link["d2_i"],link["d2_j"], link["d2_map_id"])))  


SONG = "resources/Music/The_Crypt_Loop.wav" 