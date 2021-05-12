from es13_2 import *


def most_frequently(isto, n):
    v = []
    for word, times in isto.items():
        v.append((times, word))
    v.sort(reverse=True)
    return v[0:n]


def main():
    print(
        'This program reads a file, breaks each line into words, strips whitespace and punctuation from the words, '
        'and converts them to lowercase\n')
    fin = open('a_modern_hercules_book.txt')
    list_words_for_line = [line.strip().lower().split() for line in fin]
    list_words = calc_numb_words(delete_punct_white(list_words_for_line))
    print(f'Number of words {len(list_words)}')
    print(f'Number of times each word is used: {isto_words(list_words)}')
    print(f'The 20 most frequently used words in the book are {most_frequently(isto_words(list_words), 20)}')


if __name__ == '__main__':
    main()
