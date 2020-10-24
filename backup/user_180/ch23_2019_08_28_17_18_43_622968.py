def verifica_idade(id):
    if id >= 21:
        print("Liberado EUA e BRASIL")
    elif id < 21:
        if id >=18:
            print("Liberado BRASIL")
        else:
            print("Não está liberado")