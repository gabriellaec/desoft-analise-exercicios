def verifica_idade(n):
    if n >= 21:
        return "Liberado EUA e BRASIL"
    else:
        if n >= 18:
            return "Liberado BRASIL"
        else:
            return "Não está liberado"