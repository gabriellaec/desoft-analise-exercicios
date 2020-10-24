lista_palavras = []
i = 0
while True:
    lista_palavras.append(input('Escreva uma palavra: '))
    palavra = list(lista_palavras[i])
    if palavra [0] == 'f' and palavra [1] == 'i' and palavra [2] == 'm':
        del lista_palavras[-1]
        break
    elif palavra [0] == 'a':
        i += 1
    else:
        del lista_palavras[i]
i2 = 0
while i2 < len(lista_palavras):
    print (lista_palavras[i2])
    i2 += 1