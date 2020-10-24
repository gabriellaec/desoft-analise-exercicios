def agrupa_por_idade(nome):
    faixas_etarias = {
        'crianca' : [],
        'adolescente' : [],
        'adulto' : [],
        'idoso': [],
    }
    for i in range(nome):
        idade= int(nome.get[i])
        if idade <= 11:
            faixas_etarias['crianca'].append(nome)
        elif idade >= 12 and idade <= 17:
            faixas_etarias['adolescente'].append(nome)
        elif idade >= 18 and idade <= 59:
            faixas_etarias['adulto'].append(nome)
        elif idade >= 60:
            faixas_etarias['idoso'].append(nome)
    return faixas_etarias

