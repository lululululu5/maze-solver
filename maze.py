from graphics import Window
from cell import Cell
import time
import random


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit(0, 0, t=True)
        self._break_entrance_and_exit(num_cols-1, num_rows-1, b=True)
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)

        self._animated()

    def _animated(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self, i, j, t=None, r=None, b=None, l=None):
        current_cell = self._cells[i][j]
        if t is not None:
            current_cell.has_top_wall = False
        if r is not None:
            current_cell.has_right_wall = False
        if b is not None:
            current_cell.has_bottom_wall = False
        if l is not None:
            current_cell.has_left_wall = False
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i-1 >= 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append(self._cells[i-1][j])
            if i+1 < self.num_cols:
                if self._cells[i+1][j].visited == False:
                    to_visit.append(self._cells[i+1][j])
            if j-1 >= 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append(self._cells[i][j-1])
            if j+1 < self.num_rows:
                if self._cells[i][j+1].visited == False:
                    to_visit.append(self._cells[i][j+1])
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                print("We are done here!!")
                return

            rand = random.randrange(0, len(to_visit))
            chosen_cell = to_visit.pop(rand)
            if current_cell._x1 < chosen_cell._x1:
                # chosen is right neighbor
                chosen_coordinates = [i+1, j]
                self._break_entrance_and_exit(i, j, r=True)
                self._break_entrance_and_exit(i+1, j, l=True)
            elif current_cell._x1 > chosen_cell._x1:
                # chosen is left neighbor
                chosen_coordinates = [i-1, j]
                self._break_entrance_and_exit(i, j, l=True)
                self._break_entrance_and_exit(i-1, j, r=True)
            if current_cell._y1 < chosen_cell._y1:
                # chosen is bottom neighbor
                chosen_coordinates = [i, j+1]
                self._break_entrance_and_exit(i, j, b=True)
                self._break_entrance_and_exit(i, j+1, t=True)
            elif current_cell._y1 > chosen_cell._y1:
                # chosen is top neighbor
                chosen_coordinates = [i, j-1]
                self._break_entrance_and_exit(i, j, t=True)
                self._break_entrance_and_exit(i, j-1, b=True)
            print(to_visit)
            self._break_walls_r(chosen_coordinates[0], chosen_coordinates[1])
