def classifica_idade (anos):
    if anos <= 11:
        return "crianca"
    elif 12< anos <=17:
        return "adolescente"
    else anos >= 18:
        return "adulto"