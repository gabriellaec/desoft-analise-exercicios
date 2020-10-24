def agrupa_por_idade(dic):
    dic2 = {}
    for i in dic:
        if dic[i] not in dic2:
            if dic[i] <= 11:
                dic2['criança'] = [i]
            if dic[i] >= 12  and dic[i] <= 17:
                dic2['adolescente'] = [i]
            if dic[i] >= 18  and dic[i] <= 59:
                dic2['adulto'] = [i]
            else:
                dic2['idoso'] = [i]
        else:
            if dic[i] <= 11:
                dic2['criança'].append(i)
            if dic[i] >= 12  and dic[i] <= 17:
                dic2['adolescente'].append(i)
            if dic[i] >= 18  and dic[i] <= 59:
                dic2['adulto'].append(i)
            else:
                dic2['idoso'].append(i)
    return dic2