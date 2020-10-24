def inverte_dicionario(dic):
    dic_invertido = {}
    for k,v in dic.items():
        dic_invertido[v] = k
    return dic_invertido 