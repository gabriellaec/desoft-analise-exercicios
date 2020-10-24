def agrupa_por_idade(d):
    faixas =  {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for i in d:
        if d[i] <= 11:
            faixas['criança'] += [i]
        elif d[i] <= 17:
            faixas['adolescente'] += [i]
        elif d[i] <= 59:
            faixas['adulto'] += [i]
        else:
            faixas['idoso'] += [i]
    return faixas