# Ruoyun Sun: randomly produce username and 3 passwords
from random import randint


# input first name, last name, a favourite word to randomly produce username
# and 3 passwords
def main():
    ''' input first name, last name, a favourite word to randomly produce
        user_name and 3 passwords'''
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    fav_words = input("Please enter your favorite word: ")
    print()

    # The username generated consists of the first letter from the user's first
    # name, followed by the first seven letters from their last name, and a
    # random integer between 0 and 99
    tmp_lastname = last_name + '*******'
    user_ran_num = str(randint(0, 99))
    user_name = first_name[0].lower() + tmp_lastname[:7].lower() + user_ran_num
    print("Thanks " + first_name + ", your user name is " + user_name)
    print()
    print("Here are three suggested passwords for you to consider:")
    print()

    # The first password is the concatenation of the user's first and last
    # names, in lower case, with a random integer in the range 0 – 99 between
    # them. Some of the characters in the resulting string are then replaced
    # by similar-looking digits and punctuation characters.
    pass_1 = first_name.lower() + str(randint(0, 99)) + last_name.lower()
    new_pass1 = ""
    for i in pass_1:
        if i == 'a':
            i = '@'
        elif i == 's':
            i = '$'
        elif i == 'l':
            i = '1'
        elif i == 'o':
            i = '0'
        new_pass1 += i
    print("Password 1:", new_pass1)

    # The second password consists of the first and last character from the
    # user's first name, last name, favorite word. In each case, the first
    # letter of the pair should be lower case and the second should be upper
    # case.
    pass_2 = ''
    for i in [first_name, last_name, fav_words]:
        pass_2 += i[0].lower() + i[-1].upper()
    print("Password 2:", pass_2)

    # The third password takes a random-length portion of the first name,
    # combined with random-length portions of the favorite word and last name
    # (in any order). In each case, those random-length pieces should start at
    # the beginning of the string, and it's possible to get the entire string
    # number is produced. At least one character from each part should appear
    pass_3 = ''
    choose_list = [first_name, last_name, fav_words]
    while choose_list:
        which_first = randint(0, len(choose_list)-1)
        word_now = choose_list[which_first]
        del choose_list[which_first]
        pass_3 += word_now[:randint(1, len(word_now))]
    print("Password 3:", pass_3)


main()
