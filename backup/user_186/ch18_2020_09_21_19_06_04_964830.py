def verifica_idade (x):
    y = x
    if (x>=21):
        print ("Liberado EUA e BRASIL")
    elif (x>=18 or x<20):
        print ("Liberado BRASIL")
    else :
        print ("Não está liberado")