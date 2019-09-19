from random import randint


def main():

    def guess_number():

        # produce secret number
        secret_number = randint(1, 50)
        print('''Welcome to the Guessing Game!
I picked a number between 1 and 50. Try and guess!''')

        # first guess
        guess_nb = int(input())
        print("You guessed", guess_nb)
        count = 1

        # when guess is wrong
        while guess_nb != secret_number:
            diffe = abs(guess_nb - secret_number)
            print("Your guess is ", end='')
            if diffe <= 1:
                print("scalding hot")
            elif diffe <= 2:
                print("extremely warm")
            elif diffe <= 3:
                print("very warm")
            elif diffe <= 5:
                print("warm")
            elif diffe <= 8:
                print("cold")
            elif diffe <= 13:
                print("very cold")
            elif diffe <= 20:
                print("extremely cold")
            else:
                print("icy freezing miserably cold")
            guess_nb = int(input())
            count += 1

        # print when succeed
        print("Congratulations. You figured it out in", count, end=' ')
        if count == 1:
            print("try")
        else:
            print("tries")
        # use count to judge the performances
        if count == 1:
            print("That was lucky!")
        elif 2 <= count <= 4:
            print("That was amazing!")
        elif 5 <= count <= 6:
            print("That was okay.")
        elif count == 7:
            print("Meh.")
        elif 8 <= count <= 9:
            print("This is not your game.")
        elif count >= 10:
            print("You are the worst guesser I've ever seen.")

    guess_number()


main()
