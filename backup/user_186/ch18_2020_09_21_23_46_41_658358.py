def verifica_idade (x):
    y=x
    if (x>=21):
        return ("Liberado EUA e BRASIL")
    elif (x>=18 and x<21):
        return ("Liberado BRASIL")
    else :
        return ("Não está liberado")