# Author:Ruoyun Sun
# The program receives the user's inputs which are width of the rocket, number
# of squares and a style value and draws a rocket.
import sys
import math


def main():
    '''user input 2 integers and an optional style value in command line and
        draws a rocket
        None -> None '''
    leng = len(sys.argv)
    try:
        width, square_num = int(sys.argv[1]), int(sys.argv[2])
        if leng == 4 and sys.argv[3] == 'striped':
            isstriped = True
        else:
            isstriped = False
    except Exception:
        print("There is at least one invalid input.")
        return
    draw_rocket(width, square_num, isstriped)


def draw_rocket(width, square_num, isstriped):
    '''draw a rocket(nose cone, fuselage, tail) using width, number of squares
        and a style value
        integer, integer, boolean -> None'''
    build_nose_cone(width)
    if isstriped:
        build_fuselage(width, square_num, True)
    else:
        build_fuselage(width, square_num)
    build_tail(width)


def build_nose_cone(width):
    '''build nose cone using width
        integer -> None'''
    row = (width - 1) // 2
    for i in range(row):
        space_wid = (width - 1) // 2 - i
        print(' ' * space_wid, '*' * (width-2*space_wid), sep='')


def build_fuselage(width, square_num, isstriped=None):
    '''build fuselage using width, number of squares, (style value)
        integer, integer, (boolean) -> None'''
    if isstriped:
        for i in range(square_num):
            for j in range(width // 2):
                print('_' * width)
            for j in range(math.ceil(width / 2)):
                print('x' * width)
    else:
        for i in range(square_num):
            for j in range(width):
                print('x' * width)


def build_tail(width):
    '''draw a tail using width
        integer -> None'''
    space_wid = (width + 1) // 4
    for i in range(space_wid, -1, -1):
        print(' ' * i, '*' * (width - 2 * i), ' ' * i, sep='')
    print('*' * width)


main()
