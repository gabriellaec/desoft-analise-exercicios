def agrupa_por_idade(dic):
    faixas = {'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for n,i in dic.items():
        if i <= 11:
            faixas['criança'] += [n]
        elif 12 <= i <= 17:
            faixas['adolescente'] += [n]
        elif 18 <= i <= 59:
            faixas['adulto'] += [n]
        else:
            faixas['idoso'] += [n]
    return faixas