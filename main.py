from graphics import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 25, 25, 25, 25, win, 12)
    maze.solve()
    win.wait_for_close()


main()
