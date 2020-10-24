with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    contagem = 0
    for p in conteudo:
        if p == 'banana' and p == 'Banana':
            contagem += 1
print (contagem)
            