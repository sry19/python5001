# compute the triangular number
import sys


def main():
    '''compute the triangular number'''
    input_num = int(sys.argv[1])
    triangular_num = 0
    for i in range(1, input_num+1):
        triangular_num += i
    print(triangular_num)


main()
