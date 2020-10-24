with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.readlines()
for texto in conteudo:
    palavra = texto.lower()
    contador = 0
    if palavra == 'banana':
        contador += 1
print(contador)
    