def interseccao_valores(dicionario1, dicionario2):
    lista = []
    for v1 in dicionario1.values():
        for v2 in dicionario2.values():
                if v1 == v2:
                    lista.append(v1)
    return lista