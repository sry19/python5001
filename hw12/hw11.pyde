from maze import Maze
from game_controller import GameController
from disks import Disks

WIDTH = 600
GRID_NUM = 8
SIDE_LENGTH = WIDTH / GRID_NUM

game_controller = GameController(WIDTH, GRID_NUM)
maze = Maze(WIDTH, GRID_NUM, game_controller)


def setup():
    size(WIDTH, WIDTH)


def draw():
    background(6, 129, 34)
    maze.display()
    game_controller.update()


def mousePressed():
    x = mouseX // SIDE_LENGTH
    y = mouseY // SIDE_LENGTH
    maze.add_disk(x, y)
