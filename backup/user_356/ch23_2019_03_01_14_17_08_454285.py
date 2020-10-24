 def verifica_idade(idade):
    if idade>=21:
        return "Liberado EUA e Brasil"
    if idade>=18:
        return "Liberado Brasil"
    else:
        return "Não está liberado"