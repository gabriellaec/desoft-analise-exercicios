def verifica_idade(idade):
    if idade>=21:
        return "Liberado EUA e BRASIL"
    elif 18<=idade<21:
        return "Liberado BRASIL"
    elif 0<idade<=17:
        return "Nao esta liberado"
