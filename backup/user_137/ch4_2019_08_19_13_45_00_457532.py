def classifica_idade(i):
    r = ""
    if i <= 11:
        r = "Crianca"
        return r
    if i >= 12 and i <= 17:
        r = "Adolescente"
        return r
    if i >= 18:
        r = "Adulto"
        return r