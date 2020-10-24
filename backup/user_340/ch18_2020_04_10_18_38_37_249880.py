def verifica_idade(idade):
    if idade<18:
        return "Não está liberado"
    elif idade<21 and idade>=18:
        return "Liberado no BRASIL"
    else:
        return "Liberado EUA e BRASIL"
