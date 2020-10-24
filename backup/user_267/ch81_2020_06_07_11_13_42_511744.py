def interseccao_valores(d1, d2):
    lista = []
    n = 0
    for i in range(0, len(d1)-1, 1):
        while n < (len(d2)):
            if d1[i] == d2[n]:
                lista.append(d1[i])
        n += 1
    return lista
            