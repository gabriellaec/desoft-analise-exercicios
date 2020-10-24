def numero_no_indice (lista):
    x = len(lista)
    nova_lista = [0]
    for n in range (x):
        if lista[n] == n:
            nova_lista.append(lista[n])
    return nova_lista