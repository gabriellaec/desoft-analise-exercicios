def verifica_idade(x):
    if x>=21:
        return ("Liberado BRASIL")
    elif x>=18:
        return ("Liberado EUA e BRASIL")
    else:
        return ("Não está liberado")
    