def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif idade <=17:
        return "adolescente"
    else idade >= 18:
        return "adulto"