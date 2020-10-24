def verifica_idade(idade):
    if idade >= 21:
        print ("Liberado EUA e BRASIL")
    elif 21>=idade>=18:
        print ("Liberado BRASIL")
    elif idade<=18:
        print ("Não está liberado")
        
