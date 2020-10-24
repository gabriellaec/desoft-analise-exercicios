def verifica_idade (idade):
    if 18<=idade<=21:
        return 'Liberado BRASIL'
    elif idade>=21:
        return 'Liberado EUA e BRASIL'
    else:
        return 'não está liberado'