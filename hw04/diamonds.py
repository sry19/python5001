import sys
import math


def main():
    # draw a diamond
    height = int(sys.argv[1])
    half_height = math.floor((height-1)/2)
    # the width of the longest line
    width = abs(half_height)*2+1
    for i in range(height):
        # the space in the left side
        space_width = math.floor(abs((height-1)/2-i))
        print(' '*space_width, end='')
        print('*'*(width-2*space_width), end='')
        print(' '*space_width)


main()
