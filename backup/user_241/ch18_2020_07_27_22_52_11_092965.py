def verifica_idade(idade):
    if  18 =< idade < 21:
        print("Liberado BRASIL")
    elif idade >= 21:
        print("Liberado EUA e BRASIL")
    elif idade < 18:
        print("Não está liberado")
        