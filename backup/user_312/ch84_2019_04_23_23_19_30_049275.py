def inverte_dicionario(dicionario):
    contador=0
    dic2={}
    for i, k in dicionario.items():
        if i not in dic2:
            dic2[i] = [k]
        if i in dic2:
            dic2[i].append(k)
    return dic2