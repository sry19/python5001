from maze import Maze
from game_controller import GameController
from disks import Disks

GRID_NUMBER = 4
GRID_LENGTH = 100
GREEN = (6, 129, 34)


game_controller = GameController(GRID_NUMBER * GRID_LENGTH,
                                 GRID_NUMBER * GRID_LENGTH)
maze = Maze(GRID_NUMBER * GRID_LENGTH, GRID_NUMBER * GRID_LENGTH,
            game_controller)


def setup():
    size(GRID_NUMBER * GRID_LENGTH, GRID_NUMBER * GRID_LENGTH)


def draw():
    background(*GREEN)
    maze.display()
    game_controller.update()


def mousePressed():
    x = mouseX // GRID_LENGTH
    y = mouseY // GRID_LENGTH
    maze.add_disk(x, y)
