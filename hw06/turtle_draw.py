# Author: Ruoyun Sun
# The program uses the star's segment to draw a star and a circle around the
# star
import turtle


TRIANGLE_DEGREE = 180
TAN_18_DEGREE = 0.325
STAR_SEG = 500
COS_18_DEGREE = 0.951
STAR_DEGREE = 36
STAR_SIDE = 5


def main():
    '''give the star's segment, draw a star and a circle around star
        None -> None'''
    turtle.hideturtle()
    radius = STAR_SEG / 2 / COS_18_DEGREE
    draw_circle(radius)
    draw_star(STAR_SEG)
    turtle.exitonclick()


def draw_circle(radius):
    '''use the radius to draw a circle
        number -> None'''
    CIRCLE_LINE_COLOR = "blue"
    CIRCLE_FILL_COLOR = "cyan"

    turtle.color(CIRCLE_LINE_COLOR, CIRCLE_FILL_COLOR)
    turtle.penup()
    turtle.setposition(0, -radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


def draw_star(star_seg):
    '''use the star's segments to draw a star
        integer -> None'''
    STAR_LINE_COLOR = 'red'
    STAR_FILL_COLOR = "yellow"

    turtle.pencolor(STAR_LINE_COLOR)
    turtle.penup()
    turtle.setposition(-star_seg / 2, star_seg / 2 * TAN_18_DEGREE)
    turtle.pendown()
    turtle.fillcolor(STAR_FILL_COLOR)
    turtle.begin_fill()
    for i in range(STAR_SIDE):
        turtle.forward(star_seg)
        turtle.right(TRIANGLE_DEGREE - STAR_DEGREE)
    turtle.end_fill()
    turtle.penup()


main()
