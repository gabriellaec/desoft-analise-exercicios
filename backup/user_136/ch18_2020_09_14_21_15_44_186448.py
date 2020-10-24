def verifica_idade(idade):
    if idade >= 21:
        return "liberado EUA e BRASIL"
    elif idade >= 18:
        return "liberado BRASIL"
    elif idade < 18:
        return "não está liberado"
    