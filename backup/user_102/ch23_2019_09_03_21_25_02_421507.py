def verifica_idade (x):
    if x>= 21:
        print("Liberado EUA e BRASIL")
    elif x>= 18 and x<21:
        print("Liberado BRASIL")
    else:
        print("Não está liberado")