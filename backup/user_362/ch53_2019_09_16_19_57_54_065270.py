def inverte_lista(lista):
    contador=len(lista)-1
    x=[]
    while contador >= 0:
        x.append(lista[contador])
        contador=contador-1
    return x
        