def verifica_idade(i):
    if i>=21:
        print("Liberado EUA e BRASIL")
    elif i>=18 and i<21:
        print("Liberado BRASIL")
    elif i<18:
        print("Não está liberado")  