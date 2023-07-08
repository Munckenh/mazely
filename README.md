<p align="center">
    <img src="https://raw.githubusercontent.com/Munckenh/mazely/main/docs/images/32x128-solution.svg" alt="Solved 32x128 maze">
</p>

# mazely

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](http://choosealicense.com/licenses/mit/)
[![Read the Docs](https://img.shields.io/readthedocs/mazely)](http://mazely.readthedocs.io/)

An API for solving and generating mazes, written in Python.

## Installation

Install `mazely` with [pip](https://pip.pypa.io/en/stable/getting-started/):

```shell
pip install mazely
```

## Documentation

A library reference can be found [here](https://mazely.readthedocs.io/en/latest/).

## Usage examples

Run the Python scripts below from the repository directory.

Also, see the [examples](https://github.com/Munckenh/mazely/tree/main/examples) folder.

### Load and display a maze

Create an instance of `Maze` and pass a path to a maze file to load an existing maze. Use the `show_grid()` method from `Utilities` to display a grid of the maze.

```py
from mazely import Maze, Utilities

maze = Maze(path="resources/2015apec.maze")
utils = Utilities()
utils.show_grid(maze.grid)
```

<p align="center">
    <img src="https://raw.githubusercontent.com/Munckenh/mazely/main/docs/images/2015apec.svg" alt="APEC 2015">
</p>

### Solve a maze and display its solution

A solution is always made when you create an instance of `Maze`. To display the solution, use the `show_solution()` method from `Utilities`.

```py
from mazely import Maze, Utilities

maze = Maze(path="resources/2019japan.maze")
utils = Utilities()
utils.show_solution()
```

<p align="center">
    <img src="https://raw.githubusercontent.com/Munckenh/mazely/main/docs/images/2019japan-solution.svg" alt="Japan 2019">
</p>

### Generate a maze and display its solution

To generate a maze, pass the row and column counts as you create a `Maze` instance. Refer to the previous section to display its solution.

```py
from mazely import Maze, Utilities

maze = Maze(32, 32)
utils = Utilities()
utils.show_solution()
```

<p align="center">
    <img src="https://raw.githubusercontent.com/Munckenh/mazely/main/docs/images/32x32-solution.svg" alt="Solved 32x32 maze">
</p>

## Maze files

The library only supports a single maze format, as specified below.

### File format

Each cell is 3 characters wide and 3 characters tall.

```
+---+
|   |
+---+
```

To specify the goal cell, replace the center with `G`.

```
+---+
| G |
+---+
```

And replace with `S` for the start cell.

```
+---+
| S |
+---+
```

Here is an example of a 3x3 maze.

```
+---+---+---+
|           |
+   +---+   +
|     G |   |
+---+---+   +
| S         |
+---+---+---+
```

### Links

Here are a couple links to collections of maze files (format may not be supported):

- <https://github.com/micromouseonline/mazefiles>
- <http://www.tcp4me.com/mmr/mazes/>
