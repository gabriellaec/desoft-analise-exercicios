def inverte_dicionario(dic):
    dic_invertido = {}
    i = 0
    for  k,v in dic.items():
        if  v  not in dic_invertido:
            dic_invertido[v] = [k]
        else:
            dic_invertido[v] += [k]
    return dic_invertido