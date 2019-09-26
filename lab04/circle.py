# Ruoyun Sun:input radius, compute the distance between points in a
# radius x radius grid and the center. If the distance is less than radius,
# print a "o"; else, print a whitespace
import sys
import math


def main():
    '''input radius, compute the distance between points in a radius x radius
     grid and the center. If the distance is less than radius, print a "o";
     else, print a whitespace'''
    radius = int(sys.argv[1])
    for row in range(2 * radius):
        for col in range(2 * radius):
            dist = abs(math.sqrt((row - radius) ** 2 + (col - radius) ** 2))
            if dist < radius:
                print('o', end='')
            else:
                print(' ', end='')
        print()


main()
