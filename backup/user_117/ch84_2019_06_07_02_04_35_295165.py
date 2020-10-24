def inverte_dicionario(entrada):
    dic = {}
    for k , v in entrada.items():
        if v not in dic:
            dic[v] = []
        else dic[v].append(k)
    return dic