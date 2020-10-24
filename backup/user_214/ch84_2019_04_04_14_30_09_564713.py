def inverte_dicionario(dic):
    dic_inverso={}
    for a in dic:
        if dic[a] in dic_inverso:
            dic_inverso[dic[a]]=dic_inverso[dic[a]] + ", "+a
        else:
            dic_inverso[dic[a]]=a
    return dic_inverso