def verifica_idade(x):
    if id < 18:
        return("Não está liberado")
    elif id < 21:
        return("Liberado BRASIL")
    else:
        return("Liberado EUA e BRASIL")

id = float(input('idade :'))

c = verifica_idade(id)

print(c)