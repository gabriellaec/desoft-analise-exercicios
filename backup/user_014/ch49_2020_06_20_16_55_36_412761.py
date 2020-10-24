def inverte_lista(lista):
    inversa = []
    # O primeiro elemento que vamos usar é o último da lista
    i = len(lista) - 1
    while i >= 0:
        inversa.append(lista[i])
        i -= 1
    return inversa