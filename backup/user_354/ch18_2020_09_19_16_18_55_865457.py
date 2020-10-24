def verifica_idade(x):
    if x >= 21:
        print("Liberado EUA e BRASIL")
    else:
        if x >= 18:
            print("Liberado BRASIL")
        else:
            print("Não está´liberado")
        print(verifica_idade(10))

