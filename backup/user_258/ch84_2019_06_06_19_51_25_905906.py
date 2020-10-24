def inverte_dicionario(dici):
    dic = {}
    lista_nome = []
    for k,v in dici.items():
        if v not in dic:
            dic[v] = k
        else:
            dic[v].append(k)
    return dic
            