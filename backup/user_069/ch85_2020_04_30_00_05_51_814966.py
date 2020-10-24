with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    s = 0
    for l in lista:
        p = l.lower()
        if p == 'banana':
            s += 1
print(s)
    