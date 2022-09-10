import parser

class Letter:
    letter: str
    surrounding: 'dict[str,Letter]'

    def __init__(self, letter):
        self.letter = letter
    

def index_grid(grid: 'list[list]'):
    return

def convert_grid(str_grid: 'list[list[str]]') -> 'list[list[Letter]]':
    letter_grid = []
    for row in str_grid:
        letter_row = []
        for letter in row:
            letter_row.append(Letter(letter))
        letter_grid.append(letter_row)
    return letter_grid

def load_surrounding(grid: 'list[list[Letter]]', x, y):
    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            if not (x,y) == (x1,y1):
                grid[y][x].surrounding.append(safe_fetch(grid, x1, y1))
            

def safe_fetch(grid, x, y):
    if y in [0, len(grid)]:
        return None
    elif x in [0, len(grid[y])]:
        return None
    else:
        return grid[x,y]