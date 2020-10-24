def verifica_idade(id):
    if id >=18 and id<21:
        return ("Liberado BRASIL")
    elif id >= 21:
        return ("Liberado EUA e BRASIL")
    else:
        return ("Não está liberado")
    