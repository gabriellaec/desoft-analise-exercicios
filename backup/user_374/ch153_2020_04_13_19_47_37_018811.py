def agrupa_por_idade(dicionario):
    dic2 = {}
    
    for k, v in dicionario.items():
        
        if v <= 11:
            if 'criança' not in dic2:
                dic2['criança'] = [k]
            else:
                 dic2['criança'] += [k]
        
        elif v <= 12 and v >= 17:
            if 'adolescente' not in dic2:
                dic2['adolescente'] = [k]
            else:
                 dic2['adolescente'] += [k]
    
        elif v >= 18 and v <= 59:
            if 'adulto' not in dic2:
                dic2['adulto'] = [k]
            else:
                 dic2['adulto'] += [k]
        
        elif v > 59:
            if 'idoso' not in dic2:
                dic2['idoso'] = [k]
            else:
                 dic2['idoso'] += [k]
        
        else:
            dic2['criança'] = []
            dic2['adolescente'] = []
            dic2['adulto'] = []
            dic2['idoso'] = []
        
    return dic2
