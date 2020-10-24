def verifica_idade(x):
    if x <=17:
        print("Não está liberado")
    elif x >= 18 and x <= 21:
        print("Liberado BRASIL")
    else:
        print("Liberado EUA e BRASIL")