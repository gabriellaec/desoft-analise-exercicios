def verifica_idade(idade):
    if idade >= 21:
        return "liberado EUA e BRASIL"
    elif idade >= 18:
        return "liberado BRASIL"
    else idade >= 0 and idade <= 17:
        return "não está liberado"
    