def inverte_dicionario(dic):
    invertido = dict()
    for i in dic:
        if i not in invertido:
            invertido[dic[i]] = [i]
        else:
            invertido[dic[i]].append(i)
    return invertido