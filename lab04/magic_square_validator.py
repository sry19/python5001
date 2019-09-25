

SQUARE_LEN = 3
used_list = []


def no_duplicate(one_line):
    for num in one_line:
        if int(num) in used_list:
            return False
    return True


def main():
    square_list = []
    print("Enter a magic number")
    for _ in range(SQUARE_LEN):
        one_line_nums = input()
        while len(one_line_nums) != SQUARE_LEN or not no_duplicate(
                                                                one_line_nums):
            one_line_nums = input("Enter 3 digits between 1 and 9 \
(without duplicates): \n")
        temp_list = []
        for j in one_line_nums:
            used_list.append(int(j))
            temp_list.append(int(j))
        square_list.append(temp_list)
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
        if sum_row != 15:
            print("Not a magic square!")
            return
    for col in sum_col:
        if col != 15:
            print("Not a magic square!")
            return
    if sum_diag != 15 or sum_antidiag != 15:
        print("Not a magic square!")
        return
    print("This is a magic square!")


main()
