def classifica_idade(i):
    if i <= 11:
        return "Crianca"
    if i >= 12 and i <= 17:
        return "Adolescente"
    if i >= 18:
        return "Adulto"