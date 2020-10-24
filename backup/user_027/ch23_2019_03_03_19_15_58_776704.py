def verifica_idade(x):
    if int(x) >= 21:
        return "Liberado EUA e BRASIL"
    elif int(x) >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"