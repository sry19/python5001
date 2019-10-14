# Author: Ruoyun Sun
# The program uses the star's segment to draw a star and a circle around the
# star
import turtle
import math


TRIANGLE_DEGREE = 180
TAN_18_DEGREE = 0.325
STAR_SEG = 500
COS_18_DEGREE = 0.951
STAR_DEGREE = 36
STAR_SIDE = 5
CIRCLE_ANGLE = 360


def main():
    '''give the star's segment, draw a star and a circle around star
        None -> None'''
    turtle.hideturtle()
    radius = STAR_SEG / 2 / COS_18_DEGREE
    circle_x, circle_y = 0, -radius
    draw_circle(radius, circle_x, circle_y)
    star_x, star_y = -STAR_SEG / 2, STAR_SEG / 2 * TAN_18_DEGREE
    draw_star(STAR_SEG, star_x, star_y)
    turtle.exitonclick()


def draw_circle(radius, circle_x, circle_y):
    '''use the radius to draw a circle
        radius, x, y -> None'''
    CIRCLE_LINE_COLOR = "blue"
    CIRCLE_FILL_COLOR = "cyan"
    ACCURACY = 400

    turtle.color(CIRCLE_LINE_COLOR, CIRCLE_FILL_COLOR)
    turtle.penup()
    turtle.setposition(circle_x, circle_y)
    turtle.pendown()
    turtle.begin_fill()
    # To simplify, we can use 'turtle.circle(radius)'
    circle(radius, CIRCLE_ANGLE, ACCURACY)
    turtle.end_fill()
    turtle.penup()


def circle(radius, angle, step):
    '''draw a circle. angle usually equals 360. The more steps, the more
        accurate.
        number, number, number -> None'''
    distance = 2 * radius * math.sin(angle / CIRCLE_ANGLE / step * math.pi)
    for i in range(step):
        turtle.left(angle / step)
        turtle.forward(distance)


def draw_star(star_seg, star_x, star_y):
    '''use the star's segments to draw a star
        size, x, y -> None'''
    STAR_LINE_COLOR = 'red'
    STAR_FILL_COLOR = "yellow"

    turtle.pencolor(STAR_LINE_COLOR)
    turtle.penup()
    turtle.setposition(star_x, star_y)
    turtle.pendown()
    turtle.fillcolor(STAR_FILL_COLOR)
    turtle.begin_fill()
    for i in range(STAR_SIDE):
        turtle.forward(star_seg)
        turtle.right(TRIANGLE_DEGREE - STAR_DEGREE)
    turtle.end_fill()
    turtle.penup()


main()
