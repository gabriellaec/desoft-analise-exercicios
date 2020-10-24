def agrupa_por_idade(dicionario):
    faixa_etaria = dict()
    for i in dicionario:
        if dicionario[i] <= 11:
            faixa_etaria['crianca'] = i
        if dicionario[i] > 11 and dicionario[i] <= 17:
            faixa_etaria['adolescente'] = i
        if dicionario[i] > 17 and dicionario[i] <= 59:
            faixa_etaria['adulto'] = i
        if dicionario[i] > 59:
            faixa_etaria['idoso'] = i
    return faixa_etaria