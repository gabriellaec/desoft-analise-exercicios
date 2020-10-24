def encontra_maximo(matriz):
    valor_max = 0
    e = 0
    while e <= len(matriz):
        i = 0
        lista = matriz[e]
        while i <= 3:
            if lista[i] > valor_max:
                valor_max = lista[i]
                i += 1
            else:
                i += 1
        e += 1
    return valor_max