import re


def delete_punct_white(list_words_for_line):
    for line in list_words_for_line:
        for ind_word in range(len(line)):
            line[ind_word] = re.sub('[^A-Za-z]', '', line[ind_word])
    return list_words_for_line


def main():
    print(
        'This program reads a file, breaks each line into words, strips whitespace and punctuation from the words, '
        'and converts them to lowercase\n')
    fin = open('esfiletxt.txt')
    list_words_for_line = [line.strip().lower().split() for line in fin]
    print(delete_punct_white(list_words_for_line))


if __name__ == '__main__':
    main()
