def agrupa_por_idade(dicio):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    dicionovo = {}
    for nome , idade in dicio.items():
        if idade <= 11:
            criança.append(nome)
        elif idade <= 17:
            adolescente.append(nome)
        elif idade <= 59:
            adulto.append(nome)
        else:
            idoso.append(nome)
    dicionovo['crianças'] = criança 
    dicionovo['adolescentes'] = adolescente
    dicionovo['adultos'] = adulto
    dicionovo['idosos'] = idoso
    return dicionovo