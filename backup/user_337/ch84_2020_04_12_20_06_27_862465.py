def inverte_dicionario(dicionario):
    dic_invertido = {}
    for i in dicionario:
        dic_invertido[dicionario[i]] = i
    return dic_invertido