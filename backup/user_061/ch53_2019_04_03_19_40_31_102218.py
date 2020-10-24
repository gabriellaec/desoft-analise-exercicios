def inverte_lista(lista):
    invertida = []
    f = len(lista)-1
    while f>=0:
        invertida.append(lista[f])
        f-=1
    return invertida