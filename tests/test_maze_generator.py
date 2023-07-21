import numpy as np
import pytest

from mazely.algorithms import (MazeGenerator,
                               RecursiveBacktracking,
                               RandomizedPrim)


def is_each_seed_unique(generator: MazeGenerator) -> bool:
    """Whether a generator's seed generate a unique grid."""
    grid_one = generator.generate(8, 8, seed=0)
    grid_two = generator.generate(8, 8, seed=0)
    if np.array_equal(grid_one, grid_two) is not True:
        return False
    grid_two = generator.generate(8, 8, seed=1)
    if np.array_equal(grid_one, grid_two) is not False:
        return False
    return True


def is_rectangular(grid: np.ndarray) -> bool:
    """Whether a grid is actually rectangular."""
    if len(grid) < 2 or len(grid[0]) < 2:
        return False
    row_size = len(grid[0])
    for row in grid[1:]:
        if len(row) != row_size:
            return False
    return True


def is_boundary_closed(grid: np.ndarray) -> bool:
    """Whether a grid has a closed boundary."""
    for cell in grid[0]:
        if not cell[0]:
            return False
    for cell in grid[-1]:
        if not cell[1]:
            return False
    for row in grid:
        if not row[-1][2] or not row[0][3]:
            return False
    return True


def has_isolated_cells(grid: np.ndarray) -> bool:
    """Whether a grid has isolated cells."""
    for row in grid:
        for cell in row:
            if cell.all():
                return True
    return False


def test_base_maze_generator():
    generator = MazeGenerator()
    with pytest.raises(NotImplementedError):
        generator.generate(3, 3)


def test_recursive_backtracking():
    generator = RecursiveBacktracking()
    assert is_each_seed_unique(generator)

    grid = generator.generate(3, 3, seed=0)
    assert is_rectangular(grid) is True
    assert is_boundary_closed(grid) is True
    assert has_isolated_cells(grid) is False

    grid_literal = np.array([
        [
            [True, False, True, True],
            [True, False, False, True],
            [True, False, True, False]
        ],
        [
            [False, False, True, True],
            [False, True, True, True],
            [False, False, True, True]
        ],
        [
            [False, True, False, True],
            [True, True, False, False],
            [False, True, True, False]
        ],
    ])
    assert np.array_equal(grid, grid_literal) is True


def test_randomized_prim():
    generator = RandomizedPrim()
    assert is_each_seed_unique(generator)

    grid = generator.generate(3, 3, seed=0)
    assert is_rectangular(grid) is True
    assert is_boundary_closed(grid) is True
    assert has_isolated_cells(grid) is False

    grid_literal = np.array([
        [[True, False,  True,  True],
         [True, False, False,  True],
         [True, False,  True, False]],
        [[False, False, False,  True],
         [False,  True,  True, False],
         [False,  True,  True,  True]],
        [[False,  True, False,  True],
         [True,  True, False, False],
         [True,  True,  True, False]]
    ])
    assert np.array_equal(grid, grid_literal) is True
