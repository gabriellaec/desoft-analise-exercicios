def verifica_idade(anos):
    if anos >= 21:
        print("Liberado EUA e BRASIL")
    elif anos >=18:
        print("Liberado BRASIL")
    elif anos<18:
        print("Não está liberado")