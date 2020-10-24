def verifica_idade (x):
    if x>= 21:
        print("Liberado EUA e BRASIL")
        elif x>= 18 and x<21:
            print("Liberado BRASIL")
        elif x>=1 and x < 18:
            print("Não está liberado")