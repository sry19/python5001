# Ruoyun Sun: input a number in the commond line as height in order to draw a
# diamond
import sys
import math


def main():
    ''' input a number in the commond line as height in order to draw a
        diamond'''
    height = int(sys.argv[1])
    half_height = math.floor((height-1)/2)

    # compute the width of the longest line
    width = abs(half_height)*2+1
    for i in range(height):
        # compute the space in the left side
        space_width = math.floor(abs((height-1)/2-i))
        print(' '*space_width + '*'*(width-2*space_width) + ' '*space_width)


main()
