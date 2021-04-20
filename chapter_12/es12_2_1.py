from es12_1 import most_frequent

def dict_chrs_words(file_words):
    dict_chrs_words = {}
    for line in file_words:
        word = line.strip()
        group_chrs = tuple(most_frequent(word))
        if group_chrs not in dict_chrs_words:
            group_words = []
            group_words.append(word)
            dict_chrs_words[group_chrs] = group_words
        else:
            group_words.append(word)
            dict_chrs_words[group_chrs] = group_words
    return dict_chrs_words

def main():
    fin = open('words.txt')
    for words in dict_chrs_words(fin).values():
        print(words)


if __name__ == '__main__':
    main()
