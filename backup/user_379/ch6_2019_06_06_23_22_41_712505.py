def encontra_maximo(matriz):
    lista=[]
    for i in matriz:
        lista.append(max(i))
    return max(lista)