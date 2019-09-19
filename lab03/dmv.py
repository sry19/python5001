import random

def main():

    def dmv():
        print("Welcome to the DMV (estimated wait time is 3 hours)")
        first_bf, middle_bf, last_bf = input("Please enter your first, middle, and last name:\n").split(sep = ' ')
        first, middle, last = first_bf.capitalize(), middle_bf.capitalize(), last_bf.capitalize()
        month, day, year = input("Enter date of birth (MM/DD/YY):\n").split(sep = '/')
        print("-------------------------------------")
        print("Washington Driver License")
        print("DL", random.randint(1000000, 9999999))
        print("LN", last)
        print("FN", first, middle)
        print("DOB", month + '/' + day + '/' + year)
        print("EXP", month + '/' + day + '/21')
        print("-------------------------------------")


    dmv()


main()