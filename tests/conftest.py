import json

import pytest

from mazely import Maze, Utilities


# The generated maze:
#     +---+---+---+
#     | S |       |
#     +   +   +   +
#     |   | G |   |
#     +   +---+   +
#     |           |
#     +---+---+---+
@pytest.fixture
def maze():
    maze_ = Maze(3, 3, seed=0)
    maze_.set_start_cell(0, 0)
    maze_.set_goal_cell(1, 1)
    maze_.solve()
    return maze_


@pytest.fixture
def grid(maze):
    return maze.grid


@pytest.fixture
def solution_path(maze):
    return maze.solution_path


@pytest.fixture
def utilities():
    return Utilities()


@pytest.fixture
def hashes():
    with open("tests/baseline/hashes.json", "r") as file:
        return json.load(file)
