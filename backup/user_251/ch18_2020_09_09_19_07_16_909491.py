def verifica_idade(a):
    if a < 18:
        return "Não está liberado"
    else:
        if a >= 18 and a < 21:
            return "Liberado Brasil"
        else:
            return "Liberado EUA e Brasil"



print(verifica_idade(18))
print(verifica_idade(20))
print(verifica_idade(21))            