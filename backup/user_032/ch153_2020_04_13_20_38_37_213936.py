def agrupa_por_idade(dicionario):
    criança = {}
    adolescente = {}
    adulto = {}
    idoso = {}
    for idade in dicionario.values():
        if idade <= 11:
            criança[idade] = dicionario[idade]
        elif idade > 11 and idade < 18:
            adolescente[idade] = dicionario[idade]
        elif idade >= 18 and idade < 60:
            adulto[idade] = dicionario[idade]
        else:
            idoso[idade]=dicionario[idade]
    return criança
    return adolescente
    return adulto
    return idoso