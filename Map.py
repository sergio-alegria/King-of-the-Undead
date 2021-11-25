from pathlib import Path
import csv

import common

DEBUG = [1]

DISPLAY_ROWS = 20
DISPLAY_COLS = 30

class Map():
    def __init__(self, level):
        self.level = level
        self.grid = [[-1]*common.MAX_COLS]*common.ROWS
        self.load_from_csv()
    
    def load_from_csv(self):
        path = Path("levels")
        path = path / f"level{self.level}_data.csv"
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                print(row)
                for y, tile in enumerate(row):
                    self.grid[x][y] = int(tile) 
    
    def diplayable_sub_matrix(self, x, y):
        matrix = []
        
        # Index calculation
        offset_up = y-DISPLAY_ROWS//2
        offset_down = y+DISPLAY_ROWS//2
        offset_left = x-DISPLAY_COLS//2
        offset_right = x+DISPLAY_COLS//2
        
        if offset_up < 0:
            offset_down -= offset_up # If y - is < 0 then add those rows to the other side
            offset_up = 0
        elif offset_down > common.ROWS:
            offset_up -= offset_down - common.ROWS
            offset_down = common.ROWS
        
        if offset_left < 0:
            offset_right -= offset_left
            offset_left = 0
        elif offset_right > common.MAX_COLS:
            offset_left -= offset_right - common.MAX_COLS
            offset_right = common.MAX_COLS 
            
        for row in self.grid[offset_up:offset_down+1]:
            matrix.append(row[offset_left:offset_right+1])
        print(matrix)
            

def debug_grid(map):
    for r in map.grid:
        print(len(r))


if __name__ == "__main__":
   some_map = Map(0)
   some_map.diplayable_sub_matrix(0,0)
   
    
        
        