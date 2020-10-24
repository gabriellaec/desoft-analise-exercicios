def verifica_idade(x):
    if x>=21:
        return 'Liberado EUA e BRASIL'
    elif x<16:
        return 'Não está liberado'
    else:
        return 'Liberado BRASIL'