def verifica_idade(x):
    if(x>=21):
        print("Liberado EUA e BRASIL")
    return x
    if(x<21 and x>=18):
        print("Liberado BRASIL")
    return x
    if(x<18):
        print("Não está liberado")
    return x
  