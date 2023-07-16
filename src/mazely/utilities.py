import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections, colors, patches


class Utilities:
    """A class to perform maze-related utility functions.

    Attributes
    ----------
    figure : :class:`~matplotlib.figure.Figure`, optional
        A :class:`~matplotlib.figure.Figure` instance.
    axes : :class:`~matplotlib.axes.Axes`, optional
        A :class:`~matplotlib.axes.Axes` instance.
    """

    def __init__(self):
        self.figure: plt.Figure | None = None
        self.axes: plt.Axes | None = None

    @staticmethod
    def _is_whole(number: float):
        if number.is_integer():
            return int(number)
        return number

    def _plot_walls(self, grid: np.ndarray, cell_size: int = 15, line_width: int = 2):
        """Plot the walls of the maze with Matplotlib."""
        line_width = line_width / cell_size
        for row in range(len(grid)):
            for column, walls in enumerate(grid[row]):
                if row == 0 and walls[0]:
                    self.axes.add_patch(patches.Rectangle(
                        (column - line_width / 2, row - line_width / 2), line_width, 1 + line_width, 270, rotation_point=(column, row), color="k"))
                if walls[2]:
                    self.axes.add_patch(patches.Rectangle(
                        (column + 1 - line_width / 2, row + 1 - line_width / 2), line_width, 1 + line_width, 180, rotation_point=(column + 1, row + 1), color="k"))
                if column == 0 and walls[3]:
                    self.axes.add_patch(patches.Rectangle(
                        (column - line_width / 2, row - line_width / 2), line_width, 1 + line_width, 0, rotation_point=(column, row), color="k"))
                if walls[1]:
                    self.axes.add_patch(patches.Rectangle(
                        (column + 1 - line_width / 2, row + 1 - line_width / 2), line_width, 1 + line_width, 90, rotation_point=(column + 1, row + 1), color="k"))
        self.axes.set_xlim(-line_width / 2, len(grid[0]) + line_width / 2)
        self.axes.set_ylim(len(grid) + line_width / 2, -line_width / 2)

    def _initiate_plot(self, size: tuple[int, int] = (8, 8)):
        """Initiate a plot from Matplotlib."""
        self.figure = plt.figure(figsize=size)
        self.axes = plt.axes()
        self.axes.set_aspect("equal")
        self.axes.set_axis_off()

    def show_grid(self, grid: np.ndarray):
        """Display a plot of a rectangular, two-dimensional maze.

        Visualization is done with `Matplotlib <https://matplotlib.org/>`_.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        """
        self._initiate_plot()
        self._plot_walls(grid)
        plt.show()

    def save_grid(
        self, grid: np.ndarray, file_path: str, cell_size: int = 15, line_width: int = 2
    ):
        """Save a maze as an SVG file.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        file_path : str
            A path wherein the SVG file is saved.
        cell_size : int
            The size of each cell in pixels.
        line_width : int
            The width of the wall lines in pixels.
        """
        with open(file_path, "w") as file:
            file.write(
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{cell_size * len(grid[0]) + line_width}" height="{cell_size * len(grid) + line_width}" fill="none" stroke="#000" stroke-width="{line_width}" stroke-linecap="square" style="background-color: #FFF">\n'
            )
            for row in range(len(grid)):
                for column, walls in enumerate(grid[row]):
                    a = self._is_whole(column * cell_size + line_width / 2)
                    b = self._is_whole(row * cell_size + line_width / 2)
                    c = self._is_whole((column + 1) * cell_size + line_width / 2)
                    d = self._is_whole((row + 1) * cell_size + line_width / 2)
                    if row == 0 and walls[0]:
                        file.write(
                            f'\t<line x1="{a}" y1="{b}" x2="{c}" y2="{b}"/>\n')
                    if walls[1]:
                        file.write(
                            f'\t<line x1="{a}" y1="{d}" x2="{c}" y2="{d}"/>\n')
                    if walls[2]:
                        file.write(
                            f'\t<line x1="{c}" y1="{b}" x2="{c}" y2="{d}"/>\n')
                    if column == 0 and walls[3]:
                        file.write(
                            f'\t<line x1="{a}" y1="{b}" x2="{a}" y2="{d}"/>\n')
            file.write("</svg>")

    def show_solution(self, grid: np.ndarray, solution_path: list[tuple[int, int]]):
        """Display a plot of a rectangular, two-dimensional maze and its solution path.

        Visualization is done with `Matplotlib <https://matplotlib.org/>`_.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        solution_path : list[tuple[int, int]]
            An ordered list of cell locations representing the solution path.
        """
        self._initiate_plot()
        self._plot_walls(grid)

        # Add an ordered list of rectangle patches.
        patch_list = []
        for row, column in solution_path:
            patch_list.append(patches.Rectangle((column, -row - 1), 1, 1))

        # Create a value array for the color map.
        values = [i for i in range(len(solution_path))]
        norm = colors.Normalize().autoscale(values)

        # Add the list of patches to a patch collection.
        collection = collections.PatchCollection(patch_list, norm=norm, cmap="RdYlGn")

        # Set the value array of the patches.
        collection.set_array(values)

        # Add the collection to the axes.
        self.axes.add_collection(collection)
        plt.show()

    def save_solution(
        self,
        grid: np.ndarray,
        solution_path: list[tuple[int, int]],
        file_path: str,
        cell_size: int = 15,
        line_width: int = 2,
        colormap: str = "RdYlGn",
    ):
        """Save a maze and its solution as an SVG file.

        For more colormap selection, click `here <https://matplotlib.org/stable/tutorials/colors/colormaps.html>`_.

        Parameters
        ----------
        grid : numpy.ndarray
            A two-dimensional array of cells representing a rectangular maze.
        solution_path : list[tuple[int, int]]
            An ordered list of cell locations representing the solution path.
        file_path : str
            A path wherein the SVG file is saved.
        cell_size : int
            The size of each cell in pixels.
        line_width : int
            The width of the wall lines in pixels.
        colormap : str
            A colormap included with Matplotlib.
        """

        colormap_ = mpl.colormaps[colormap]
        array = np.linspace(0, 1, len(solution_path))
        color_list = list()

        for value in array:
            rgba = colormap_(value)
            color_list.append(colors.to_hex(rgba))

        with open(file_path, "w") as file:
            file.write(
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{cell_size * len(grid[0]) + line_width}" height="{cell_size * len(grid) + line_width}" style="background-color: #FFF">\n'
            )

            for i, cell in enumerate(solution_path):
                file.write(
                    f'\t<path fill="{color_list[i]}" d="M{self._is_whole(cell[1] * cell_size + line_width / 2)} {self._is_whole(cell[0] * cell_size + line_width / 2)}h{cell_size}v{cell_size}h-{cell_size}z"/>\n'
                )
            file.write(
                f'\t<g fill="none" stroke="#000" stroke-width="{line_width}" stroke-linecap="square">\n')
            for row in range(len(grid)):
                for column, walls in enumerate(grid[row]):
                    a = self._is_whole(column * cell_size + line_width / 2)
                    b = self._is_whole(row * cell_size + line_width / 2)
                    c = self._is_whole(
                        (column + 1) * cell_size + line_width / 2)
                    d = self._is_whole((row + 1) * cell_size + line_width / 2)
                    if row == 0 and walls[0]:
                        file.write(
                            f'\t\t<line x1="{a}" y1="{b}" x2="{c}" y2="{b}"/>\n'
                        )
                    if walls[1]:
                        file.write(
                            f'\t\t<line x1="{a}" y1="{d}" x2="{c}" y2="{d}"/>\n'
                        )
                    if walls[2]:
                        file.write(
                            f'\t\t<line x1="{c}" y1="{b}" x2="{c}" y2="{d}"/>\n'
                        )
                    if column == 0 and walls[3]:
                        file.write(
                            f'\t\t<line x1="{a}" y1="{b}" x2="{a}" y2="{d}"/>\n'
                        )
            file.write("\t</g>\n")
            file.write("</svg>")
