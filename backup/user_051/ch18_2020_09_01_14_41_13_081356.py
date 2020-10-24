def verifica_idade(i):
    if i < 18:
        return "Não está liberado"
    if 18<= i < 21:
        return "Liberado BRASIL"
    if i>= 21:
        return "Liberado EUA e BRASIL"