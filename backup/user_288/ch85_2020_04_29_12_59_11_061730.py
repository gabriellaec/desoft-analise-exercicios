contagem = 0
with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.readline()
    for p in conteudo:
        if p == 'banana' and p == 'Banana' and p == 'BANANA' and p== 'BaNaNa':
            contagem += 1
print (contagem)
            