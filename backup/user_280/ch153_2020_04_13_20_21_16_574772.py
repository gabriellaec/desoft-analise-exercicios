def agrupa_por_idade(idades):
    faixas_etarias = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome in idades:
        if idades[nome] <= 11:
            faixas_etarias['criança'] = nome
        if idades[nome] >= 12 and idades[nome] <= 17:
            faixas_etarias['adolescente'] = nome
        if idades[nome] >= 18 and idades[nome] <= 59:
            faixas_etarias['adulto'] = nome
        if idades[nome] >= 60:
            faixas_etarias['idoso'] = nome
    return faixas_etarias