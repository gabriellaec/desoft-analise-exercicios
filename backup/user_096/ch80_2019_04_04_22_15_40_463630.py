def interseccao_chaves(dicionario1,dicionario2):
    listac = []
    for k1 in dicionario1.keys():
        listac.append(k1)
    for k2 in dicionario2.keys():
        listac.append(k2)
    return listac