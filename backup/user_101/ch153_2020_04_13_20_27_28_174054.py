def agrupa_por_idade(dic):
    dic_f = {}
    c = 'criança'
    a = 'adolescente'
    ad = 'adulto'
    i = 'idoso'
    dic_m = {}
    for k, v in dic.items():
        if v <= 11:
            dic_m[k] = c
        elif v <= 17:
            dic_m[k] = a
        elif v <= 59:
            dic_m[k] = ad
        else:
            dic_m[k] = i

    for k, v in dic_m.items():
        if v in dic_f:
            dic_f[v].append(k)
        else:
            dic_f[v] = [k]
    return dic_f