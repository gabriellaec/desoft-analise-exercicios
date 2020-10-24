def filtra_positivos(lista):
    contador = 0
    while contador < len(lista):
        if lista[contador]<=0:
            del lista[contador]
        contador +=1
    return lista