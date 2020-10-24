def verifica_idade(x):
    if(x>=21):
        print("Liberado EUA e BRASIL")
    if(x<21 and x>=18):
        print("Liberado BRASIL")
    if(x<18):
        print("Não está liberado")
  