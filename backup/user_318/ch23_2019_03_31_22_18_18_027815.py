def verifica_idade(x):
    if(x>=21):
        print("Liberado EUA e BRASIL")
    if(x>=18 and x<=20):
        print("Liberado BRASIL")
    if(18>x):
        print("Não está liberado")
    if(x==1):
        print("Não está liberado")
    return x    