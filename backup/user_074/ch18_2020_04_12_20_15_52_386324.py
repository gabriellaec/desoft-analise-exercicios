def  verifica_idade(i):
    if i>=21:
        print ("Liberado EUA e BRASIL")
    if i>=18 and i<21:
        print ("Liberado BRASIL")
    else:
        print("Não está liberado")