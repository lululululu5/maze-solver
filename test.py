import unittest
from unittest.mock import patch

from graphics import Window
from maze import Maze
from cell import Cell


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_cell_initialization(self):
        num_cols = 12
        num_rows = 10
        win = Window(300, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        # m1._create_cells()
        for row in m1._cells:
            for cell in row:
                self.assertIsInstance(cell, Cell)
                self.assertEqual(cell._win, win)

    def test_draw_cell(self):
        num_cols = 2
        num_rows = 2
        win = Window(300, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._create_cells()
        with patch.object(Cell, 'draw', return_value=None) as mock_draw:
            m1._draw_cell(0, 0)
            mock_draw.assert_called_once_with(0, 0, 10, 10)


if __name__ == "__main__":
    unittest.main()
