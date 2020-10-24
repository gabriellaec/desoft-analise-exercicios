def verifica_idade(idade):
    if idade>= 21 or idade==1:
        print("Liberado EUA e BRASIL")
    elif idade>=18:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")