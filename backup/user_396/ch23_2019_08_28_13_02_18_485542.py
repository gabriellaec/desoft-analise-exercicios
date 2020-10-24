def verifica_idade(x):
    if x < 18:
        print("Não está liberado")
    elif x < 21:
        print("Liberado EUA e BRASIL")
    else:
        print("Liberado BRASIL")