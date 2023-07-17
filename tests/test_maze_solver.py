import pytest

from mazely.algorithms import MazeSolver, ShortestPath


def are_both_cells_adjacent(cell_one: tuple[int, int],
                            cell_two: tuple[int, int]) -> bool:
    """Whether two cell locations are adjacent to each other."""
    if (abs(cell_one[0] - cell_two[0]) == 1) ^ \
            (abs(cell_one[1] - cell_two[1]) == 1):
        return True
    return False


def is_each_cell_adjacent(cells: list[tuple[int, int]]) -> bool:
    """Whether, in a list of cell locations, each cell location is adjacent to
    the next one."""
    for i, cell in enumerate(cells[:-1]):
        if are_both_cells_adjacent(cell, cells[i + 1]) is False:
            return False
    return True


def are_there_duplicates(cells: list[tuple[int, int]]) -> bool:
    """Whether there is a duplicate cell location in a list of cell
    locations"""
    for i, cell in enumerate(cells):
        if cell in cells[i + 1:]:
            return False
    return True


def test_base_maze_solver(grid):
    solver = MazeSolver()
    with pytest.raises(NotImplementedError):
        solver.solve(grid, (0, 0), {(1, 1)})


def test_shortest_path(grid):
    solver = ShortestPath()
    solution_path = solver.solve(grid, (0, 0), {(1, 1)})
    assert is_each_cell_adjacent(solution_path) is True
    assert are_there_duplicates(solution_path) is True

    solution_path_literal = [(0, 0), (1, 0), (2, 0),
                             (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1)]
    assert solution_path == solution_path_literal
