from graphics import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(0, 0, 15, 15, 25, 25, win)

    win.wait_for_close()


main()
