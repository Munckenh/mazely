import random
import sys

import numpy as np

from .maze_generator import MazeGenerator


class RecursiveBacktracking(MazeGenerator):
    """A maze-generating algorithm that creates a perfect maze using a randomized version of depth-first search."""

    def __init__(self):
        super().__init__()
        self._visited = None

    def _visit_cell(self, row, column):
        """Visit a cell using recursive backtracking.

        Parameters
        ----------
        row : int
            The row of the cell to be visited.
        column : int
            The column of the cell to be visited.
        """
        self._visited.add((row, column))  # Mark current cell as visited

        # Iterate over the four directions in a randomized order
        for row_delta, column_delta in random.sample(
            ((-1, 0), (0, 1), (1, 0), (0, -1)), k=4
        ):
            # Get a random neighbor's row and column
            neighbor = (row + row_delta, column + column_delta)

            # See if the neighbor exists
            if (
                neighbor[0] < 0
                or neighbor[0] >= len(self._grid)
                or neighbor[1] < 0
                or neighbor[1] >= len(self._grid[0])
            ):
                continue

            # See if the neighbor is already visited
            if neighbor in self._visited:
                continue

            # Remove the wall between the current cell and the selected neighbor
            self._remove_wall((row, column), neighbor)

            # Visit the neighbor recursively
            self._visit_cell(neighbor[0], neighbor[1])

    def generate(self, rows: int, columns: int) -> np.ndarray:
        """Generate a maze.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.

        Returns
        -------
        numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        """
        sys.setrecursionlimit(rows * columns)
        self._visited = set()
        self._initiate_grid(rows, columns, walls=True)
        self._visit_cell(random.randrange(rows), random.randrange(columns))
        return self._grid
