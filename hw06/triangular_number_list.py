# Author:Ruoyun Sun
# The program repeatedly prompts the user for numbers (until the user inputs
# 'done') and adds the corresponding triangular number to a list. When the
# user finally inputs 'done' the full list is printed out.


def main():
    '''input a integer to get its triangular number or input 'done' to end
        the program.
        None -> None'''
    res = []
    x = input("Enter a number, or enter 'done': ")
    while x != 'done':
        tri_num = triangular_number(int(x))
        print("The triangular number for", str(x), "is", str(tri_num))
        res.append(tri_num)
        x = input("Enter another number, or enter 'done': ")
    print(res)


def triangular_number(input_num):
    '''compute the triangular number
        integer -> integer'''
    triangular_num = 0
    for i in range(1, input_num+1):
        triangular_num += i
    return triangular_num


main()
