import sys


def main():
    # compute first n fibonacci sequence
    first_n_fibo = int(sys.argv[1])
    fibo_list = [0, 1]
    if first_n_fibo <= 2:
        print(fibo_list[:first_n_fibo])
        return
    first_num = 0
    second_num = 1
    for i in range(2, first_n_fibo):
        first_num, second_num = second_num, first_num + second_num
        fibo_list.append(second_num)
    print(fibo_list)


main()
