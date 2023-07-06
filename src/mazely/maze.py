import random

import numpy as np

from .algorithms import MazeGenerator, MazeSolver, RecursiveBacktracking, ShortestPath


class Maze:
    """A class to represent a rectangular, two-dimensional maze.

    Attributes
    -----------
    rows : int
        The total number of rows in the maze. Defaults to ``3``.
    columns : int
        The total number of columns in the maze. Defaults to ``3``.
    grid : numpy.ndarray
        A two-dimensional array of cells representing a rectangular maze.
    grid_size : int
        The total number of cells in the maze.
    solution_path : list[tuple[int, int]]
        An ordered list of cell locations representing the solution path.
    start : tuple[int, int]
        The location of the start cell.
    goal : set[tuple[int, int]]
        The location(s) of the goal cell(s).
    path : str, optional
        A path to a maze file. Defaults to :obj:`None`.
    generator : MazeGenerator
        An instance of a :class:`.MazeGenerator` subclass used for generating mazes. Defaults to :class:`.RecursiveBacktracking`.
    solver : MazeSolver
        An instance of a :class:`.MazeSolver` subclass used for solving mazes. Defaults to :class:`.ShortestPath`.
    """

    def __init__(
        self,
        rows: int = 3,
        columns: int = 3,
        path: str | None = None,
        generator: MazeGenerator = RecursiveBacktracking(),
        solver: MazeSolver = ShortestPath(),
    ):
        self.generator = generator
        self.solver = solver

        if path is not None:
            self.load_maze(path)
        else:
            self.rows = rows
            self.columns = columns
            self.grid_size = rows * columns
            self.grid = self.generator.generate(rows, columns)
            self.start = self.get_random_cell()
            self.goal = {self.get_random_cell()}

        self.solution_path = self.solver.solve(self.grid, self.start, self.goal)

    def load_maze(self, path: str):
        """Parse a maze file.

        Parameters
        ----------
        path : str
            A path to a maze file.
        """
        with open(path, "r") as file:
            # Parse the file into a list of strings of lines.
            lines = [line.strip() for line in file if not line.isspace()]

            # Update the attributes.
            self.rows = len(lines) // 2
            self.columns = len(lines[0]) // 4
            self.grid_size = self.rows * self.columns
            self.grid = np.full((self.rows, self.columns, 4), [False] * 4)

            # Iterate over each possible cell position and update the wall details of the current cell.
            for row in range(self.rows):
                for column in range(self.columns):
                    # If the current cell is the start.
                    if lines[row * 2 + 1][column * 4 + 2] == "S":
                        self.set_start_cell(row, column)

                    # If the current cell is the goal.
                    elif lines[row * 2 + 1][column * 4 + 2] == "G":
                        if hasattr(self, "goal"):
                            self.add_goal_cell(row, column)
                        else:
                            self.set_goal_cell(row, column)

                    # If a north wall exists.
                    if lines[row * 2][column * 4 + 2] == "-":
                        self.grid[row][column][0] = True

                    # If a south wall exists.
                    if lines[row * 2 + 2][column * 4 + 2] == "-":
                        self.grid[row][column][1] = True

                    # If an east wall exists.
                    if lines[row * 2 + 1][column * 4 + 4] == "|":
                        self.grid[row][column][2] = True

                    # If a west wall exists.
                    if lines[row * 2 + 1][column * 4] == "|":
                        self.grid[row][column][3] = True

    def generate(self, rows: int, columns: int):
        """Generate a new maze and overwrite to :attr:`grid`.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.
        """
        self.rows = rows
        self.columns = columns
        self.grid_size = rows * columns
        self.grid = self.generator.generate(rows, columns)

    def solve(self):
        """Solve the maze with a specific configuration."""
        self.solution_path = self.solver.solve(self.grid, self.start, self.goal)

    def set_start_cell(self, row: int, column: int):
        """Set a cell at a location as a start cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.
        """
        self.start = (row, column)

    def set_goal_cell(self, row: int, column: int):
        """Set a cell at a location as a goal cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.
        """
        self.goal = {(row, column)}

    def add_goal_cell(self, row: int, column: int):
        """Add a cell at a location as a goal cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.
        """
        self.goal.add((row, column))

    def get_random_cell(self) -> tuple[int, int]:
        """Get a random cell location.

        Returns
        -------
        tuple[int, int]
            The location of a random cell.
        """
        return (random.randrange(self.rows), random.randrange(self.columns))

    def remove_wall(self, cell: tuple[int, int], neighbor: tuple[int, int]):
        """Remove the wall between a cell and its neighbor.

        Parameters
        ----------
        cell : tuple[int, int]
            The location of the cell.
        neighbor : tuple[int, int]
            The location of the cell's neighbor.
        """
        if cell[1] == neighbor[1]:  # If both cells share the same column.
            # +---+
            # | C |
            # +---+
            # | N |
            # +---+
            if cell[0] < neighbor[0]:
                self._grid[cell[0]][cell[1]][1] = False
                self._grid[neighbor[0]][neighbor[1]][0] = False
            
            # +---+
            # | N |
            # +---+
            # | C |
            # +---+
            else:
                self._grid[cell[0]][cell[1]][0] = False
                self._grid[neighbor[0]][neighbor[1]][1] = False
                
        elif cell[0] == neighbor[0]:  # If both cells share the same row.
            # +---+---+
            # | C | N |
            # +---+---+
            if cell[1] < neighbor[1]:
                self._grid[cell[0]][cell[1]][2] = False
                self._grid[neighbor[0]][neighbor[1]][3] = False

            # +---+---+
            # | N | C |
            # +---+---+
            else:
                self._grid[cell[0]][cell[1]][3] = False
                self._grid[neighbor[0]][neighbor[1]][2] = False
