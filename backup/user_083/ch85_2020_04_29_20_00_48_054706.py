with open('macacos-me-mordam.txt') as arquivo: 
    conteudo=arquivo.read()
    palavras=conteudo.split()
    contador=0
    if 'banana' in palavras:
        contador+=1
print(contador)