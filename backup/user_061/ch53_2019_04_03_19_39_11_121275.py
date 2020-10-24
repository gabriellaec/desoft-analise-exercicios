def inverte_lista(lista):
    invertida = []
    f = len(lista)
    while f>=0:
        invertida.append(lista[f])
        f-=1
    return invertida