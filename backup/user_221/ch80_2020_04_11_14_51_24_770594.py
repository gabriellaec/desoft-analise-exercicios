def interseccao_chaves(dicionario1, dicionario2):
    lista = []
    for k1 in dicionario1.keys():
        for k2 in dicionario2.keys():
                if k1 == k2:
                    lista.append(k1)
    return lista