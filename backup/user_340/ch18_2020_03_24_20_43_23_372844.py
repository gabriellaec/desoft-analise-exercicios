def verifica_idade(idade):
    if idade<18:
        return "Não está liberado"
    if idade>=18 and idade<21:
        return "Liberado no BRASIL"
    else:
        return "Liberado EUA e BRASIL"
