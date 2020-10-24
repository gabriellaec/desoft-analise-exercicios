def interseccao_chaves (dicionario_1, dicionario_2):
    lista = []
    for k in dicionario_1.keys() and j in dicionario_2.keys():
        if k == j:
            lista.append(k)
            return lista