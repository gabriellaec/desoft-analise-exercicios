def verifica_idade(idade):
    if idade>=21:
        print ("Liberado EUA e BRASIL")
    elif idade>=18 and idade<=20:
        print ("Liberado BRASIL")
    elif idade<=17:
        print ("Não está liberado")