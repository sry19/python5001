from text_cleaner import TextCleaner
import sys


def main(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError:
        print(file_name, 'is not found')
        return
    tc = TextCleaner()
    for line in f:
        line = tc.pre_process(line.strip())
        for sentence in line.split('.'):
            tc.separate_sentences(sentence)
    tc.count_uni_word()
    tc.count_bi_word()
    tc.count_tri_word()


main(sys.argv[1])
