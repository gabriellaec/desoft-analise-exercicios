def verifica_idade(i):
    if i > 17:
        if i >20:
            return "Liberado EUA e BRASIL"
        else:
            return "Liberado BRASIL"
    else:
        return "Não está liberado"