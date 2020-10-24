with open('macacos-me-mordam.txt') as arquivo: 
    contador=0
    conteudo=arquivo.readlines()
    for contador in conteudo:
        conteudo_lower=contador.lower()
        conteudo_capitalize=contador.capitalize()
        conteudo_1=contador.lower().capitalize()
        conteudo_split=contador.split()
    for palavra in conteudo:
        if palavra=='banana':
            contador+=1
print(contador)