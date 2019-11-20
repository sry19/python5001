from maze import Maze
from game_controller import GameController
from disks import Disks

BOARD_LENGTH = 400
GRID_LENGTH = 100


game_controller = GameController(BOARD_LENGTH, BOARD_LENGTH)
maze = Maze(BOARD_LENGTH, BOARD_LENGTH, game_controller)



def setup():
    size(BOARD_LENGTH, BOARD_LENGTH)

    
def draw():
    background(6,129,34) 
    maze.display()
    game_controller.update()
    
def mousePressed():
    x = mouseX // GRID_LENGTH
    y = mouseY // GRID_LENGTH
    maze.add_disk(x, y)
