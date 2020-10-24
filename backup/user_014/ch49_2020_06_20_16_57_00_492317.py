def inverte_lista(lista):
    inversa = []
    # O primeiro elemento que vamos usar é o último da lista
    i = len(lista) - 1
    # Enquanto o elemento for maior que 0
    while i >= 0:
        # Ele será adicionado na lista
        inversa.append(lista[i])
        # Pega o elemento anterior
        i -= 1
    return inversa