from pathlib import Path
import csv
import common

DEBUG_ROW = 5
DEBUG = [1]


class Map:
    """
        Class that stores the map representation (matrix)
    """
    def __init__(self, level : int):
        """
            :param level: Identifier of the level
        """
        self.level = level
        self.grid = []
        self._load_from_csv()
        self.doors : "list[common.DoorLink]" = [] # List with door links that involve this map
        for door_link in common.DOOR_LIST:
            if door_link.door1.map_id == level or door_link.door2.map_id == level:
                self.doors.append(door_link)

    def check_door(self, i:int, j:int) -> common.Door:
        """
            Checks whether a i,j block is a a door and what level is it linked to (None on error or no link)
        """
        for link in self.doors:
            d1, d2 = link.doors()
            if d1.equals(i,j):
                return d2
            if d2.equals(i,j):
                return d1  
        return None
    
    def _load_from_csv(self):
        """
            Loads the map from the csv file
        """
        path = Path("levels")
        path = path / f"level{self.level}_data.csv"
        # print(f'{path = }')
        with open(path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                self.grid.append([int(e) for e in row])

    def getTile(self, pos: common.Point):
        """
            Returns the tile type given the pos as a Point
            
            :param pos: Point representation
        """
        i, j = pos.toMatrixIndex()
        return self.grid[i][j]
