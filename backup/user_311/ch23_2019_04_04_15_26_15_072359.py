def verifica_idade(idade):
    if idade >= 21:
        return "Liberado EUA e BRASIL"
    elif idade < 21 and idade >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"

i = 1
print(verifica_idade(i))