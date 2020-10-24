def verifica_idade (age):
    if age < 18:
        return "Não está liberado"
    elif age < 21:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"
