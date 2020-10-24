def agrupa_por_idade (dicionario):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    i = 0
    nomes = list(dicionario.keys())
    idades = list(dicionario.values())
    while i < len(dicionario):
        if idade[i] <= 11:
            crianca.append(nome[i])
            i = i + 1
        elif idade[i] > 12 and idade[i] <= 17:
            adolescente.append(nome[i])
            i = i + 1
        elif idade[i] > 18 and idade[i] <= 59:
            adulto.append(nome[i])
            i = i + 1
        else:
            idoso.append(nome[i])
            i = i + 1
    dicionario['crianca'] = crianca
    dicionario['adolescente'] = adolescente
    dicionario['adulto'] = adulto
    dicionario['idoso'] = idoso