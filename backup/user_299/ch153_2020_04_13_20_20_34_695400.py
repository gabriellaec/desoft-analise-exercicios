def agrupa_por_idade(dicio):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    dicionovo = {}
    for nome , idade in dicio.items():
        if idade <= 11:
            crianca.append(nome)
        elif idade <= 17:
            adolescente.apppend(nome)
        elif idade <= 59:
            adulto.append(nome)
        else:
            idoso.append(nome)
    dicionovo['crianças'] = crianca 
    dicionovo['adolescentes'] = adolescente
    dicionovo['adultos'] = adulto
    dicionovo['idosos'] = idoso
    return dicionovo