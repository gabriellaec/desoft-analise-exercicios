def agrupa_por_idade(dic):
    dic_a = {'criança': , 'adolescente': [], 'adulto': [], 'idoso': []}
    for n,i in dic.items():
        if i <= 11:
            dic_a['criança'] = n
        elif i <= 17:
            dic_a['adolescente'] = n
        elif i <= 59:
            dic_a['adulto'] = n
        else:
            dic_a['idoso'] = n
    return dic_a
        