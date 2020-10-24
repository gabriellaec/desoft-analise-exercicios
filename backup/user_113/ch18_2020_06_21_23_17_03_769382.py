def verifica_idade(idade):
    if idade >= 21:
        print("Liberado EUA e BRASIL")
    elif 18<=idade<=20:
        print("Liberado BRASIL")
    elif idade < 18:
        print("Não está liberado")
