def agrupa_por_idade(pessoa_idade):
    faixa_etaria = {}
    lista_criancas = []
    lista_adolescentes = []
    lista_adultos = []
    lista_idosos = []
    for pessoa, idade in pessoa_idade.items():
        if idade <= 11:
            lista_criancas.append(pessoa)
        if idade >= 12 and idade <= 17:
            lista_adolescentes.append(pessoa)
        if idade >= 18 and idade <= 59:
            lista_adultos.append(pessoa)
        if idade >= 60:
            lista_idosos.append(pessoa)
        faixa_etaria['criança'] = lista_criancas
        faixa_etaria['adolescente'] = lista_adolescentes
        faixa_etaria['adulto'] = lista_adultos
        faixa_etaria['idoso'] = lista_idosos
    return faixa_etaria