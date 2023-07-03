from maze import Maze, Utilities


def main():
    maze = Maze(path="resources/2015apec.maze")
    utils = Utilities()
    utils.show_grid(maze.grid)


if __name__ == "__main__":
    main()
