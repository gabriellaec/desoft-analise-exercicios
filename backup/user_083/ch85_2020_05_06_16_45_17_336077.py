contador=0
with open('macacos-me-mordam.txt') as arquivo: 
    conteudo=arquivo.readlines()
    if 'banana' in conteudo:
        contador+=1
print(contador)