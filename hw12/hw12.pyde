from maze import Maze
from game_controller import GameController

WIDTH = 400
GRID_NUM = 8
GREEN = (6, 129, 34)
YELLOW = (255, 255, 0)
TIME = 90
TIME1 = 50
TEXTSIZE = 30

game_controller = GameController(WIDTH, GRID_NUM)
maze = Maze(WIDTH, GRID_NUM, game_controller)
count = TIME
count1 = TIME1


def setup():
    size(WIDTH, WIDTH)


def draw():
    global count
    global count1

    background(*GREEN)
    maze.display()
    game_controller.update()
    if maze.turn == 'white':
        if count > 0:
            count -= 1
            fill(*YELLOW)
            textSize(TEXTSIZE)
            text('thinking...', WIDTH/2 - 140, 60)
        if count == 0:
            maze.add_disk_ai()
            count = TIME

    if game_controller.game_over and game_controller.once:
        count1 -= 1
        if count1 == 0:
            game_controller.once = False
            game_controller.setup()


def mousePressed():
    if maze.turn == 'black':
        x = mouseX // (WIDTH // GRID_NUM)
        y = mouseY // (WIDTH // GRID_NUM)
        if 0 <= x < GRID_NUM and 0 <= y < GRID_NUM:
            maze.add_disk(x, y)
