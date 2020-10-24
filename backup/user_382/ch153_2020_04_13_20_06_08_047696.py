def agrupa_por_idade(dic):
    dic2 = {'criança':[], 'adolescente':[], 'adulto':[], 'idoso':[]}
    for i in dic:
        if dic[i] <= 11:
            dic2['criança'].append(i)
        elif dic[i] >= 12  and dic[i] <= 17:
            dic2['adolescente'].append(i)
        elif dic[i] >= 18  and dic[i] <= 59:
            dic2['adulto'].append(i)
        else:
            dic2['idoso'].append(i)
    return dic2