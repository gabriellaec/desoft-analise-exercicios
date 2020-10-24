def verifica_idade (x):
    if x >= 21:
        return ("Liberado EUA e BRASIL")
    elif 18 <= x <= 21:
        return ("Liberado BRASIL")
    else:
        return ("Não está liberado")