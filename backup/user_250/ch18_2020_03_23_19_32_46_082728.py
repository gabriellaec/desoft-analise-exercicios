def verifica_idade(y):
    if y >= 21:
        return("Liberado EUA e BRASIL")
    elif y >= 18 and y < 21:
        return("Liberado BRASIL")
    elif y < 18:
        return("Não está liberado")