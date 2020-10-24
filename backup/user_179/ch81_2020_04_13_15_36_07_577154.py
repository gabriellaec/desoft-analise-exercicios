def interseccao_valores (d1,d2):
    d1_valores = list(d1.values())
    d2_valores = list(d2.values())
    lista = []
    i = 0
    while i < len(d1_valores):
        if d1_valores[i] in d2_valores:
            lista.append(d1_valores[i])
            i = i + 1
        else:
            i = i + 1
    return lista