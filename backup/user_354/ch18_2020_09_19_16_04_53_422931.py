def verifica_idade(idade):
    if int("idade") >= 21:
        return ("Liberado EUA e BRASIL")
    else:
        if "idade" >= 18:
            return ("Liberado BRASIL")
        else:
            return ("Não está´liberado")
        return
x="qual sua idade"
print( verifica_idade(x))