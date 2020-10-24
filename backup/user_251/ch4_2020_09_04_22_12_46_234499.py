def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    else:
        if idade >= 12 and idade <=17:
            return "adolescente"
        else:
            return "adulto"


print(classifica_idade(6))
print(classifica_idade(15))
print(classifica_idade(22))
