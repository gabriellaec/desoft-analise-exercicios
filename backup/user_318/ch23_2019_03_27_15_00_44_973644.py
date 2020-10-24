def verifica_idade(x):
    if(x>20):
        print("Liberado EUA e BRASIL")
    return x
    if(x<21 and x>17):
        print("Liberado BRASIL")
    return x
    if(x<18):
        print("Nao esta liberado")
    return x    