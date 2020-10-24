def verifica_idade(x):
    x = int(input(qual sua idade))
    if x >= 21:
        return ("Liberado EUA e BRASIL")
    else:
        if x >= 18:
            return ("Liberado BRASIL")
        else:
            return ("Não está´liberado")
    

