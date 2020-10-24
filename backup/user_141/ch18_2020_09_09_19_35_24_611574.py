def verifica_idade(anos):
    if anos >= 18:
        print("Liberado BRASIL")
    elif anos >= 21:
        print("Liberado EUA e BRASIL")
    else:
        print("Não está liberado")