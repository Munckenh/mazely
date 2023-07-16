import hashlib

import pytest

try:
    import cairosvg
except OSError:
    import os
    from ctypes.util import find_library
    library_names = ("cairo-2", "cairo", "libcairo-2")
    for library_name in library_names:
        library_path = find_library(library_name)
        if library_path:
            os.add_dll_directory(os.path.dirname(library_path))
    import cairosvg


@pytest.mark.mpl_image_compare(style="default", hash_library="baseline/hashes.json")
# Run the following to generate a hash of the baseline image and create a PNG file to ensure that the images are as expected:
# $ python -m pytest --mpl-generate-hash-library=hashes.json --mpl-generate-path=.
# To enable image comparison testing, pass `--mpl` when running `pytest`.
# $ pytest --mpl
def test_show_grid(utilities, grid, mocker):
    mocker.patch("matplotlib.pyplot.show")
    utilities.show_grid(grid)
    return utilities._figure


def test_save_grid(utilities, grid, hashes, tmp_path):
    file_path = str(tmp_path / "test_save_grid.svg")
    utilities.save_grid(grid, file_path)

    # Rasterize the SVG file and get the hash of the output.
    file_hash = hashlib.sha256(cairosvg.svg2png(
        url=file_path, background_color="#FFF")).hexdigest()

    assert hashes["tests.test_utilities.test_save_grid"] == file_hash, "Hashes don't match"


@pytest.mark.mpl_image_compare(style="default", hash_library="baseline/hashes.json")
# Run the following to generate a hash of the baseline image and create a PNG file to ensure that the images are as expected:
# $ python -m pytest --mpl-generate-hash-library=hashes.json --mpl-generate-path=.
# To enable image comparison testing, pass `--mpl` when running `pytest`.
# $ pytest --mpl
def test_show_solution(utilities, grid, solution_path, mocker):
    mocker.patch("matplotlib.pyplot.show")
    utilities.show_solution(grid, solution_path)
    return utilities._figure


def test_save_solution(utilities, grid, solution_path, hashes, tmp_path):
    file_path = str(tmp_path / "test_save_solution.svg")
    utilities.save_solution(grid, solution_path, file_path)

    # Rasterize the SVG file and get the hash of the output.
    file_hash = hashlib.sha256(cairosvg.svg2png(
        url=file_path, background_color="#FFF")).hexdigest()

    assert hashes["tests.test_utilities.test_save_solution"] == file_hash, "Hashes don't match"
