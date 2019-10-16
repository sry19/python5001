# Author:Ruoyun Sun
# implement luhn's Algorithm to chexk if an account number is valid
DIVISOR = 10
FIR_2_DIGIT = 10


def main():
    '''input an account number, check if it is valid
        None -> None'''
    acc_num = input("Please input an account number: ")
    while not acc_num.isnumeric():
        acc_num = input("Please input a number：")
    if len(acc_num) == 1:
        print("The account number", acc_num, "is not valid")
        return
    ori_num = acc_num
    acc_num = list(acc_num)
    luhn_algo(acc_num)
    if is_valid(acc_num):
        print("The account number", ori_num, "is valid")
    else:
        print("The account number", ori_num, "is not valid")


def luhn_algo(acc_num):
    '''Beginning with the second to right-most digit, modify every other digit
         moving from right to left as follows:
                1.Double the digit's value.
                2.If the resulting number is a two digit number, add the first
                 digit of that value to the second digit, yielding a single
                  digit number.
        list -> None'''
    for i in range(len(acc_num)-2, -1, -2):
        num = 2 * int(acc_num[i])
        if num >= FIR_2_DIGIT:
            str_num = str(num)
            num = int(str_num[0]) + int(str_num[1])
        acc_num[i] = num


def is_valid(acc_num):
    '''If the resulting sum is evenly divisible by 10, the sequence is valid.
     If the resulting sum is not divisible by 10, the sequence is not valued
        list -> Boolean'''
    sums = 0
    for i in range(len(acc_num)):
        sums += int(acc_num[i])
    return not sums % DIVISOR


main()
