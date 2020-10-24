def verifica_idade(a):
    if a >= 21:
        print("Liberado EUA e BRASIL")
    elif a < 21 and a >= 18:
        print("Liberado Brasil")
    else:
        print("Não está liberado")
    return (verifica_idade)