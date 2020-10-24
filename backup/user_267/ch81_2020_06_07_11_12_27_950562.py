def interseccao_valores(d1, d2):
    lista = []
    for i in range(0, len(d1)-1, 1):
        for n in range(0, len(d2)-1, 1):
            if d1[i] == d2[n]:
                lista.append(d1[i])
    return lista
            