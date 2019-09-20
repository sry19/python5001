import random


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
        while int(month) < 1 or int(month) > 12 or \
                int(day) < 1 or int(day) > 31:
            month, day, year = input("Enter valid date of \
birth (MM/DD/YY):\n").split(sep='/')
        print("-------------------------------------")

        # output
        print("Washington Driver License")
        print("DL", random.randint(1000000, 9999999))
        print("LN", last)
        print("FN", first, middle)
        print("DOB", month + '/' + day + '/' + year)
        print("EXP", month + '/' + day + '/21')
        print("-------------------------------------")


def main():

    dmv()


main()
