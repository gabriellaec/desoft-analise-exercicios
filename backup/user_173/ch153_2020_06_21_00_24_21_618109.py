def agrupa_por_idade(dic):
    dic2 = {'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for nome,idade in dic.items():
        if idade <= 11:
            dic2['criança'].append(nome)
        elif idade >= 12 and idade <= 17:
            dic2['adolescente'].append(nome)
        elif idade >= 18 and idade <= 59:
            dic2['adulto'].append(nome)
        else:
            dic2['idoso'].append(nome)
    return dic2