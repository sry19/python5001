from maze import Maze
from game_controller import GameController
from disks import Disks

WIDTH = 400
HEIGHT = 400

game_controller = GameController(WIDTH, HEIGHT)
maze = Maze(WIDTH, HEIGHT, game_controller)



def setup():
    size(WIDTH, HEIGHT)

    
def draw():
    background(6,129,34) 
    maze.display()
    game_controller.update()
    
def mousePressed():
    x = mouseX
    y = mouseY
    maze.add_disk(x, y)
