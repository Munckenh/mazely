import pytest
from mazely import Maze, Utilities
from mazely.algorithms import RecursiveBacktracking


@pytest.fixture
def utilities():
    return Utilities()


@pytest.fixture
def grid():
    generator = RecursiveBacktracking()
    # +---+---+---+
    # |   |       |
    # +   +   +   +
    # |   |   |   |
    # +   +---+   +
    # |           |
    # +---+---+---+
    return generator.generate(3, 3, seed=0)


@pytest.fixture
def maze():
    # maze.grid:
    #   +---+---+---+
    #   |   |       |
    #   +   +   +   +
    #   |   |   |   |
    #   +   +---+   +
    #   |           |
    #   +---+---+---+
    return Maze(3, 3, seed=0)
