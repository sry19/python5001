# Author:Ruoyun Sun
# The program adds 2 numbers which the user input, outputs the result and
# count the carries when carry is 1
BASE = 10


def main():
    '''input 2 numbers and print their addition result and number of carries
        None -> None'''
    fir_num = input("Enter the first number: ")
    while not fir_num.isnumeric():
        fir_num = input("Enter the first number(must be an integer): ")
    sec_num = input("Enter the second number: ")
    while not sec_num.isnumeric():
        sec_num = input("Enter the second number(must be an integer): ")
    count_carry, res_str = add_str(fir_num, sec_num)
    print(fir_num, '+', sec_num, '=', res_str)
    print("Number of carries:", count_carry)


def add_str(num_str_1, num_str_2):
    '''convert two strings to lists and pass them to find_count,
        function find_count will return number of carries and their sum
        string, string -> number, string'''
    fir_num_lst = list(num_str_1)
    sec_num_lst = list(num_str_2)
    count_carry, res_str = find_count(fir_num_lst, sec_num_lst)
    return count_carry, res_str


def find_count(fir_num_lst, sec_num_lst):
    '''find the addition of two numbers(lists), return number of carries
        and result
        list, list -> number, string'''
    i = -1
    carry = 0
    res_str = ''
    count_carry = 0
    while i >= -len(fir_num_lst) or i >= -len(sec_num_lst) or carry:
        if i >= -len(fir_num_lst):
            carry += int(fir_num_lst[i])
        if i >= -len(sec_num_lst):
            carry += int(sec_num_lst[i])
        res_str = str(carry % BASE) + res_str
        carry = carry // BASE
        if carry == 1:
            count_carry += 1
        i -= 1
    return count_carry, res_str


main()
