def classifica_idade(idade):
    if idade <= 11:
        return 'Crianca'
    elif 12 <= idade < 18:
        return 'Adolescente'
    else:
        return 'Adulto'