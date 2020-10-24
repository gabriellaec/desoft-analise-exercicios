with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
    b = texto.replace('B', 'b')
    a = b.replace('A', 'a')
    c = a.replace('N', 'n')
    bananas = c.count('banana')
    print(bananas)
            