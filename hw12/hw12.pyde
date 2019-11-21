from maze import Maze
from game_controller import GameController

WIDTH = 400
GRID_NUM = 4
SIDE_LENGTH = WIDTH / GRID_NUM
GREEN = (6, 129, 34)
YELLOW = (255, 255, 0)
TIME = 100
TEXTSIZE = 40

game_controller = GameController(WIDTH, GRID_NUM)
maze = Maze(WIDTH, GRID_NUM, game_controller)
count = TIME

def setup():
    size(WIDTH, WIDTH)


def draw():
    global count
    background(*GREEN)
    maze.display()
    game_controller.update()
    if maze.turn == 'white':
        if count > 0:
            count -= 1
            fill(*YELLOW)
            textSize(TEXTSIZE)
            text('thinking...', WIDTH/2 - 140, 50)
        if count == 0:
            maze.add_disk_ai()
            count = TIME

def mousePressed():
    if maze.turn == 'black':
        x = mouseX // SIDE_LENGTH
        y = mouseY // SIDE_LENGTH
        maze.add_disk(x, y)
