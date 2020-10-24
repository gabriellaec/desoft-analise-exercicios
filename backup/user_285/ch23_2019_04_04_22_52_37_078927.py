def verifica_idade(idade):
    if idade >= 20:
        return "liberado EUA e BRASIL"
    else:
        if idade >= 18:
            return "liberado BRASIL"
        else:
            return "não está liberado"
        