.. currentmodule:: mazely

Usage Examples
==============

Examples of use.

Load and display a maze
-----------------------

Create an instance of :class:`Maze` and pass a path to a maze file to load an existing maze. Use the :meth:`~Utilities.show_grid()` method from :class:`Utilities` to display a grid of the maze.

.. code-block:: python
    :linenos:

    from mazely import Maze, Utilities

    maze = Maze(path="resources/2015apec.maze")
    utils = Utilities()
    utils.show_grid(maze.grid)

.. image:: images/2015apec.svg
    :alt: APEC 2015
    :align: center

Solve a maze and display its solution
-------------------------------------

A solution is always made when you create an instance of :class:`Maze`. To display the solution, use the :meth:`~Utilities.show_solution()` method from :class:`Utilities`.

.. code-block:: python
    :linenos:

    from mazely import Maze, Utilities

    maze = Maze(path="resources/2019japan.maze")
    utils = Utilities()
    utils.show_solution()

.. image:: images/2019japan-solution.svg
    :alt: Japan 2019
    :align: center

Generate a maze and display its solution
----------------------------------------

To generate a maze, pass the row and column counts as you create a :class:`Maze` instance. Refer to the previous section to display its solution.

.. code-block:: python
    :linenos:

    from mazely import Maze, Utilities

    maze = Maze(32, 32)
    utils = Utilities()
    utils.show_solution()

.. image:: images/32x32-solution.svg
    :alt: Solved 32x32 maze
    :align: center