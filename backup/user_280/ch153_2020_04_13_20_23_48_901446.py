def agrupa_por_idade(idades):
    faixas_etarias = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome in idades:
        if idades[nome] <= 11:
            faixas_etarias['criança'].append(nome)
        if idades[nome] >= 12 and idades[nome] <= 17:
            faixas_etarias['adolescente'].append(nome)
        if idades[nome] >= 18 and idades[nome] <= 59:
            faixas_etarias['adulto'].append(nome)
        if idades[nome] >= 60:
            faixas_etarias['idoso'].append(nome)
    return faixas_etarias