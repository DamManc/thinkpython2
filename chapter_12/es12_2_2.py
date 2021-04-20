from es12_2_1 import dict_chrs_words

def main():
    fin = open('words.txt')
    v = []
    for chrs, words in dict_chrs_words(fin).items():
        v.append((len(words), words))
    v.sort(reverse=True)
    for freq, words in v:
        print(words)


if __name__ == '__main__':
    main()