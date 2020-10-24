def inverte_dicionario(entrada):
    dic = {}
    for k , v in entrada.items:
        if v not in dic:
            dic[v] = []
        dic[v].append(k)
    return dic