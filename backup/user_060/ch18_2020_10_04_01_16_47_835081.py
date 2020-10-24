def verifica_idade(idade):
    if 17<idade<21:
        return "Liberado BRASIL"
    elif idade>20:
        return "Liberado EUA e BRASIL"
    else:
        return "Não está liberado"