def verifica_idade(ano):
    if ano < 18:
        return "Não está liberado"
    elif ano >= 18:
        return "Liberado BRASIL"
    elif ano >= 21:
        return "Liberado EUA e BRASIL"