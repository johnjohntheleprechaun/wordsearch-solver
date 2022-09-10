def str_to_grid(string: str):
    return [[letter for letter in row] for row in string.split("\n")]