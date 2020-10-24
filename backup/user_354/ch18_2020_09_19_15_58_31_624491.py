def verifica_idade(idade):
    if idade >= 21:
        return ("liberado nos eua e brasil")
    else:
        if idade >= 18:
            return ("liberado no brasil")
        else:
            return ("nao liberado")
        return
    