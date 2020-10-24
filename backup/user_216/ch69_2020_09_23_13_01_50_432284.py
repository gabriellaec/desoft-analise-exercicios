def junta_listas(lista):
    nova_lista = []
    i = 0
    while i < len(lista):
        c = 0
        while c < len(lista[i]):
            nova_lista.append(lista[i][c])
            c += 1
        i += 1
    return nova_lista