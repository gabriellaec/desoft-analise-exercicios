def agrupa_por_idade(dic):
    dic_f = {}
    c = 'criança'
    a = 'adolescente'
    ad = 'adulto'
    i = 'idoso'
    for v in dic.values():
        if v <= 11:
            v = c
        elif v <= 17:
            v = a
        elif v <= 59:
            v = ad
        else:
            v = i
    for k, v in dic.items():
        if v in dic_f:
            dic_f[v].append(k)
        else:
            dic_f[v] = [k]
    return dic_f