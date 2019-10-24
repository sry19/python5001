from text_cleaner import TextCleaner
import sys
N = 10


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
    tc.print_out_uni(N)
    tc.print_out_bi(N)
    tc.print_out_tri(N)


main(sys.argv[1])
