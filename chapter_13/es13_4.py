from es13_3 import *


def word_not_in_list(isto, word_to_find):
    new_list = []
    for word in isto.keys():
        if word not in word_to_find:
            new_list.append(word)
    return new_list


def main():
    word_to_find = ['chapter', 'the', 'in']
    fin = open('a_modern_hercules_book.txt')
    list_words_for_line = [line.strip().lower().split() for line in fin]
    list_words = calc_numb_words(delete_punct_white(list_words_for_line))
    print(f'Number of words in the book {len(list_words)}')
    print(
        f'All the words in the book that are not in the word list {word_not_in_list(isto_words(list_words), word_to_find)}')


if __name__ == '__main__':
    main()
