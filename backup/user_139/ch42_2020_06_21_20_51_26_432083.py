lista_palavras = []
i = 0
parar = False
while not parar:
    palavra = input('Escreva uma palavra: ')
    lista_palavras.append(palavra)
    if palavra[0] == 'f' and palavra[1] == 'i' and palavra[2] == 'm':
        parar = True
        del lista_palavras[i]
    elif palavra[0] == 'a':
        i += 1
    else:
        del lista_palavras[i]
e = 0
while e < len(lista_palavras):
    print (lista_palavras[e])
    e += 1