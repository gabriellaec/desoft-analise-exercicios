def agrupa_por_idade (dicionario_inicial):
    dicionario_final = {}
    lista_crianças = []
    lista_adolescentes = []
    lista_adultos = []
    lista_idosos = []
    for nome, idade in dicionario_inicial.items():
        if idade <= 11:
            faixa_etaria = 'criança'
            lista_crianças.append(nome)
        elif idade>= 12 and idade <= 17:
            faixa_etaria = 'adolescente'
            lista_adolescentes.append(nome)
        elif idade>= 18 and idade <= 59:
            faixa_etaria = 'adulto'
            lista_adultos.append(nome)
        else:
            faixa_etaria = 'idoso'
            lista_idosos.append(nome)
    dicionario_final['criança'] = lista_crianças
    dicionario_final['adolescente'] = lista_adolescentes
    dicionario_final['adulto'] = lista_adultos
    dicionario_final['idoso'] = lista_idosos
    return dicionario_final