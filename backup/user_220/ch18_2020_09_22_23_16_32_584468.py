def verifica_idade(ano):
    if ano >= 21:
        return "Liberado EUA e BRASIL"
    elif ano >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"