def most_frequent(s):
    # creo un instogramma dizionario
    table = {}
    for ch in s:
        if ch not in table:
            table[ch] = 1
        else:
            table[ch] += 1
    # creo una lista di tuple invertendo x e freq in modo poi da ordinarla in base al valore numerico
    v = []
    for x, freq in table.items():
        v.append((freq, x))
    # ordino in modo descescente
    v.sort(reverse=True)
    # creo la lista result con solo i valori chiave
    res = []
    for freq, x in v:
        res.append(x)
    print(res)


def main():
    print('Enter a word')
    s = input()
    most_frequent(s)


if __name__ == '__main__':
    main()
