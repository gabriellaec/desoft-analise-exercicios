def verifica_idade(x):
    if idade < 18:
        return("Não está liberado")
    elif idade < 21:
        return("Liberado BRASIL")
    else:
        return("Liberado EUA e BRASIL")

idade = int(input())

c = verifica_idade(idade)

print(c)