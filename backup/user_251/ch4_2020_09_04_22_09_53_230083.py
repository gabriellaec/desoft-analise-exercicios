def classifica_idade(idade):
    if idade <= 7:
        return "crianca"
    else:
        if idade >= 12 and idade <=17:
            return "adolescente"
        else:
            return "adulto"



print(classifica_idade(15))
