with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.lower()
    b = a.split()
    n = 0
    for e in b:
        if e == 'banana':
            n += 1
    print(n)