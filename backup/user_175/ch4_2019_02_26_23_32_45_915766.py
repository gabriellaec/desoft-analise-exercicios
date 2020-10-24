def classifica_idade(idade):
    if idade <= 11:
        classificacao = 'Crianca!'
    elif 12 <= idade <= 17:
        classificacao = 'Adolescente!'
    else:
        classificacao = 'Adulto!'
    return classificacao