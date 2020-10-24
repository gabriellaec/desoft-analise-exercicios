def verifica_idade(x):
    if 21<=x:
        return 'Liberado EUA e BRASIL'
    elif 18<=x:
        return 'Liberado BRASIL'
    else:
        return 'Não está liberado'
    