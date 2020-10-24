with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read().lower().split(' ')
    ocorrencias = 0
    for i in conteudo:
        if i == 'banana':
            ocorrencias += 1
    print(ocorrencias)