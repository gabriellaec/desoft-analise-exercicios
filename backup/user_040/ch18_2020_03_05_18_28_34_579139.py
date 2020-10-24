def verifica_idade(x):
    if (21>x>=18):
        return ("Liberado BRASIL")
    elif (x>=21):
        return ("Liberado EUA e BRASIL")
    else:
        return ("Não está liberado")