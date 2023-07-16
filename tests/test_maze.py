from pathlib import Path

import numpy as np
import pytest


def test_are_cells_adjacent(maze):
    assert not maze.are_cells_adjacent((0, 0))
    assert maze.are_cells_adjacent((0, 0), (0, 1))
    assert maze.are_cells_adjacent((0, 0), (0, 1), (1, 1))
    assert not maze.are_cells_adjacent((0, 0), (1, 1))
    assert not maze.are_cells_adjacent((0, 0), (0, 1), (1, 2))


def test_load_maze(maze):
    maze.load_maze(Path(__file__).parent.parent /
                   "resources" / "2015apec.maze")
    assert maze.rows == 16
    assert maze.columns == 16
    assert maze.grid_size == 256
    assert maze.start == (15, 0)
    assert maze.goal == {(7, 7)}


def test_set_start_cell(maze):
    maze.set_start_cell(0, 0)
    assert maze.start == (0, 0)

    with pytest.raises(ValueError):
        maze.set_start_cell(-1, 0)
        maze.set_start_cell(0, -1)
        maze.set_start_cell(-10, -1)


def test_set_goal_cell(maze):
    maze.set_goal_cell(0, 0)
    assert maze.goal == {(0, 0)}

    with pytest.raises(ValueError):
        maze.set_goal_cell(-1, 0)
        maze.set_goal_cell(0, -1)
        maze.set_goal_cell(-10, -1)


def test_add_goal_cells(maze):
    maze.set_goal_cell(0, 0)
    maze.add_goal_cells((1, 0), (1, 1))
    assert maze.goal == {(0, 0), (1, 0), (1, 1)}

    with pytest.raises(ValueError):
        maze.add_goal_cells((-1, 0))
        maze.add_goal_cells((0, -1))
        maze.add_goal_cells((-10, -1))


def test_get_random_cell(maze):
    cell = maze.get_random_cell()

    assert len(maze.grid[cell[0]][cell[1]]) == 4


def test_remove_wall(maze):
    assert maze.remove_wall((0, 0), (0, 1))
    assert np.array_equiv(maze.grid[0][0], [True, False, False, True])
    assert np.array_equiv(maze.grid[0][1], [True, False, False, False])

    assert not maze.remove_wall((1, 0), (1, 2))
    assert np.array_equiv(maze.grid[1][0], [False, False, True, True])
    assert np.array_equiv(maze.grid[1][2], [False, False, True, True])
