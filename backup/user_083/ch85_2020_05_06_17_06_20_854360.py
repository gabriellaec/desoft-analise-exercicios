with open('macacos-me-mordam.txt') as arquivo: 
    contador=0
    conteudo=arquivo.readlines()
    conteudo=conteudo.split()
    for palavra in conteudo:
        if palavra=='banana':
            contador+=1
print(contador)