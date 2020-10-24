def agrupa_por_idade(d):
    new_d = {}
    for k,v in d.items():
        if v <= 11 :
            new_d['criança'] = [k]
        elif v >= 12 and v <= 17:
            new_d['adolescente'] = [k]
        elif v >= 18 and <= 59 :
            new_d['adulto'] = [k]
        elif v >= 60:
            new_d['idoso'] = [k]
    return new_d