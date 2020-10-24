def agrupa_por_idade(dicionario):
    nome = dicionario.keys()
    idade = dicionario.values()
    faixa_etaria = dict()
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    if dicionario(nome) <= 11:
        crianca.append(nome)
    if dicionario(nome) > 11 and dicionario(nome) <= 17:
        adolescente.append(nome)
    if dicionario(nome) > 17 and dicionario(nome) <= 59:
        adulto.append(nome)
    if dicionario(nome) > 59:
        idoso.append(nome)
    faixa_etaria['crianca'] = crianca
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso