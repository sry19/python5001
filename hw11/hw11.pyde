from maze import Maze
from game_controller import GameController

WIDTH = 600
HEIGHT = 600

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
    while not maze.disks.is_valid(maze.turn, x//100, y//100):
        rect(3, 2, 5, 5)
        x = mouseX
        y = mouseY
    maze.add_disk(x, y) 
