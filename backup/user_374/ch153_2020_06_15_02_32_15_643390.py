def agrupa_por_idade(dicionario):
    dic2 = {}
    dic2['criança'] = []
    dic2['adolescente'] = []
    dic2['adulto'] = []

    dic2['idoso'] = []
       
    for k, v in dicionario.items():
        
        if v <= 11:
            if k not in dic2['criança']:
                dic2['criança'] += [k]
        
        elif v >= 12 and v <= 17:
            if k not in dic2['adolescente']:
                dic2['adolescente'] += [k]
        
        elif v >= 18 and v <= 59:
            if k not in dic2['adulto']:
                dic2['adulto'] += [k]
        
        elif v > 59:
            if k not in dic2['idoso']:
                dic2['idoso'] += [k]
    return dic2