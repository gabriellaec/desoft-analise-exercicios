def filtra_positivos ():
    i= 0
    nova= []
    while i < len(lista):
        if lista[i] <= 0:
            i = i + 1
        else:
            nova.append(lista[i])
            i = i + 1
    return nova
            