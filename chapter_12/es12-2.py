def main():
    fin = open('..\words.txt')
    for line in fin:
        word = line.strip()
        print(word)


if __name__ == '__main__':
    main()
