def agrupa_por_idade(dic):
    dic_f = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
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
        dic_f[v].append(k)
    return dic_f