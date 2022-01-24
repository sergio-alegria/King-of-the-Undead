from enum import Enum
import json
from pygame import USEREVENT

# Map variables
DISPLAY_ROWS = 20
DISPLAY_COLS = 30

TILE_SIZE = 32

TILE_TYPES = 82

MUSIC_END = USEREVENT+1

ROWS = DISPLAY_ROWS
MAX_COLS = DISPLAY_COLS

# Game variables
speed = 1.4

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0: [16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 45],
    52:[77, 78, 80, 81]
}

# Define base enemies hp
ENEMIES_HP = {
    "Goblin" : 10,
    "Skeleton" : 15,
    "Wizard" : 35,
    "Ghost" : 25
}

# Healt bar parameter
HEALTH_BAR_WIDTH = TILE_SIZE
HEALTH_BAR_HEIGHT = 5

# Define which tiles the character can move to
FLOOR = [0,1,2,3,4,11,39,40,14,20,21,17,18,15,45,46,47,52,53,54,
        60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,79,80,81]

class Dir(Enum):
    """
        Enum to represent the possible directions a character can move
    """
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
        """
            Updates the y value of the point and the matrix's point index
        """
        self.y += value
        self.i =  int(self.y/self.factor)
        
    def update_x(self, value):
        """
            Updates the x value of the point and the matrix's point index
        """
        self.x += value
        self.j =  int(self.x/self.factor) 
    
    def toTuple(self):
        """
            Returns the point as a tuple (x,y)
        """
        return (self.x, self.y)

    def toMatrixIndex(self):
        """
            Returns the point's index in the matrix based on the coordinates
        """
        return self.i, self.j
    
class Door:
    def __init__(self, i : int, j : int, map_id : int):
        self.i = i
        self.j = j
        self.map_id = map_id
        
    def equals(self, i : int, j : int) -> bool:
        """
            Checks if some i,j matrix index are the same as the ones where the door is
        """
        return self.i == j and self.j == i
    
    def toPoint(self) -> Point:
        """
            Return the door coordinates x,y in pixels as a Point
        """
        return Point(self.i*TILE_SIZE, self.j*TILE_SIZE)
        
class DoorLink:
    def __init__(self, door1 : Door, door2 : Door):
        self.door1 : Door = door1
        self.door2 : Door = door2
    
    def doors(self):
        """
            Returns the doors that are linked
        """
        return self.door1, self.door2

# Define the door list and read it from the config/doors.json        
DOOR_LIST : "list[DoorLink]" = []
with open("config/doors.json", "r") as jsonfile:
    data = json.load(jsonfile)
for link in data["LINKS"]:
    DOOR_LIST.append(DoorLink(Door(link["d1_i"],link["d1_j"], link["d1_map_id"]), Door(link["d2_i"],link["d2_j"], link["d2_map_id"])))  


SONG = "resources/Music/The_Crypt_Loop.wav" 