"""Display a 32 by 32 rectangular, two-dimensional maze and its solution."""

from mazely import Maze, Utilities


def main():
    maze = Maze(32, 32)
    utils = Utilities()
    utils.show_solution(maze.grid, maze.solution_path)


if __name__ == "__main__":
    main()
