def verifica_idade(idade):
    if idade<18:
        return("não esta liberado")
    elif idade<21:
        return("Liberado BRASIL")
    else:
        return("Liberado EUA e BRASIL")
print(verifica_idade(21))
