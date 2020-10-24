def agrupa_por_idade(dic):
    dic_f = {}
    c = 'criança'
    a = 'adolescente'
    ad = 'adulto'
    i = 'idoso'
    for k, v in dic.items():
        if v <= 11:
            del dic[k]
            dic[k] = c
        elif v <= 17:
            del dic[k]
            dic[k] = a
        elif v <= 59:
            del dic[k]
            dic[k] = ad
        else:
            del dic[k]
            dic[k] = i
    for k, v in dic.items():
        if v in dic_f:
            dic_f[v].append(k)
        else:
            dic_f[v] = [k]
    return dic_f