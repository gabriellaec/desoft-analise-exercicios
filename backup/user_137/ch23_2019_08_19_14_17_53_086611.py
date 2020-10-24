def verifica_idade(i):
    if i >= 21:
        return print("Liberado EUA e BRASIL")
    elif i >= 18 and i <= 21:
        return print("Liberado BRASIL")
    else:
        return print("Não esta liberado")