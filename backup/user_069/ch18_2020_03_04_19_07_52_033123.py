def verifica_idade (i):
    if i >= 21:
        return("Liberado EUA e BRASIL")
    if i < 18:
        return("Não está liberado")
    else:
        return("Liberado BRASIL")