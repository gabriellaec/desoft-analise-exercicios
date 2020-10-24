def agrupa_por_idade(dic):
    dic_a = {'criança:' [], 'adolescente:' [], 'adulto:' [], 'idoso:' []}
    for n,i in dic.items():
        if i <= 11:
            dic_a['criança'] = i
        elif dic[i] <= 17:
            dic_a['adolescente'] = i
        elif dic[i] <= 59:
            dic_a['adulto'] = i
        else:
            dic_a['idoso'] = i
    return dic_a
        