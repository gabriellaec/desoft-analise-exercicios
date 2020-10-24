def inverte_dicionario(dic):
    novo_dic = {}
    for k in dic.keys():
        v = dic[k]
        if v not in novo_dic.keys():
            novo_dic[v] = []
        novo_dic[v].append(k)
    return novo_dic