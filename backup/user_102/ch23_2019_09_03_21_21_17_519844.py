def verifica_idade (x):
    if x < 18:
        print("Não está liberado")
    elif x>= 18 and x<21:
        print("Liberado BRASIL")
    elif x>= 21:
        print("Liberado EUA e BRASIL")
        