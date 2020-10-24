def classifica_idade(idade):
    if idade <=11:
        faixa_etaria = 'crianca'
    elif idade <=17:
        faixa_etaria = 'adolescente'
    else:
        faixa_etaria = 'adulto'
    return faixa_etaria