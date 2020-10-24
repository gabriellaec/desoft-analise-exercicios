def verifica_idade(idade):
    if idade >= 18 < 21:
        print("Liberado BRASIL")
    elif idade > 21:
        print("Liberado EUA e BRASIL")
    else:
        print("Não está liberado")
        