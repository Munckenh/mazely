import numpy as np


class MazeGenerator:
    """A base class for maze-generating algorithms."""

    def __init__(self):
        self._grid = None

    def _remove_wall(self, cell: tuple[int, int], neighbor: tuple[int, int]):
        """Remove the wall between a cell and its neighbor.

        Parameters
        ----------
        cell : tuple[int, int]
            The location of the cell.
        neighbor : tuple[int, int]
            The location of the cell's neighbor.
        """
        if cell[1] == neighbor[1]:  # If both cells share the same column.
            if cell[0] < neighbor[0]:
                self._grid[cell[0]][cell[1]][1] = False
                self._grid[neighbor[0]][neighbor[1]][0] = False
            else:
                self._grid[cell[0]][cell[1]][0] = False
                self._grid[neighbor[0]][neighbor[1]][1] = False

        elif cell[0] == neighbor[0]:  # If both cells share the same row.
            if cell[1] < neighbor[1]:
                self._grid[cell[0]][cell[1]][2] = False
                self._grid[neighbor[0]][neighbor[1]][3] = False
            else:
                self._grid[cell[0]][cell[1]][3] = False
                self._grid[neighbor[0]][neighbor[1]][2] = False

    def _initiate_grid(self, rows: int, columns: int, walls: bool = False):
        """Initiate a two-dimensional list of each cell's wall data.

        The wall data is a list consisting of four Boolean values in NSEW
        order.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.
        walls : bool
            Whether to initiate all the cell with walls. Defaults to ``False``.
        """

        self._grid = np.full((rows, columns, 4), [walls] * 4)

    def generate(
        self,
        rows: int,
        columns: int,
        seed: int | None = None
    ) -> np.ndarray:
        """An abstract method to generate a maze.

        Parameters
        ----------
        rows : int
            The total number of rows of the maze.
        columns : int
            The total number of columns of the maze.
        seed : int, optional
            The seed value used to initialize the random number generator.
            Defaults to ``None``.

        Raises
        ------
        NotImplementedError
            If the method has not been implemented in a subclass.
        """
        raise NotImplementedError(
            "The 'generate()' method must be implemented in the subclass."
        )
