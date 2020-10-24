def verifica_idade(pais, idade):
    if idade>=21:
        y=1
        return y
    elif idade>=18 and idade <21:
        if pais = "Brasil":
            y=0
            return y
        else:
            y=-1
            return y
    else:
        y=-1
        return y