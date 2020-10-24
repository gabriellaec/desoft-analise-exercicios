def agrupa_por_idade(dicionario):
    faixa_etaria = dict()
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    for i in dicionario:
        if dicionario[i] <= 11:
            crianca.append(i)
        if dicionario[i] > 11 and dicionario[i] <= 17:
            adolescente.append(i)
        if dicionario[i] > 17 and dicionario[i] <= 59:
            adulto.append(i)
        if dicionario[i] > 59:
            idoso.append(i)
        faixa_etaria['crianca'] = crianca
        faixa_etaria['adolescente'] = adolescente
        faixa_etaria['adulto'] = adulto
        faixa_etaria['idoso'] = idoso
    return faixa_etaria