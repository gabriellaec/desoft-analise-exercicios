def interseccao_valores(dicio1, dicio2):
    lista_valores = []
    n = 0
    for i in range(0, len(dicio1)-1):
        while n < (len(dicio2)):
            if dicio1[i] == dicio2[n]:
                lista_valores.append(dicio1[i])
            n += 1
    return lista_valores
            