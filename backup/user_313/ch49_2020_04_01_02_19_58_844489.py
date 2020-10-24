def inverte_lista(l1):
    a = len(l1)
    contador = 0
    indice = a
    novaLista = [0]*a

    while contador != a:
        novaLista[contador]=l1[indice-1]

        contador = contador + 1
        indice = indice - 1

    return novaLista


lista1 = [1,2,3,4]