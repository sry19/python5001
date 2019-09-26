# Ruoyun Sun: This program checks if the square that the user input is a
# magic square by computing sum of three horizontal rows, three vertical
# columns, and two corner-to-corner diagonals

SQUARE_LEN = 3
STANDARD_SUM = 15
used_list = []


def no_duplicate(one_line):
    '''given one line, check if the digits have already been used before
    or same number appears in the same line more than once'''
    this_line = []
    for num in one_line:
        if int(num) in used_list:
            return False
        if int(num) in this_line:
            return False
        this_line.append(int(num))
    return True


def main():
    '''check if the square that the user input is a magic square by computing
    sum of three horizontal rows, three vertical columns, and two
     corner-to-corner diagonals'''
    square_list = []
    print("Enter a magic number")
    for _ in range(SQUARE_LEN):
        one_line_nums = input()

        # try again if the input does not meet the requirements
        while len(one_line_nums) != SQUARE_LEN or not no_duplicate(
                                                                one_line_nums):
            one_line_nums = input("Enter 3 digits between 1 and 9 \
(without duplicates): \n")
        temp_list = []
        for j in one_line_nums:
            used_list.append(int(j))
            temp_list.append(int(j))
        square_list.append(temp_list)

    # judge whether the square is a magic square or not by computing
    # sum of three horizontal rows, three vertical columns, and two
    # corner-to-corner diagonals
    sum_col = [0] * SQUARE_LEN
    sum_diag, sum_antidiag = 0, 0
    for row in range(SQUARE_LEN):
        sum_row = 0
        for col in range(SQUARE_LEN):
            if col == row:
                sum_diag += square_list[row][col]
            if col + row == SQUARE_LEN - 1:
                sum_antidiag += square_list[row][col]
            sum_col[col] += square_list[row][col]
            sum_row += square_list[row][col]
        if sum_row != STANDARD_SUM:
            print("Not a magic square!")
            return
    for col in sum_col:
        if col != STANDARD_SUM:
            print("Not a magic square!")
            return
    if sum_diag != STANDARD_SUM or sum_antidiag != STANDARD_SUM:
        print("Not a magic square!")
        return
    print("This is a magic square!")


main()
