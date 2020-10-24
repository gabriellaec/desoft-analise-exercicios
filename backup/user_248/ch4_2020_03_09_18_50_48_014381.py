def classifica_idade(idade):
    if int(idade) <= 11:
        return "crianca"
    else:
        if int(idade) <= 17:
            return "adolescente"
        else:
            return "adulto"
