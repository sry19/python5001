from random import randint

MAX_SEVEN_DIGIT = 9999999
MIN_VAL = 0
NUM_OF_DIGIT = 7
MAX_MONTH = 12
MAX_DAY = 31


def produce_random():
        n = str(randint(MIN_VAL, MAX_SEVEN_DIGIT))
        return '0000000'[:NUM_OF_DIGIT - len(n)] + n


def dmv():
        # print some prompts
        print("Welcome to the DMV (estimated wait time is 3 hours)")

        # input names and capitalize
        name = input("Please enter your first, middle, and last name:\n")
        first = name[:name.find(' ')]
        last = name[name.rfind(' ') + 1:]
        middle = name[name.find(' ') + 1: name.rfind(' ')]
        first, middle, last = first.capitalize(), \
            middle.capitalize(), last.capitalize()

        # input valid DOB
        month, day, year = input("Enter date of birth \
(MM/DD/YY):\n").split(sep='/')
        while int(month) < 1 or int(month) > MAX_MONTH or \
                int(day) < 1 or int(day) > MAX_DAY:
                month, day, year = input("Enter valid date of \
birth (MM/DD/YY):\n").split(sep='/')
        print("-------------------------------------")

        # output
        print("Washington Driver License")
        print("DL", produce_random())
        print("LN", last)
        print("FN", first, middle)
        print("DOB", month + '/' + day + '/' + year)
        print("EXP", month + '/' + day + '/21')
        print("-------------------------------------")


def main():

        dmv()


main()
