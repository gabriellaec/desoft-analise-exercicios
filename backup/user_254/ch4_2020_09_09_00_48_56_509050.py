def classifica_idade(idade):
    int(idade)
    if idade <= 11:
        return"crianca"
    elif  12 <= idade <= 17:
        return "adolescente"
    else:
        return "adulto"