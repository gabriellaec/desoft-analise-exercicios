def verifica_idade(idade):
    return idade

if idade >= 21: 
    return("Liberado EUA e BRASIL")

elif idade >= 18 and verifica_idade <= 21:
    return( "Liberado BRASIL")

else :
    return("Não está liberado")

