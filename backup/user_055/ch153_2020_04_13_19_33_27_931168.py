def agrupa_por_idade(pessoa_idade):
    faixa_etaria = {}
    for pessoa, idade in pessoa_idade.items():
        if idade <= 11:
            faixa_etaria['criança'] = pessoa
        if idade >= 12 and idade <= 17:
            faixa_etaria['adolescente'] = pessoa
        if idade >= 18 and idade <= 59:
            faixa_etaria['adulto'] = pessoa
        if idade >= 60:
            faixa_etaria['idoso'] = pessoa
    return faixa_etaria