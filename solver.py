import grid_parser as parser

def index_grid(grid: 'list[list[str]]') -> 'dict[str,list[tuple[int,int]]]':
    indexed = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if not grid[y][x] in indexed:
                indexed[grid[y][x]] = []
            indexed[grid[y][x]].append((x, y))
    return indexed
            

def safe_fetch(grid, x, y):
    if y in [0, len(grid)]:
        return None
    elif x in [0, len(grid[y])]:
        return None
    else:
        return grid[x,y]

def test():
    grid = parser.str_to_grid(open("word_search.txt", "r").read())
    print(index_grid(grid))
test()