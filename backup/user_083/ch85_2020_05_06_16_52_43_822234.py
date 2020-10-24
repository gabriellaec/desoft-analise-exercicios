with open('macacos-me-mordam.txt') as arquivo: 
    contador=0
    conteudo=arquivo.readlines()
    for i in conteudo:
        conteudo_lower=i.lower()
    for palavra in conteudo:
        if palavra=='banana':
        contador+=1
print(contador)