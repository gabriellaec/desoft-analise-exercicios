def agrupa_por_idade(dicionario):
    faixa_etaria = {}
    crianca = []
    faixa_etaria['crianca'] = crianca
    adolescente = []
    faixa_etaria['adolescente'] = adolescente
    adulto = []
    faixa_etaria['adulto'] = adulto
    idoso = []
    faixa_etaria['idoso'] = idoso
    for nome,idade in dicionario.items():
        if dicionario[nome] <= 11:
            crianca.append(nome)
            faixa_etaria['crianca'] = crianca
        if 12 <= dicionario[nome] <= 17:
            adolescente.append(nome)
            faixa_etaria['adolescente'] = adolescente
        if 18 <= dicionario[nome] <= 59:
            adulto.append(nome)
            faixa_etaria['adulto'] = adulto
        if 60 <= dicionario[nome]:
            idoso.append(nome)
            faixa_etaria['idoso'] = idoso
    return faixa_etaria
print(agrupa_por_idade( {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}))