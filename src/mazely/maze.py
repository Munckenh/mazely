import random
import sys

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
    seed : int
        The seed value used to initialize the random number generator.
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
        seed: int = random.randrange(sys.maxsize),
        generator: MazeGenerator = RecursiveBacktracking(),
        solver: MazeSolver = ShortestPath(),
    ):
        self.generator = generator
        self.solver = solver
        self.seed = seed

        if path is not None:
            self.load_maze(path)
        else:
            self.rows = rows
            self.columns = columns
            self.grid_size = rows * columns
            self.grid = self.generator.generate(rows, columns, seed=seed)
            self.start = self.get_random_cell()
            self.goal = {self.get_random_cell()}

        self.solution_path = self.solver.solve(
            self.grid, self.start, self.goal)

    @staticmethod
    def are_cells_adjacent(*cells: tuple[int, int]) -> bool:
        """Whether each cell is adjacent to the next.

        Returns
        -------
        bool
            ``True`` if each cell is adjacent to the next. ``False`` if otherwise. Also, ``False`` if only one cell is provided as an argument.
        """
        if len(cells) < 2:
            return False
        for i, cell in enumerate(cells[:-1]):
            if not ((abs(cell[0] - cells[i+1][0]) == 1) ^ (abs(cell[1] - cells[i+1][1]) == 1)):
                return False
        return True

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

            # Initiate store-purpose variables
            goal = []
            start = []

            # Iterate over each possible cell position and update the wall details of the current cell.
            for row in range(self.rows):
                for column in range(self.columns):
                    # If the current cell is the start.
                    if lines[row * 2 + 1][column * 4 + 2] == "S":
                        start.append((row, column))

                    # If the current cell is the goal.
                    elif lines[row * 2 + 1][column * 4 + 2] == "G":
                        goal.append((row, column))

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

            # Update the start attribute
            if len(start) > 0:
                self.start = start[0]
            else:
                self.start = self.get_random_cell()

            # Update the goal attribute
            if len(goal) == 0:
                self.goal = {self.get_random_cell()}
            else:
                self.goal = set()
                self.add_goal_cells(*goal)

    def generate(self, rows: int, columns: int, seed: int = random.randrange(sys.maxsize)):
        """Generate a new maze and overwrite to :attr:`grid`.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.
        seed : int
            The seed value used to initialize the random number generator.
        """
        self.seed = seed
        self.rows = rows
        self.columns = columns
        self.grid_size = rows * columns
        self.grid = self.generator.generate(rows, columns, seed=seed)

    def solve(self):
        """Solve the maze with a specific configuration."""
        self.solution_path = self.solver.solve(
            self.grid, self.start, self.goal)

    def set_start_cell(self, row: int, column: int):
        """Set a cell at a location as a start cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.

        Raises
        ------
        ValueError
            If either row or column is out of range. 
        """
        if row < 0 or row >= self.rows:
            raise ValueError("Row is out of range.")
        if column < 0 or column >= self.columns:
            raise ValueError("Column is out of range.")
        self.start = (row, column)

    def set_goal_cell(self, row: int, column: int):
        """Set a cell at a location as a goal cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.

        Raises
        ------
        ValueError
            If either row or column is out of range. 
        """
        if row < 0 or row >= self.rows:
            raise ValueError("Row is out of range.")
        if column < 0 or column >= self.columns:
            raise ValueError("Column is out of range.")
        self.goal = {(row, column)}

    def add_goal_cell(self, row: int, column: int):
        """Add a cell at a location as a goal cell.

        Parameters
        ----------
        row : int
            The row of a cell.
        column : int
            The column of a cell.

        Raises
        ------
        ValueError
            If either row or column is out of range. 
        """
        if row < 0 or row >= self.rows:
            raise ValueError("Row is out of range.")
        if column < 0 or column >= self.columns:
            raise ValueError("Column is out of range.")
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
