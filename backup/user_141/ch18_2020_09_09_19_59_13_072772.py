def verifica_idade(anos):
    if anos >= 18 and anos < 21:
        return("Liberado BRASIL")
    elif anos >= 21:
        return("Liberado EUA e BRASIL")
    else:
        return("Não está liberado")