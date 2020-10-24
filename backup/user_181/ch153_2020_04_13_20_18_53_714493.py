def agrupa_por_idade(dicionario):
    nome = dicionario.keys()
    idade = dicionario.values()
    faixa_etaria = dict()
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    if idade <= 11:
        crianca.append(nome)
    if idade > 11 and idade <= 17:
        adolescente.append(nome)
    if idade > 17 and idade <= 59:
        adulto.append(nome)
    if idade > 59:
        idoso.append(nome)
    faixa_etaria['crianca'] = crianca
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso