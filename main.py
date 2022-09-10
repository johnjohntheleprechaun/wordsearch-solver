import grid_parser as parser
import solver

grid = parser.str_to_grid(open("word_search.txt", "r").read())
words = open("words.txt", "r").read().split("\n")