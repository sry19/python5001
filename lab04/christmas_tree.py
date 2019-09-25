# input a number which means the length of the base of the tree, then we can
# draw a christmas tree


def main():
    '''input a number which means the length of the base of the tree, then we
        can draw a christmas tree'''
    tree_base = int(input("Please input an odd number which is greater than \
1: "))
    while tree_base % 2 == 0 or tree_base < 3:
        tree_base = int(input("Please input an odd number which is greater \
than 1: "))
    tree_height = (tree_base + 1) // 2  # compute the height of the tree
    for i in range(tree_height):
        space_width = (tree_base - 1) // 2 - i  # compute length of left space
        print(' ' * space_width, end='')
        if i == 0:
            print('*')
        else:
            print("/", end='')
            if i == tree_height - 1:
                print("_" * (tree_base - 2), end='')
            else:
                print(' ' * (2 * i - 1), end='')
            print("\\")


main()
