def verifica_idade(a):
    if a < 18:
        return "Não está liberado"
    else:
        if a >= 18 and a < 21:
            return "Liberado BRASIL"
        else:
            return "Liberado EUA e BRASIL"



print(verifica_idade(18))
print(verifica_idade(21))
            