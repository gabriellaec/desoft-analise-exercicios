def verifica_idade(idade):
    if idade > 21:
        print("Liberado EUA e BRASIL")
    elif idade > 18 and idade < 21:
        print("Librado BRASIL")
    elif idade < 18:
        print("Não está liberado")