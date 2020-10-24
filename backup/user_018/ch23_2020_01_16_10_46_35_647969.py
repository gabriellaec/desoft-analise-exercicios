def verifica_idade(idade):
    if idade>17 and idade<21:
        return 'Liberado BRASIL'
    if idade>20:
        return 'Liberado EUA e BRASIL'
    else:
        return 'Não está liberado'
    