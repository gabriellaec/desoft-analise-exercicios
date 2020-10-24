def verifica_idade(n):
    if n >= 21:
        print ("Liberado EUA e BRASIL")
    elif n < 18:
        print ('Não está liberado')
    elif n >= 18 and n < 21:
        print ("Liberado BRASIL")