from chapter_13.es13_1 import delete_punct_white


def isto_words(list_words):
    isto = {}
    for word in list_words:
        if word not in isto:
            isto[word] = 1
        else:
            isto[word] += 1
    return isto


def calc_numb_words(list_words_for_line):
    new_list = [sub_sublist for sublist in list_words_for_line for sub_sublist in sublist if sublist]
    return new_list


def main():
    print(
        'This program reads a file, breaks each line into words, strips whitespace and punctuation from the words, '
        'and converts them to lowercase\n')
    fin = open('a_modern_hercules_book.txt')
    list_words_for_line = [line.strip().lower().split() for line in fin]
    list_words = calc_numb_words(delete_punct_white(list_words_for_line))
    print(f'Number of words {len(list_words)}')
    print(f'Number of times each word is used: {isto_words(list_words)}')


if __name__ == '__main__':
    main()
