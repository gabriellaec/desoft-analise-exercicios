lista_palavras = []
indice = 0

while True:
    lista_palavras.append(str(input('Escreva uma palavra: ')))
    palavra = list(lista_palavras[indice])
    if palavra[0] == 'f' and palavra[1] == 'i' and palavra[2] == 'm':
        del lista_palavras[-1]
        break
    elif palavra[0] == 'a':
        indice = indice + 1
    else:
        del lista_palavras[indice]

indice2 = 0
while indice2 < len(lista_palavras):
    print (lista_palavras[indice2])
    indice2 = indice2 + 1