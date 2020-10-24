def agrupa_por_idade(n):
    dic={'criança':[],'adolescente':[],'adulto':[], 'idoso':[]}
    for i,o in n.items():
        if o<=11:
            dic['criança'].append(i)
        elif o<=17:
            dic['adolescente'].append(i)
        elif o<=59:
            dic['adulto'].append(i)
        else:
            dic['idoso'].append(i)
    return dic