def classifica_idade(i):
    r = ""
    if i <= 11:
        r = "Crianca"
    if  i >= 12 and i <= 17:
        r = "Adolescente"
    if i >= 18:
        r = "Adulto"
    return r