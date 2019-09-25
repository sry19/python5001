# User input a symbol that they would like to use to make a rectangle
# and then input the width and height of the rectangle. The program will
# print this kind of rectangle


def main():
    '''User input a symbol that they would like to use to make a rectangle
    and then input the width and height of the rectangle. The program will
    print this kind of rectangle'''
    single_char = input("Please input a single character as symbol: ")
    width = int(input("Please input an integer as the width of the rectangle \
(the integer should be greater than 1): "))
    while width < 2:
        width = int(input("Width should be greater than 1. Please input \
again: "))
    height = int(input("Please input an integer as the height of the rectangle \
(the integer should be greater than 1): "))
    while height < 2:
        height = int(input("Height should be greater than 1. Please input \
again: "))
    for i in range(height):
        print(single_char, end='')
        if i == 0 or i == height - 1:
            print(single_char * (width - 2), end='')
        else:
            print(' ' * (width - 2), end='')
        print(single_char)


main()
