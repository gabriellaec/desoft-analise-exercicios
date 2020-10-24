def verifica_idade(i):
    if i<18:
        print("Não está liberado")
    elif i>=21:
        print("Liberado EUA e BRASIL")
    else:
        print("Liberado BRASIL")