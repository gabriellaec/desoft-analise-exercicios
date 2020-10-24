def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif idade <= 17 or idade >= 12:
        return "adolescente"
    else:
        return "adulto"
    
