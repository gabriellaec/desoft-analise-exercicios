def verifica_idade(anos):
    if anos >= 21:
        return 'Liberado EUA e BRASIL'
    elif anos <= 18:
        return 'Não está liberado'
    else:
        return 'Liberado BRASIL'
    

    