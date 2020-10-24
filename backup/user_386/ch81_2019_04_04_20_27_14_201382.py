def interseccao_valores(dic1,dic2):
    lista = []
    c = dic2.values
    for values in dic1.items():
        if values in c:
            lista.append(values)
    return lista