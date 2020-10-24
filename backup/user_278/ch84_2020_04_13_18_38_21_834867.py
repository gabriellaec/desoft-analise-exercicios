def inverte_dicionario (dic1):
    dic2= {}
    for k in dic1:
        if dic1[k] not in dic2:
            dic2[dic1[k]]= [k]
        else:
            dic2[dic1[k]].append(k)
    return dic2