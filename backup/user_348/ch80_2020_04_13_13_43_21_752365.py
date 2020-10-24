def interseccao_chaves (dicionario_1, dicionario_2):
    lista = []
    for k in dicionario_1.keys() and k in dicionario_2.keys():
        lista.append(k)
        return lista