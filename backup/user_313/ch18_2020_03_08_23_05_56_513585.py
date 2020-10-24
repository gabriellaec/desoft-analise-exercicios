def verifica_idade(x):
    if (x >= 18 and x <= 20):
        return("Liberado BRASIL")
    if (x>=21):
        return("Liberado EUA e BRASIL")
    if(x < 18):
        return("Não está liberado")

print(verifica_idade(18))