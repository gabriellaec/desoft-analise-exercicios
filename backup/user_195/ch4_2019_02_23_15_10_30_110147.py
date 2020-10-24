def classifica_idade(idade):
    if idade<=11:
        return str ("crianca")
    elif idade>=12 and idade<=17:
        return str("adolescente")
    elif idade>=18:
        return str("adulto")
print(classifica_idade(15))