from collections import deque

import numpy as np

from .maze_solver import MazeSolver


class ShortestPath(MazeSolver):
    """A maze-solving algorithm that finds the shortest path using
    breadth-first search."""

    def __init__(self):
        pass

    def solve(
        self,
        grid: np.ndarray,
        start: tuple[int, int],
        goal: set[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        """Solve the maze.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        start : tuple[int, int]
            The location of the start cell.
        goal : set[tuple[int, int]]
            The location(s) of the goal cell(s).

        Returns
        -------
        list[tuple[int, int]]
            An ordered list of cell locations representing the solution path.
        """
        queue = deque([start])
        visited = set()
        path = {}
        index_delta = ((-1, 0), (1, 0), (0, 1), (0, -1))

        # Loop until the queue is empty.
        while queue:
            # Get the next cell.
            current = queue.popleft()
            # Save the solution path and break the loop if the current cell is
            # the goal.
            if current in goal:
                solution_path = []

                # Loop until the current cell is the start cell.
                while current is not start:
                    # Append current cell to the solution path.
                    solution_path.append(current)

                    # Get the next cell.
                    current = path[current]
                else:
                    solution_path.append(start)

                # Reverse the order of the list to get a proper solution path.
                solution_path.reverse()

                return solution_path

            # Add the current cell to the visited list.
            visited.add(current)

            for direction, wall in enumerate(grid[current[0]][current[1]]):
                if not wall:
                    neighbor = (
                        current[0] + index_delta[direction][0],
                        current[1] + index_delta[direction][1],
                    )

                    # If the neighbor is not in the visited list.
                    if neighbor not in visited:

                        # Add the neighbor to the queue.
                        queue.append(neighbor)

                        # Store the path.
                        path[neighbor] = current
