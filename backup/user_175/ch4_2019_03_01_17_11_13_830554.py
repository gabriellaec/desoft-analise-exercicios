def classifica_idade(idade):
    if idade <= 11:
        classificacao = 'crianca'
    elif 12 <= idade <= 17:
        classificacao = 'adolescente'
    else:
        classificacao = 'adulto'
    return classificacao