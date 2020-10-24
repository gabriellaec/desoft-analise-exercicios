def verifica_idade(i):
    if i < 18:
        print("Não está liberado")
    if 18 <= i < 21:
        print("Liberado BRASIL")
    if 21 <= i:
        print("Liberado EUA e BRASIL")
    return i