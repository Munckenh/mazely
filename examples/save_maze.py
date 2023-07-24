"""Save a 64 by 64 rectangular, two-dimensional maze as `image.svg`."""

from mazely import Maze, Utilities


def main():
    maze = Maze(64, 64)
    utils = Utilities()
    utils.save_grid(maze.grid, "image.svg")


if __name__ == "__main__":
    main()
