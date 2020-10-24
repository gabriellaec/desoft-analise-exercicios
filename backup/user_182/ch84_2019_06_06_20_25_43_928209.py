def inverte_dicionario(dic):
    novodic = {}
    for k,i in dic.items():
        if i in novodic:
            novodic[i].append(k)
        else:
            novodic[i]=[k]
    return novodic