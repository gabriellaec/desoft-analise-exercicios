def verifica_idade(ano):
    if ano < 18:
        return "Não está liberado"
    elif ano >= 18:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"