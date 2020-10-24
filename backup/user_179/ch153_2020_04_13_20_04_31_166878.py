def agrupa_por_idade (dicionario):
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    faixa_etaria = {}
    nome = list(dicionario.keys())
    idade = list(dicionario.values())
    i = 0
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
    faixa_etaria['criança'] = crianca
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso
    return faixa_etaria