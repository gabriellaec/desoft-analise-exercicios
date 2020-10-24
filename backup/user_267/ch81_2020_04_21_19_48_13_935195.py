def interseccao_valores(d1, d2):
    i = 0
    lista = []
    for i in range(0, len(d1)-1, 1):
        if d1[i] == d2[i]:
            lista.append(d1[i])
    return lista
            