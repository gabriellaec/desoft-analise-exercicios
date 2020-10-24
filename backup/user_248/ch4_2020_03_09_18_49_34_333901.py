def classifica_idade(idade):
    if int(idade) <= 11:
        return "criança"
    else:
        if int(idade) <= 17:
            return "adolescente"
        else:
            return "adulto"
print(classifica_idade(10))