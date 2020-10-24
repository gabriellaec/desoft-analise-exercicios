def verifica_idade(y):
    if y>=21:
        print("Liberado EUA e BRASIL")
    elif y>= 18 and y<21:
        print("Liberado BRASIL")
    elif y<18:
        print("Não está liberado")
    elif y==1:
        print("Não está liberado")