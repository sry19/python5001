

def main():

    def capitalized_vowels():
        vowels = ['a', 'e', 'i', 'o', 'u']
        x = input("Please input a string:")
        new_x = ''
        # lower and upper
        for i in x:
            if i.lower() in vowels:
                new_x += i.upper()
            else:
                new_x += i.lower()
        print(new_x)

    capitalized_vowels()


main()
