def agrupa_por_idade(dicionario):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    faixaetaria = dict()
    for i, v in dicionario:
        if v <= 11:
            criança.append(k)
        elif v >= 12 and v <= 17:
            adolescente.append(k)
        elif v >=18 and <=59:
            adulto.append(k)
        else:
            idoso.append(k)
    faixaetaria['criança']= criança
    faixaetaria['adolescente'] = adolescente
    faixaetaria['adulto'] = adulto
    faixaetaria['idoso'] = idoso
    return faixaetaria
            
      