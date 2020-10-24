def encontra_maximo(matriz):
    lista = []
    for i in matriz:
        for v in i:
            lista.append(abs(v))
    return max(lista)