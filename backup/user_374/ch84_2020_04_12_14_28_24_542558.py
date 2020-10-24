def inverte_dicionario(teste):
    dic = {}
    for k, v in teste.items():
            if v not in dic:
                dic[v] = [k]
            else:
                dic[v] += [k]
    return dic