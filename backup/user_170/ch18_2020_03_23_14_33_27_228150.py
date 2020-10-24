
def verifica_idade(i):
    if i >= 21:
        return "Liberado EUA e BRASIL"
    elif 18 <= i < 21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"