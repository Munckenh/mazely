"""Prints out the hash of the baseline images for `mazely.Utilities.save_grid()` and `mazely.Utilities.save_solution()`"""

import hashlib
import tempfile

from mazely import Maze, Utilities

try:
    import cairosvg
    import os
except OSError:
    import os
    from ctypes.util import find_library
    library_names = ("cairo-2", "cairo", "libcairo-2")
    for library_name in library_names:
        library_path = find_library(library_name)
        if library_path:
            os.add_dll_directory(os.path.dirname(library_path))
    import cairosvg


def svg_to_hash256(file_path: str, verbose: bool = True, _debug: bool = False) -> str:
    file_bytes = cairosvg.svg2png(url=file_path, background_color="#FFF")
    if _debug:
        output = f"{os.path.basename(os.path.splitext(file_path)[0])}.png"
        cairosvg.svg2png(url=file_path, write_to=output,
                         background_color="#FFF")
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    if verbose:
        print(file_hash)
    return file_hash


if __name__ == "__main__":
    maze = Maze(3, 3, seed=0)
    utilities = Utilities()
    maze.set_start_cell(0, 0)
    maze.set_goal_cell(1, 1)
    maze.solve()
    with tempfile.TemporaryDirectory() as tempdir:
        grid_svg = os.path.join(tempdir, "grid.svg")
        solution_svg = os.path.join(tempdir, "solution.svg")
        utilities.save_grid(maze.grid, grid_svg)
        utilities.save_solution(maze.grid, maze.solution_path, solution_svg)
        svg_to_hash256(grid_svg, verbose=True)
        svg_to_hash256(solution_svg, verbose=True)
