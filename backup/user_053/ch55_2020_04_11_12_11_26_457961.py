def encontra_maximo(matriz):
    for i in matriz:
        maximo = i[0]
        j = 0
        lista_maximos = []
        while j < len(i):
            if i[j] > maximo:
                maximo = i[j]
                lista_maximos.append(maximo)
                j += 1
            else:
                j += 1
    maximo_matrix = max(lista_maximos)
    return maximo_matrix