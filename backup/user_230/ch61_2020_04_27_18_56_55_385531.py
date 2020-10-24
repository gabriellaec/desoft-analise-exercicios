def filtra_positivos (lista):
    nova_lista=[]
    for i in range(0, len(lista)):
        if lista[i]>=0:
            nova_lista.append(lista[i])
    return nova_lista