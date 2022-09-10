import grid_parser as parser

def solve(grid: 'list[list[str]]', words: 'list[str]') -> 'dict[str,tuple[tuple[int,int],tuple[int,int]]]':
    solutions = {}
    indexed = index_grid(grid)
    for word in words:
        solved = False
        for position in indexed[word[0]]:
            # get possible directions
            directions = []
            for y in range(position[0]-1, position[0]+2):
                for x in range(position[1]-1, position[1]+2):
                    # check if direction matches the second letter
                    if (y,x) != position and safe_fetch(grid, (y,x)) == word[1]:
                        directions.append((y-position[0],x-position[1]))
            if len(directions) == 0:
                pass
            # start recursive
            for direction in directions:
                if match(grid, word[1:], position, direction):
                    # add solution
                    solutions[word] = (position, direction)
                    solved = True
                    break
            if solved:
                break
    return solutions

def match(grid: 'list[list[str]]', word: str, position: 'tuple[int,int]', direction: 'tuple[int,int]') -> bool:
    if len(word) == 0: # full word has been matched
        return True
    # move in direction
    next = (position[0] + direction[0], position[1] + direction[1])
    # check if word matches
    if word[0] == safe_fetch(grid, next):
        # recurse (cut off first letter)
        return match(grid, word[1:], next, direction)
    else:
        return False

def index_grid(grid: 'list[list[str]]') -> 'dict[str,list[tuple[int,int]]]':
    indexed = {}
    # iterate through every letter on the grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # safeguard against KeyError
            if not grid[y][x] in indexed:
                indexed[grid[y][x]] = []
            # add the letters position to the index
            indexed[grid[y][x]].append((y, x))

    return indexed

def safe_fetch(grid, position):
    # return None if position is off of grid
    if position[0] < 0 or position[1] < 0 or position[0] > len(grid)-1 or position[1] > len(grid)-1:
        return None
    # otherwise return the letter at position
    else:
        return grid[position[0]][position[1]]

def test():
    grid = parser.str_to_grid(open("word_search.txt", "r").read())
    words = open("words.txt", "r").read().split("\n")
    print(solve(grid, words))
test()