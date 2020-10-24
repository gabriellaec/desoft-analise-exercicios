def verifica_idade(a):
    if a < 18:
        return("Não está liberado")
    elif a >= 21:
        return("Liberado EUA e BRASIL")
    else:
        return("Liberado BRASIL")