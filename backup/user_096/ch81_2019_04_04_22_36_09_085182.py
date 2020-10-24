def interseccao_valores(dicionario1,dicionario2):
    listac = []
    for v1 in dicionario1.values():
        for v2 in dicionario2.values():
            if v1 == v2:
                listac.append(v1)
    return listac