def verifica_idade(idade):
    if idade >= 18 and idade<21:
        return "Liberado BRASIL"
    elif idade >=21:
        return "Liberado EUA e BRASIL"
    else:
        return "Não está liberado"