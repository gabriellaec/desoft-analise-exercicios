def agrupa_por_idade(d):
    new_d = {}
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    for k,v in d.items():
        if v <= 11 :
            criança.append(k)
        elif v >= 12 and v <= 17:
            adolescente.append(k)
        elif v >= 18 and v <= 59:
            adulto.append(k)
        elif v >= 60:
            idoso.append(k)
    new_d['criança'] = criança
    new_d['adolescente'] = adolescente
    new_d['adulto'] = adulto
    new_d['idoso'] = idoso
    return new_d