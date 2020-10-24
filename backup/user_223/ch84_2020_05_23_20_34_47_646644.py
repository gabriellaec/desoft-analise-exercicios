def inverte_dicionario(dicio):
    dic={}
    for k in dicio.keys():
        if k in dic.keys:
            dic[k] += dicio[k]
        else:
            dic[k] = [dicio[k]]
    return dic