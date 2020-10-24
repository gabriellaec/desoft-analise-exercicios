def inverte_dicionario(dic):
    dic2 = {}
    for nome in dic.keys():
        if dic[nome] in dic2.keys():
            dic2[dic[nome]] = [dic2[dic[nome]], nome]
        else:
            dic2[dic[nome]] = [nome]
    return dic2  
