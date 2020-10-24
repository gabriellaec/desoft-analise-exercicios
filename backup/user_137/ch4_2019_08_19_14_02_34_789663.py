def classifica_idade(i):
    r = ""
    if i <= 11:
        r = "crianca"
    if  i >= 12 and i <= 17:
        r = "adolescente"
    if i >= 18:
        r = "Adulto"
    return r