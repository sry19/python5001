# Author:Ruoyun Sun
# The program can draw a 2d cube using the size which user input


def main():
    '''use the cube size to draw a cube
        None -> None'''
    x = input("Input cube size (multiple of 2): ")
    while not x.isnumeric() or int(x) % 2:
        x = input("Input cube size (multiple of 2): ")
    draw_2d_cube(int(x))


def draw_2d_cube(cube_size):
    '''input the size of cube, draw a cube
        integer -> None'''
    print(' '*(cube_size//2+1), '+', '--'*cube_size, '+', sep='')
    for i in range(cube_size//2, 0, -1):
        print(' '*i, '/', ' '*int(cube_size*2), '/', ' '*(cube_size//2-i),
              '|', sep='')
    print('+', '--'*cube_size, '+', ' '*(cube_size//2), '|', sep='')
    for i in range(cube_size//2-1):
        print('|', ' '*2*cube_size, '|', ' '*(cube_size//2), '|', sep='')
    print('|', ' '*2*cube_size, '|', ' '*(cube_size//2), '+', sep='')
    for i in range(1, cube_size//2+1):
        print('|', ' '*2*cube_size, '|', ' '*(cube_size//2-i), '/', sep='')
    print('+', '--'*cube_size, '+', sep='')


main()
