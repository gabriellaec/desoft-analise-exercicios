def verifica_idade(i):
    if i >= 21:
        return ("Liberado EUA e BRASIL")
    elif i >= 18:
        return ("Liberado BRASIL")
    else:
        return ("Não está liberado")
x = int(input("Qual sua idade?"))
print (verifica_idade(x))