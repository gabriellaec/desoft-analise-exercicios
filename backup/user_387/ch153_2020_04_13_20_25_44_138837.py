def agrupa_por_idade(idades):
    dic = {'criança':[], 'adolescente':[], 'adulto':[], 'idoso':[]}
    for pessoa in idades:
        if idades[pessoa] <= 11:
            dic['criança'].append(pessoa)
        elif idades[pessoa] >= 12 and idades[pessoa] <= 17:
            dic['adolescente'].append(pessoa)
        elif idades[pessoa] >= 18 and idades[pessoa] <= 59:
            dic['adulto'].append(pessoa)
        elif idades[pessoa] >= 60:
            dic['idoso'].append(pessoa)
    return dic
