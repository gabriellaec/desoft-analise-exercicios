def verifica_idade(x):
    if x<=18:
        print ("Não está liberado")
    if 18<x<21:
        print ("Liberado BRASIL")
    if x>=21:
        print ("Liberado BRASIL E EUA")
print(verifica_idade(43))