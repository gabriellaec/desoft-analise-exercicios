def verifica_idade(x):
    if(x>20):
        print("Liberado EUA e BRASIL")
    return x
    elif(x>17 and x<21):
        print("Liberado BRASIL")
    return x
    else:
        print("Não está liberado")
    return x    