def agrupa_por_idade(dicionario_nome_idade):
    dicionario_faixa_etaria_nome = {'criança': None, 'adolescente': None, 'adulto': None, 'idoso':None}
    lista_criancas = []
    lista_adolescentes = []
    lista_adultos = []
    lista_idosos = []
    idade_max_crianca = 11
    idade_max_adolescente = 17
    idade_max_adulto = 59
    for nome, idade in dicionario_nome_idade.items():
        if idade <= idade_max_crianca:
            lista_criancas.append(nome)
        elif idade_max_crianca < idade <= idade_max_adolescente:
            lista_adolescentes.append(nome)
        elif idade_max_adolescente < idade <= idade_max_adulto:
            lista_adultos.append(nome)
        else:
            lista_idosos.append(nome)
    dicionario_faixa_etaria_nome['criança'] = lista_criancas
    dicionario_faixa_etaria_nome['adolescente'] = lista_adolescentes
    dicionario_faixa_etaria_nome['adulto'] = lista_adultos
    dicionario_faixa_etaria_nome['idoso'] = lista_idosos
    return dicionario_faixa_etaria_nome