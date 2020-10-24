def verifica_idade(idade):
    if idade >= 21:
        print("Liberado EUA e BRASIL")
    if idade >= 18 and idade < 21:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")