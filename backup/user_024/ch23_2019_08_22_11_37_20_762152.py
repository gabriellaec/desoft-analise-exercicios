def verifica_idade(pais, idade):
    if idade>=21:
        return "Liberado EUA e Brasil"
    elif idade<18:
        return "Não está liberado"
    else:
        return "Liberado Brasil"