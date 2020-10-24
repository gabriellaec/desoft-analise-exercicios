def agrupa_por_idade(pessoa_idade):
    faixa_etaria = {}
    lista_criancas = []
    lista_adolescentes = []
    lista_adultos = []
    lista_idosos = []
    for pessoa, idade in pessoa_idade.items():
        if idade <= 11:
            lista_criancas.append(pessoa)
            faixa_etaria['criança'] = lista_criancas
        if idade >= 12 and idade <= 17:
            lista_adolescentes.append(pessoa)
            faixa_etaria['adolescente'] = lista_adolescentes
        if idade >= 18 and idade <= 59:
            lista_adultos.append(pessoa)
            faixa_etaria['adulto'] = lista_adultos
        if idade >= 60:
            lista_idosos.append(pessoa_idade)
            faixa_etaria['idoso'] = lista_idosos
    return faixa_etaria