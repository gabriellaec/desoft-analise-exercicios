with open('macacos-me-mordam.txt') as arquivo: 
    conteudo=arquivo.read()
    conteudo=conteudo.split()
contador=0
for palavra in conteudo:
    if palavra=='banana':
        contador+=1
print(contador)