def verifica_idade(idade):
    if idade < "18":
        return "Nao esta liberado"
    elif idade >= "21":
        return "Liberado EUA e BRASIL"
    elif idade >="18":
        return "Liberado no BRASIL"
 

print(verifica_idade)



