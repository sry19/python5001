import re


def main():
    # prompts the user for a file name
    filename = input("Enter the file name: ")
    try:
        f = open(filename, "r")
    except:
        print("Can't open", filename)
        return
    count_word, count_chr, count_alnum = 0, 0, 0
    for line in f:
        content = line.strip()

        # count alphanumeric characters (letters and numbers, excluding
        # punctuation)
        count_alnum += len(re.findall('\w', content))

        # count non-whitespace characters (including punctuation)
        count_chr += len(re.findall('\S', content))

        # counts of words
        for i in content.split(' '):
            if len(i) > 0:
                count_word += 1
    print("Words:", count_word)
    print("Characters:", count_chr)
    print("Letters & numbers:", count_alnum)


main()
