"""Generate a 32 by 32 rectangular, two-dimensional maze with a
randomized version of Prim's algorithm.
"""

from mazely import Maze, Utilities
from mazely.algorithms import RandomizedPrim


def main():
    maze = Maze(32, 32, generator=RandomizedPrim())
    utils = Utilities()
    utils.show_grid(maze.grid)


if __name__ == "__main__":
    main()
