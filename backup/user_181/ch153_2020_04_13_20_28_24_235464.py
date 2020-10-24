def agrupa_por_idade(dicionario):
    nome = dicionario.keys()
    idade = dicionario.values()
    faixa_etaria = dict()
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    if idade <= 11:
        faixa_etaria[crianca] = nome
    if idade > 11 and idade <= 17:
        faixa_etaria[adolescente] = nome
    if idade > 17 and idade <= 59:
        faixa_etaria[adulto] = nome
    if idade > 59:
        faixa_etaria[idoso] = nome
    faixa_etaria['crianca'] = crianca
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso
    return faixa_etaria