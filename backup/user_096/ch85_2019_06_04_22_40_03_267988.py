with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.lower()
    i = 0
    for i in a:
        if i == 'banana':
            i += 1
print(i)
