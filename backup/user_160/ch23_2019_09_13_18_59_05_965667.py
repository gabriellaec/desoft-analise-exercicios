def verifica_idade(x):
    if x >= 21:
        return "Liberado EUA e Brasil"
    elif x >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"