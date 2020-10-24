def agrupa_por_idade(d):
    new_d = {}
    for k,v in d.items():
        if v <= 11 and not 'criança' in new_d :
            new_d['criança'] = [k]
        elif v <= 11:
            new_d['criança'].append(k)
        elif v >= 12 and v <= 17 and not 'adolescente' in new_d:
            new_d['adolescente'] = [k]
        elif v >= 12 and v <= 17:
            new_d['adolescente'].append(k)
        elif v >= 18 and v <= 59 and not 'adulto' in new_d :
            new_d['adulto'] = [k]
        elif v >= 18 and v <= 59:
            new_d['adulto'].append(k)
        elif v >= 60 and not 'idoso' in new_d:
            new_d['idoso'] = [k]
        elif v >= 60:
            new_d['idoso'].append(k)
    return new_d