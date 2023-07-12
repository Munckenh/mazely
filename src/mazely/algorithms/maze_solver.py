import numpy as np


class MazeSolver:
    """A base class for maze-solving algorithms."""

    def solve(self, grid: np.ndarray, start: tuple[int, int], goal: set[tuple[int, int]]):
        """An abstract method to solve a maze.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        start : tuple[int, int]
            The location of the start cell.
        goal : set[tuple[int, int]]
            The location(s) of the goal cell(s).

        Raises
        ------
        NotImplementedError
            If the method has not been implemented in a subclass.
        """
        raise NotImplementedError(
            "The 'solve()' method must be implemented in the subclass."
        )
