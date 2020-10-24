with open('macacos-me-mordam.txt') as arquivo: 
    conteudo=arquivo.readlines()
    palavras=conteudo.split()
    contador=0
    if 'banana' in palavras:
        contador+=contador+1
print(contador)