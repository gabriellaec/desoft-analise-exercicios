def verifica_idade(anos):
    if anos >= 21:
        return 'Liberado EUA e BRASIL'
    elif anos >= 18 and anos <21:
        return 'Liberado Brasil'
    else:
        return 'Não esta liberado'
    

    