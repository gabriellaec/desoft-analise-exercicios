def inverte_dicionario(dicionario):
    dic_invertido = {}
    for i in dicionario:
        if dicionario[i] not in dic_invertido:
            dic_invertido[dicionario[i]] = [i]
        else:
            x = dic_invertido[dicionario[i]]
            lista = [x,i]
            dic_invertido[dicionario[i]] =lista
    return dic_invertido