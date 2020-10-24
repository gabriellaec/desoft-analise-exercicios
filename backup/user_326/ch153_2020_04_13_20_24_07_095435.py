def agrupa_por_idade(dicionario_nome_idade):
    dicionario_faixa_etaria_nome = {}
    idade_max_crianca = 11
    idade_max_adolescente = 17
    idade_max_adulto = 59
    for nome, idade in dicionario_nome_idade.items():
        if idade <= idade_max_crianca:
            dicionario_faixa_etaria_nome['criança'] += nome
        elif idade_max_crianca < idade <= idade_max_adolescente:
            dicionario_faixa_etaria_nome['adolescente'] += nome
        elif idade_max_adolescente < idade <= idade_max_adulto:
            dicionario_faixa_etaria_nome['adulto'] += nome
        else:
            dicionario_faixa_etaria_nome['idoso'] += nome
    return dicionario_faixa_etaria_nome