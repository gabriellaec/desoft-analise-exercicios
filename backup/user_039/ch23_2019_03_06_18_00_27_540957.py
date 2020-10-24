def verifica_idade(anos):
    if anos<18:
        return "Não esta liberado"
    elif 18<anos<21:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"