def agrupa_por_idade(nome):
    faixas_etarias = {
        'crianca' : [],
        'adolescente' : [],
        'adulto' : [],
        'idoso': [],
    }
    for i in range(nome):
        idade= nome.get[i]
        if idade <= '11':
            faixas_etarias['crianca'].append(nome[i])
        elif idade >= '12' and idade <= '17':
            faixas_etarias['adolescente'].append(nome[i])
        elif idade >= '18' and idade <= '59':
            faixas_etarias['adulto'].append(nome[i])
        elif idade >= '60':
            faixas_etarias['idoso'].append(nome[i])
    return faixas_etarias
