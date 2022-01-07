from pathlib import Path
import csv
import common
from Character import Point

DEBUG_ROW = 5
DEBUG = [1]   

class Map():
    def __init__(self, level):
        self.level = level
        self.grid = []
        self.load_from_csv()
        
        print(f'{self.grid = }')
        
    def load_from_csv(self):
        path = Path("levels")
        path = path / f"level{self.level}_data.csv"
        #print(f'{path = }')
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.grid.append([int(e) for e in row])
               
                
    def diplayable_sub_matrix(self, x, y):
        matrix = []
        
        # Index calculation
        offset_up = y-common.DISPLAY_ROWS//2
        offset_down = y+common.DISPLAY_ROWS//2
        offset_left = x-common.DISPLAY_COLS//2
        offset_right = x+common.DISPLAY_COLS//2
        
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
        
        print(f"{offset_up   = }  {offset_down  = }")
        print(f"{offset_left = }  {offset_right = }")
        for row in self.grid[offset_up:offset_down]:
            matrix.append(row[offset_left:offset_right])
        return matrix
        
    def getTile(self, pos: Point):
        factor = common.TILE_SIZE
        print(pos.__dict__)
        print(f'{pos.x//factor}')
        print(f'{pos.y//factor}')
        print(self.grid[pos.x//factor][pos.y//factor])
        return self.grid[pos.x//factor][pos.y//factor]    

    def parse_map(self):
        map_parsed = [[0 if e not in common.WALL_TILES else 1 for e in row] for row in self.grid]
        return map_parsed



def debug_grid(map):
    for r in map.grid:
        print(len(r))


if __name__ == "__main__":
    m = Map(0)
    with open("parsed.csv", "w") as f:
        for row in m.parse_map():
            f.write(str(row) + '\n')
    
        
    
        
        
