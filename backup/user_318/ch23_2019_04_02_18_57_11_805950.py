def verifica_idade(x):
    if(x>20):
        s="Liberado EUA e BRASIL"
        print(s)
    if(x>17 and x<21):
        s="Liberado BRASIL"
        print(s)
    if(18>x):
        s="Nao esta liberado"
        print(s)
    return s