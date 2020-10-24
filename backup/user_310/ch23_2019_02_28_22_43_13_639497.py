def verifica_idade(idade):
    if idade<18:
        print("Não está liberado")
    elif idade>=18 and idade<21:
        print("Liberado BRASIL")
    else:
        print("Liberado EUA e BRASIL")