def filtra_positivos(lista):
    i=0
    c = 0
    nova_lista =[]
    while i<len(lista):
        if lista[c] > 0:
            nova_lista.append(lista[c])
        i+=1
        c+=1
    return nova_lista

