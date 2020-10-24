def inverte_dicionario(dic):
    dic_i = {}
    for k, v in dic.items():
        lista = []
        lista.append(k)
        dic_i[v] = lista
    return dic_i