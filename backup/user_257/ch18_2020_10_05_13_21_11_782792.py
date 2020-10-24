verifica_idade= int(input("Digite sua idade? "))

if verifica_idade >= 21: 
    print("Liberado EUA e BRASIL")

elif verifica_idade >= 18 and <= 21:
    print( "Liberado BRASIL")

else :
    print("Não está liberado")

