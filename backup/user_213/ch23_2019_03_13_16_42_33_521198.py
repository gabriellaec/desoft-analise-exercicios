def verifica_idade(i):
    if idade<18:
        return "nao esta liberado"
    elif idade>=21:
        return "liberado EUA e BRASIL"
    else:
        return "liberado BRASIL"