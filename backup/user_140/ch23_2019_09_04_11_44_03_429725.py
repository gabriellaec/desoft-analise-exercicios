def verifica_idade(i):
    if idade>21:
        return "Liberado EUA e BRASIL"
    if idade<18:
        return "Não está liberado"
    else:
        return "Liberado BRASIL"
        