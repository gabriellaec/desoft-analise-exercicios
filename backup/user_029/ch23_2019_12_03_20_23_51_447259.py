def verifica_idade(idade):
    if idade < 18:
        return 'Não está liberado'
    if 18 <= idade < 21:
        return 'Liberado BRASIL'
    if idade >= 21:
        return 'Liberado EUA e BRASIL'
