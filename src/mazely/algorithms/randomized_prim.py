import random

import numpy as np

from .maze_generator import MazeGenerator


class RandomizedPrim(MazeGenerator):
    """A maze-generating algorithm that creates a perfect maze using a
    randomized version of Prim's algorithm."""
    def __init__(self):
        super().__init__()

    def generate(
        self,
        rows: int,
        columns: int,
        seed: int | None = None
    ) -> np.ndarray:
        """Generate a maze.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.
        seed : int, optional
            The seed value used to initialize the random number generator.
            Defaults to ``None``

        Returns
        -------
        numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        """
        random.seed(seed)
        self._initiate_grid(rows, columns, walls=True)

        # Get a random cell and mark it as a passage.
        passage_cell = (random.randrange(rows), random.randrange(columns))
        passage = {passage_cell}

        # Add the walls of the cell to the wall list.
        # The wall is represented as a pair of adjacent cells.
        wall_list = []
        for neighbor in self._get_neighbors(passage_cell):
            wall_list.append((neighbor, passage_cell))

        # While the wall list is empty.
        while len(wall_list) > 0:
            # Get a random wall and remove it from the wall list.
            current_cell, passage_cell = random.choice(wall_list)
            wall_list.remove((current_cell, passage_cell))

            # If one of the cells is not a passage.
            if current_cell not in passage:
                # Mark the cell as a passage.
                passage.add(current_cell)

                # Open up the wall in the grid.
                self._remove_wall(current_cell, passage_cell)

                # Add the neighboring walls of the cell to the wall list.
                for neighbor in self._get_neighbors(current_cell):
                    if neighbor not in passage:
                        wall_list.append((neighbor, current_cell))

        return self._grid
