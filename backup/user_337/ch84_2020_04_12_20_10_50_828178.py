def inverte_dicionario(dicionario):
    dic_invertido = {}
    for i in dicionario:
        if dicionario[i] not in dic_invertido:
            dic_invertido[dicionario[i]] = i
        else:
            x = dic_invertido[dicionario[i]]
            dic_invertido[dicionario[i]] = [x] + [i]
    return dic_invertido